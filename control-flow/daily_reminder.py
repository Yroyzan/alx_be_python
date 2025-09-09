# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority and base message
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task", end="")
    case "low":
        print(f"Reminder: '{task}' is a low priority task", end="")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level", end="")

# Append time-bound info
if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(". Consider completing it when you have free time.")
