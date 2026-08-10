import csv
from pathlib import Path

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
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = DATA_FILE.exists()

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)


show_welcome()

saved_results = load_results()
display_saved_results(saved_results)

new_result = add_result()
save_result(new_result)

saved_results = load_results()
display_saved_results(saved_results)

print("\nThanks for using Track Career Analyzer!")
