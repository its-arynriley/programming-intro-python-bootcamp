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


show_welcome()

athlete_name, graduation_year, primary_event, current_pr, goal_mark = get_athlete_profile()
display_athlete_profile(athlete_name, graduation_year, primary_event, current_pr, goal_mark)
compare_to_goal(current_pr, goal_mark)

print("\nThanks for using Track Career Analyzer!")

results = collect_results()
display_results(results)