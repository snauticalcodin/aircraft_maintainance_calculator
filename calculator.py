def calculate_next_service(last_service, interval):
    return last_service + interval

def calculate_remaining_hours(next_service, current_hours):
    return next_service - current_hours

def calculate_total_cost(maintenance_tasks):
    total = 0
    for task in maintenance_tasks:
        total += task.cost
        return total
