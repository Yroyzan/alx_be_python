task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

<<<<<<< HEAD
# Match-case for priority and base message
=======
>>>>>>> e5db128 (Update daily_reminder.py)
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task", end="")
    case "low":
        print(f"Reminder: '{task}' is a low priority task", end="")
    case _:
<<<<<<< HEAD
        print(f"Reminder: '{task}' has an unknown priority level", end="")

# Append time-bound info
if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(". Consider completing it when you have free time.")
=======
        message = f"Note: '{task}' has an unknown priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority != "high":
    message += ". Consider completing it when you have free time."

print(message)
>>>>>>> e5db128 (Update daily_reminder.py)
