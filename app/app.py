print("Welcome to Track Career Analyzer")
print("This app will grow throughout the Python bootcamp.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


athlete_name = input("Athlete name: ")
graduation_year = int(get_number("Graduation year: "))
primary_event = input("Primary event: ")
current_pr = get_number("Current PR (seconds): ")
goal_mark = get_number("Goal mark (seconds): ")

print("\nAthlete Profile")
print("---------------")
print(f"Name: {athlete_name}")
print(f"Graduation year: {graduation_year}")
print(f"Primary event: {primary_event}")
print(f"Current PR: {current_pr} seconds")
print(f"Goal mark: {goal_mark} seconds")

if current_pr < goal_mark:
    print("Goal reached!")
elif current_pr == goal_mark:
    print("Exactly at the goal!")
else:
    print("Still chasing the goal.")

difference = current_pr - goal_mark
print(f"Difference: {difference} seconds")

print("\nThanks for using Track Career Analyzer!")

results = []
first_result = float(input("First result: "))
second_result = float(input("Second result: "))
third_result = float(input("Third result: "))

results.append(first_result)
results.append(second_result)
results.append(third_result)

print("Meet Results")
print("------------")

if not results:
    print("No results entered yet.")
else:
    for result in results:
        print(result)

number_of_results = len(results)
print(f"Number of results: {number_of_results}")

if results:
    best_result = min(results)
    print(f"Best result: {best_result}")
else:
    print("No results available for best result.")
for number in range(3):
    result = float(input(f"Enter result #{number + 1}: "))
    results.append(result)
print()
print("Results Summary")
print("---------------")

for result in results:
    print(result)

print(f"Number of results: {len(results)}")
print(f"Best result: {min(results)}")