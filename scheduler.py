def get_status(remaining_hours):
    if remaining_hours < 0:
        return "OVERDUE"
    elif remaining_hours <= 50:
        return "DUE SOON"
    else:
        return "OK"

def get_overall_status(maintenance_tasks):
    overdue = sum(
    1 for task in maintenance_tasks
    if task.status == "OVERDUE"
    )
    due_soon = sum(
    1 for task in maintenance_tasks
    if task.status == "DUE SOON")

    if overdue > 0:
        return "AIRCRAFT REQUIRES MAINTENANCE"
    elif due_soon > 0:
        return "SOME MAINTENANCE TASKS ARE DUE SOON"
    else:
        return "ALL MAINTENANCE TASKS ARE WITHIN LIMITS"

print(get_status(690))


