from pathlib import Path

import pandas as pd
import csv

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "Results.csv"

def load_results():
    results = []

    if not DATA_FILE.exists():
        return results

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row:
                results.append(row)

    return results

def display_saved_results(results):
    print()
    print("Saved Results")
    print("-------------")

    if len(results) == 0:
        print("No saved results yet.")
    else:
        for result in results:
            print(f"{result['date']} | {result['event']} | {result['mark']} | {result['meet']}")
 

def show_welcome():
    print("Welcome to Track Career Analyzer")
    print("This app will grow throughout the Python bootcamp.")


def calculate_best_result(results):
    return min(results)


def compare_to_goal(current_pr, goal_mark):
    difference = current_pr - goal_mark

    if current_pr < goal_mark:
        print("Goal reached!")
    elif current_pr == goal_mark:
        print("Exactly at the goal!")
    else:
        print("Still chasing the goal.")

    print(f"Difference: {difference} seconds")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_athlete_profile():
    athlete_name = input("Athlete name: ")
    graduation_year = int(get_number("Graduation year: "))
    primary_event = input("Primary event: ")
    current_pr = get_number("Current PR (seconds): ")
    goal_mark = get_number("Goal mark (seconds): ")

    return athlete_name, graduation_year, primary_event, current_pr, goal_mark


def display_athlete_profile(athlete_name, graduation_year, primary_event, current_pr, goal_mark):
    print()
    print("Athlete Profile")
    print("---------------")
    print(f"Name: {athlete_name}")
    print(f"Graduation year: {graduation_year}")
    print(f"Primary event: {primary_event}")
    print(f"Current PR: {current_pr}")
    print(f"Goal mark: {goal_mark}")


def collect_results():
    results = []

    for number in range(3):
        result = float(input(f"Enter result #{number + 1}: "))
        results.append(result)

    return results


def display_results(results):
    print()
    print("Results Summary")
    print("---------------")

    for result in results:
        print(result)

    print(f"Number of results: {len(results)}")
    best_result = calculate_best_result(results)
    print(f"Best result: {best_result}")

def add_result():
    date = input("Date (YYYY-MM-DD): ")
    event = input("Event: ")
    mark = input("Mark: ")
    meet = input("Meet: ")
    notes = input("Notes: ")

    return {
        "date": date,
        "event": event,
        "mark": mark,
        "meet": meet,
        "notes": notes,
    }

def save_result(result):
    fieldnames = ["date", "event", "mark", "meet", "notes"]

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(result)

def load_results_dataframe():
    return pd.read_csv(DATA_FILE, on_bad_lines="skip")

def analyze_event(df, event_name):
    event_results = df[df["event"] == event_name]

    if len(event_results) == 0:
        print("No results found for that event.")
    else:
        best_result = event_results["mark"].min()
        average_result = event_results["mark"].mean()
        number_of_results = len(event_results)

        print(f"Best {event_name}: {best_result}")
        print(f"Average {event_name}: {average_result}")
        print(f"Number of {event_name} results: {number_of_results}")


show_welcome()

#athlete_name, graduation_year, primary_event, current_pr, goal_mark = get_athlete_profile()
#display_athlete_profile(athlete_name, graduation_year, primary_event, current_pr, goal_mark)
#compare_to_goal(current_pr, goal_mark)

print("\nThanks for using Track Career Analyzer!")

#results = collect_results()
#display_results(results)

saved_results = load_results()
display_saved_results(saved_results)

print("\nDataframe preview:")
df = load_results_dataframe()
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("Head:")
print(df.head())

df["mark"] = pd.to_numeric(df["mark"])
results_by_event = df["event"].value_counts()
print(results_by_event)
best_by_event = df.groupby("event")["mark"].min()
print(best_by_event)
average_by_event = df.groupby("event")["mark"].mean()
print(average_by_event)
sorted_results = df.sort_values("mark")
print(sorted_results)
event_name = input("Event to analyze: ")
event_results = df[df["event"] == event_name]
print(event_results)

event_name = input("Event to analyze: ")
analyze_event(df, event_name)

