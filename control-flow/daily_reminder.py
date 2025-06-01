task = input("Enter your task: ")
priority = input("Priority (high, medium, low):").lower()
time_bound = input("Is it time-bound? (yes or no):").lower()
# Process priority using match-case
match priority:
    case 'high':
        message = f"Reminder: '{task}' is a HIGH priority task."
    case 'medium':
        message = f"Reminder: '{task}' is a MEDIUM priority task."
    case 'low':
        message = f"Reminder: '{task}' is a LOW priority task."
    case _:
        message = f"Reminder: '{task}' has an UNKNOWN priority."
# Add urgency for time-bound tasks
if time_bound == 'yes':
    message += " This task requires immediate attention today!"
print(message)
