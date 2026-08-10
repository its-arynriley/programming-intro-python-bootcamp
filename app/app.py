import csv
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent / "data" / "results.csv"
FIELDNAMES = ["date", "event", "mark", "meet", "notes"]


def show_welcome():
    print("Welcome to Track Career Analyzer")
    print("This app will grow throughout the Python bootcamp.")
    print("Phase 01 is about running and editing Python code.")


def load_results():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def display_saved_results(results):
    print()
    print("Saved Results")
    print("-------------")

    if len(results) == 0:
        print("No saved results yet.")
    else:
        for result in results:
            print(f"{result['date']} | {result['event']} | {result['mark']} | {result['meet']}")


def load_results_dataframe():
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=FIELDNAMES)

    return pd.read_csv(DATA_FILE, on_bad_lines="skip")


def prepare_results_dataframe(df):
    if df.empty:
        return df

    df = df.copy()
    df["mark"] = pd.to_numeric(df["mark"], errors="coerce")
    return df.dropna(subset=["mark"])


def display_dataframe_summary(df):
    print()
    print("DataFrame Preview")
    print("-----------------")

    if df.empty:
        print("No saved data to analyze yet.")
        return

    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
    print(df.head())


def display_event_statistics(df):
    print()
    print("Event Statistics")
    print("----------------")

    if df.empty:
        print("No numeric marks to analyze yet.")
        return

    print("Results by event:")
    print(df["event"].value_counts())

    print()
    print("Best mark by event:")
    print(df.groupby("event")["mark"].min())

    print()
    print("Average mark by event:")
    print(df.groupby("event")["mark"].mean())


def analyze_event(df, event_name):
    event_results = df[df["event"] == event_name]

    print()
    print(f"{event_name} Analysis")
    print("-" * (len(event_name) + 9))

    if len(event_results) == 0:
        print("No results found for that event.")
        return

    print(event_results.sort_values("mark"))
    print(f"Best {event_name}: {event_results['mark'].min()}")
    print(f"Average {event_name}: {event_results['mark'].mean()}")
    print(f"Number of {event_name} results: {len(event_results)}")


show_welcome()

saved_results = load_results()
display_saved_results(saved_results)

df = load_results_dataframe()
df = prepare_results_dataframe(df)
display_dataframe_summary(df)
display_event_statistics(df)

if not df.empty:
    event_name = input("Event to analyze: ")
    analyze_event(df, event_name)

print("\nThanks for using Track Career Analyzer!")
