from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent / "data" / "results.csv"


def load_results():
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=["date", "event", "mark", "meet", "notes"])

    results = pd.read_csv(DATA_FILE, on_bad_lines="skip")

    if "mark" in results.columns:
        results["mark"] = pd.to_numeric(results["mark"], errors="coerce")
        results = results.dropna(subset=["mark"])

    return results


st.set_page_config(
    page_title="Track Career Analyzer",
    layout="centered",
)

st.title("Track Career Analyzer")
st.write("Analyze saved track results from a CSV file.")

results = load_results()

if results.empty:
    st.info("No valid results were loaded. Please check app/data/results.csv.")
    st.stop()

st.subheader("Results")
st.dataframe(results, use_container_width=True)

st.subheader("Athlete Profile")
athlete_name = st.text_input("Athlete name", "Riley")
primary_event = st.text_input("Primary event", "400m")
st.write(f"{athlete_name} is analyzing results for {primary_event}.")

events = sorted(results["event"].dropna().unique())
selected_event = st.selectbox("Event", events)
event_results = results[results["event"] == selected_event]

best_mark = event_results["mark"].min()
average_mark = event_results["mark"].mean()
result_count = len(event_results)

st.subheader("Event Summary")
st.metric("Best mark", f"{best_mark:.2f}")
st.metric("Average mark", f"{average_mark:.2f}")
st.metric("Number of results", result_count)

goal_mark = st.number_input("Goal mark", min_value=0.0, value=float(best_mark), step=0.01)

if best_mark < goal_mark:
    st.success("Goal reached!")
elif best_mark == goal_mark:
    st.info("Exactly at the goal.")
else:
    difference = best_mark - goal_mark
    st.warning(f"Still chasing. Difference: {difference:.2f}")

chart_data = event_results[["date", "mark"]].set_index("date")
st.line_chart(chart_data)
