# User prompts
task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

# Match cases
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a medium/low priority task. Consider completing it when you have time.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires your attention today!")
        else:
            print(f"{task} is a medium priority task but not time-bound. Consider completing it when you have time.")

    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task but is time-bound. Consider completing it as soon as you can.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

