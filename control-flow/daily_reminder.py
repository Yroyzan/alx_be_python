task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        details = f"'{task}' is a high priority task"
    case "medium":
        details = f"'{task}' is a medium priority task"
    case "low":
        details = f"'{task}' is a low priority task"
    case _:
        details = f"'{task}' has an unknown priority"

if time_bound == "yes":
    details += " that requires immediate attention today!"
elif time_bound == "no" and priority != "high":
    details += ". Consider completing it when you have free time."

# Final print that starts with "Reminder:"
print(f"Reminder: {details}")
