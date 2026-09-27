print("=" * 55)
print("        AIRCRAFT MAINTENANCE CALCULATOR")
print("=" * 55)

aircraft = input("Enter aircraft name/model: ")
current_hours = float(input("Enter current aircraft hours: "))

maintenance_tasks = []

while True:
    print("\n--- Add Maintenance Task ---")

    task = input("Enter component/task name: ")
    interval = float(input("Maintenance interval (hours): "))
    last_service = float(input("Aircraft hours at last service: "))
    cost = float(input("Estimated maintenance cost (₹): "))

    next_service = last_service + interval
    remaining = next_service - current_hours

    if remaining < 0:
        status = "OVERDUE"
    elif remaining <= 50:
        status = "DUE SOON"
    else:
        status = "OK"

    maintenance_tasks.append({
        "task": task,
        "interval": interval,
        "last_service": last_service,
        "next_service": next_service,
        "remaining": remaining,
        "cost": cost,
        "status": status
    })

    choice = input("\nAdd another maintenance task? (y/n): ").lower()

    if choice != "y":
        break


# Display maintenance report
print("\n")
print("=" * 65)
print("             AIRCRAFT MAINTENANCE REPORT")
print("=" * 65)

print(f"Aircraft: {aircraft}")
print(f"Current Flight Hours: {current_hours}")

total_cost = 0

for item in maintenance_tasks:

    print("\n---------------------------------------------")
    print(f"Component/Task : {item['task']}")
    print(f"Service Interval: {item['interval']} hours")
    print(f"Last Service   : {item['last_service']} hours")
    print(f"Next Service   : {item['next_service']} hours")

    if item["remaining"] >= 0:
        print(f"Hours Remaining: {item['remaining']} hours")
    else:
        print(f"Overdue By     : {abs(item['remaining'])} hours")

    print(f"Status         : {item['status']}")
    print(f"Estimated Cost : ₹{item['cost']:.2f}")

    total_cost += item["cost"]


print("\n" + "=" * 65)
print(f"TOTAL ESTIMATED MAINTENANCE COST: ₹{total_cost:.2f}")

# Overall aircraft status
overdue = sum(1 for x in maintenance_tasks if x["status"] == "OVERDUE")
due_soon = sum(1 for x in maintenance_tasks if x["status"] == "DUE SOON")

print("\nOVERALL STATUS:")

if overdue > 0:
    print("AIRCRAFT REQUIRES MAINTENANCE")
elif due_soon > 0:
    print("SOME MAINTENANCE TASKS ARE DUE SOON")
else:
    print("ALL MAINTENANCE TASKS ARE WITHIN LIMITS")

print("=" * 65)
