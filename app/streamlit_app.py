from pathlib import Path
from fractions import Fraction
import re

import altair as alt
import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent / "data" / "results.csv"
SEASON_PATTERN = re.compile(r"\b(20\d{2})\s+(Indoor|Outdoor|Cc|XC|Cross Country)\b", re.IGNORECASE)
INCHES_TO_METERS = 0.0254
OVERVIEW_PR_EVENTS = ["Shot Put", "Discus", "Long Jump", "55m", "300m", "300H"]

def load_results():
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=["date", "event", "mark", "meet", "notes"])

    results = pd.read_csv(DATA_FILE, on_bad_lines="skip")

    if "mark" in results.columns:
        results["mark"] = pd.to_numeric(results["mark"], errors="coerce")
        results = results.dropna(subset=["mark"])

    if "date" in results.columns:
        results["date"] = pd.to_datetime(results["date"], errors="coerce")
        results = results.dropna(subset=["date"])

    return results


def extract_season(notes):
    match = SEASON_PATTERN.search(str(notes))
    if not match:
        return "Unknown Season"

    year, season = match.groups()
    season_name = "XC" if season.lower() in {"cc", "xc", "cross country"} else season.title()
    return f"{year} {season_name}"


def is_field_event(event_results):
    return event_results["notes"].astype(str).str.contains("unit inches", case=False).any()


def padded_mark_domain(marks):
    lowest_mark = marks.min()
    highest_mark = marks.max()
    mark_range = highest_mark - lowest_mark
    padding = max(mark_range * 0.12, 1.0)
    return [max(0, lowest_mark - padding), highest_mark + padding]


def format_fractional_inches(inches):
    fraction = Fraction(inches).limit_denominator(16)
    whole_inches = fraction.numerator // fraction.denominator
    remainder = fraction - whole_inches

    if remainder == 0:
        return str(whole_inches)

    if whole_inches == 0:
        return f"{remainder.numerator}/{remainder.denominator}"

    return f"{whole_inches} {remainder.numerator}/{remainder.denominator}"


def format_field_mark(total_inches):
    feet = int(total_inches // 12)
    inches = total_inches - (feet * 12)
    meters = total_inches * INCHES_TO_METERS
    return f"{feet}' {format_fractional_inches(inches)}\" / {meters:.2f} m"


def format_running_mark(seconds):
    return f"{seconds:.2f} sec"


def format_mark(mark, field_event):
    if field_event:
        return format_field_mark(mark)

    return format_running_mark(mark)


def find_personal_bests(results_table):
    personal_bests = []

    for event, event_results in results_table.groupby("event"):
        field_event = is_field_event(event_results)
        best_index = event_results["mark"].idxmax() if field_event else event_results["mark"].idxmin()
        best_result = event_results.loc[best_index].copy()
        best_result["field_event"] = field_event
        best_result["mark_display"] = format_mark(best_result["mark"], field_event)
        personal_bests.append(best_result)

    return pd.DataFrame(personal_bests).sort_values("event")


def show_personal_best_cards(personal_bests, columns_per_row=4):
    for row_start in range(0, len(personal_bests), columns_per_row):
        card_columns = st.columns(columns_per_row)
        for column, (_, personal_best) in zip(
            card_columns,
            personal_bests.iloc[row_start : row_start + columns_per_row].iterrows(),
        ):
            with column.container(border=True):
                st.markdown(f"**{personal_best['event']}**")
                st.markdown(f"### {personal_best['mark_display']}")
                st.caption(personal_best["date"].strftime("%Y-%m-%d"))
                st.caption(personal_best["meet"])


def display_results_table(results_table):
    display_table = results_table.copy()
    display_table["date"] = display_table["date"].dt.strftime("%Y-%m-%d")
    display_table["field_event"] = display_table["notes"].astype(str).str.contains(
        "unit inches", case=False
    )
    display_table["display_mark"] = display_table.apply(
        lambda row: format_mark(row["mark"], row["field_event"]), axis=1
    )
    display_table = display_table[
        ["date", "event", "display_mark", "mark", "meet", "notes"]
    ].rename(
        columns={
            "display_mark": "mark_display",
            "mark": "numeric_mark",
        }
    )
    return display_table


st.set_page_config(
    page_title="Riley Chapman Track & Field Performance Dashboard",
    layout="centered",
)

st.title("Riley Chapman Track & Field Performance Dashboard")

results = load_results()

if results.empty:
    st.info("No valid results were loaded. Please check app/data/results.csv.")
    st.stop()

results = results.sort_values("date")
results["season"] = results["notes"].apply(extract_season)
start_date = results["date"].min().date().isoformat()
end_date = results["date"].max().date().isoformat()
date_range = f"{start_date} to {end_date}"
season_count = results["season"].nunique()
event_count = results["event"].nunique()
personal_bests = find_personal_bests(results)

st.write(f"Track & Field and Cross Country (XC) results, covering my high school career {date_range}.")

overview_tab, personal_bests_tab, event_progress_tab, raw_data_tab = st.tabs(
    ["Overview", "Personal Bests", "Event Progress", "Raw Data"]
)

with overview_tab:
    summary_columns = st.columns(3)
    summary_columns[0].metric("Total Results", len(results))
    summary_columns[1].metric("Seasons", season_count)
    summary_columns[2].metric("Events", event_count)

    st.caption(f"First result: {start_date} | Latest result: {end_date}")

    st.subheader("Career Snapshot")
    st.write(
        "This dashboard summarizes Riley's meet history before showing the full data table. "
        "Use the event tools below to explore results by race or field event."
    )

    st.subheader("Top Personal Bests")
    overview_personal_bests = personal_bests[
        personal_bests["event"].isin(OVERVIEW_PR_EVENTS)
    ]
    show_personal_best_cards(overview_personal_bests, columns_per_row=2)

with personal_bests_tab:
    st.subheader("Personal Bests")
    show_personal_best_cards(personal_bests)

with event_progress_tab:
    events = sorted(results["event"].dropna().unique())
    selected_event = st.selectbox("Event", ["Choose an event..."] + events)
    if selected_event == "Choose an event...":
        st.info("Choose an event to see event-specific stats and progress.")
    else:
        event_results = results[results["event"] == selected_event]
        field_event = is_field_event(event_results)
        mark_unit = "inches" if field_event else "seconds"
        best_mark = event_results["mark"].max() if field_event else event_results["mark"].min()
        average_mark = event_results["mark"].mean()
        result_count = len(event_results)

        st.subheader("Event Summary")
        st.metric("Personal best", format_mark(best_mark, field_event))
        st.metric("Average mark", format_mark(average_mark, field_event))
        st.metric("Number of results", result_count)

        chart_results = event_results.copy()
        chart_results["date_display"] = chart_results["date"].dt.strftime("%Y-%m-%d")
        chart_results["mark_display"] = chart_results["mark"].map(
            lambda mark: format_mark(mark, field_event)
        )

        st.subheader("Event Progress")
        st.caption(
            "The chart is zoomed to this event's result range so small changes are easier to see."
        )

        base_chart = alt.Chart(chart_results).encode(
            x=alt.X(
                "date:T",
                title="Date",
                axis=alt.Axis(format="%b %Y", labelAngle=-35, tickCount=9),
            ),
            y=alt.Y(
                "mark:Q",
                title=f"Mark ({mark_unit})",
                scale=alt.Scale(domain=padded_mark_domain(chart_results["mark"]), zero=False),
            ),
        )

        line = base_chart.mark_line(color="#2563eb", strokeWidth=3)
        points = base_chart.mark_circle(color="#f97316", size=80).encode(
            tooltip=[
                alt.Tooltip("date_display:N", title="Date"),
                alt.Tooltip("meet:N", title="Meet"),
                alt.Tooltip("event:N", title="Event"),
                alt.Tooltip("mark_display:N", title="Mark"),
                alt.Tooltip("season:N", title="Season"),
            ]
        )

        st.altair_chart((line + points).properties(height=360), use_container_width=True)

        if field_event:
            st.caption("Field event marks are charted in inches and displayed as feet/inches plus meters.")

with raw_data_tab:
    st.subheader("Detailed Source Data")
    st.dataframe(display_results_table(results), use_container_width=True)
