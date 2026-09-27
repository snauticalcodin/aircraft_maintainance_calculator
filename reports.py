def generate_report(aircraft, maintenance_tasks):
    print("\n")
    print("=" * 65)
    print("             AIRCRAFT MAINTENANCE REPORT")
    print("=" * 65)

    print(f"Aircraft: {aircraft.name}")
    print(f"Current Flight Hours: {aircraft.current_hours}")

    total_cost = 0

    for item in maintenance_tasks:

        print("\n---------------------------------------------")
        print(f"Component/Task : {item.task}")
        print(f"Service Interval: {item.interval} hours")
        print(f"Last Service   : {item.last_service} hours")
        print(f"Next Service   : {item.next_service} hours")

        if item.remaining >= 0:
            print(f"Hours Remaining: {item.remaining} hours")
        else:
            print(f"Overdue By     : {abs(item.remaining)} hours")

        print(f"Status         : {item.status}")
        print(f"Estimated Cost : ₹{item.cost:.2f}")

        total_cost += item.cost

    print("\n" + "=" * 65)
    print(f"TOTAL ESTIMATED MAINTENANCE COST: ₹{total_cost:.2f}")

    print("\nOVERALL STATUS:")

    overdue = sum(
        1 for task in maintenance_tasks
        if task.status == "OVERDUE"
    )

    due_soon = sum(
        1 for task in maintenance_tasks
        if task.status == "DUE SOON"
    )

    if overdue > 0:
        print("AIRCRAFT REQUIRES MAINTENANCE")
    elif due_soon > 0:
        print("SOME MAINTENANCE TASKS ARE DUE SOON")
    else:
        print("ALL MAINTENANCE TASKS ARE WITHIN LIMITS")

    print("=" * 65)
