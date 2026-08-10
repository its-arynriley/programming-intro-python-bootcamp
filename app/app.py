print("Welcome to Track Career Analyzer")
print("This app will grow throughout the Python bootcamp.")
print("Phase 01 is about running and editing Python code.")

athlete_name = input("Athlete name: ")
graduation_year = int(input("Graduation year: "))
primary_event = input("Primary event: ")
current_pr = float(input("Current PR (seconds): "))
goal_mark = float(input("Goal mark (seconds): "))

print()
print("Athlete Profile")
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
