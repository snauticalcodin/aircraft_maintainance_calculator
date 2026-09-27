

1. Problem Statement

Aircraft require regular maintenance and inspection based on flight hours and predefined service intervals. Manually tracking these intervals can make it difficult to identify which maintenance tasks are due, approaching their service limit, or already overdue.

The Aircraft Maintenance System is developed to provide a simple digital method for recording maintenance tasks, calculating upcoming service requirements, identifying maintenance status, and estimating maintenance costs.

The project applies basic Python programming and software development concepts to a practical aerospace engineering problem.



2. Scope of the Project

The project focuses on flight-hour-based aircraft maintenance tracking.

The system will:

* Store aircraft name/model and current flight hours.
* Record individual maintenance tasks.
* Store maintenance intervals and previous service hours.
* Calculate the next required service hour.
* Calculate remaining or overdue flight hours.
* Classify maintenance tasks as **OK, DUE SOON, or OVERDUE**.
* Calculate the total estimated maintenance cost.
* Generate a maintenance report.
* Provide basic input validation.
* Include unit tests for important calculations and functions.

[] Limitations

The system is an educational prototype and does not cover:

* Manufacturer-specific maintenance programs.
* Airworthiness Directives (ADs).
* Calendar-based inspections.
* Certified maintenance records.
* Real-time aircraft data.
* Actual aircraft health monitoring.


3. Target Users

The system is intended for:

* Aerospace/Aeronautical Engineering Students — for learning how programming can be applied to aviation maintenance.
* Aviation Students and Beginners — for understanding basic maintenance scheduling concepts.
* Educational Institutions — as a Python programming project or demonstration.
* Maintenance Planning Learners — for practicing flight-hour-based maintenance tracking.

The project is not intended to replace software or procedures used by certified aircraft maintenance organizations.



4. High-Level Features

[] Aircraft Management

* Enter aircraft name/model.
* Record current aircraft flight hours.

[] Maintenance Management

* Add multiple maintenance tasks.
* Record maintenance intervals.
* Record last service hours.
* Record estimated maintenance costs.

[] Maintenance Calculation

* Calculate next service hour.
* Calculate remaining service hours.
* Identify overdue maintenance.

[] Status Monitoring

The system categorizes tasks into:

```text
Remaining Hours < 0  →  OVERDUE
Remaining Hours ≤ 50 →  DUE SOON
Remaining Hours > 50 →  OK
```

[] Reporting

* Display aircraft information.
* Display individual maintenance task details.
* Display service status.
* Display remaining/overdue hours.
* Calculate total estimated maintenance cost.
* Display overall aircraft maintenance status.

[] Testing

* Automated unit tests for aircraft data.
* Unit tests for maintenance calculations.
* Unit tests for maintenance status classification.
