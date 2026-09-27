# Aircraft Maintenance System

## About the Project

This is a Python project for keeping track of basic aircraft maintenance requirements based on flight hours.

The program takes the aircraft's current flight hours and allows the user to enter different maintenance tasks, their service intervals, last service hours, and estimated costs. It then calculates when each task is due and shows whether it is **OK, DUE SOON, or OVERDUE**.

I made this project to apply Python programming concepts to an aerospace-related problem instead of building a completely generic calculator.

## Features

* Enter aircraft name/model
* Enter current aircraft flight hours
* Add multiple maintenance tasks
* Set service intervals in hours
* Enter the hours at the last service
* Calculate the next service hour
* Show remaining or overdue hours
* Mark tasks as `OK`, `DUE SOON`, or `OVERDUE`
* Calculate total estimated maintenance cost
* Generate a maintenance report
* Basic input validation
* Unit tests for the main calculations

## Technologies Used

### Programming

* Python 3
* Functions and modules
* Lists and dictionaries
* Classes and objects
* Dataclasses
* Exception handling
* JSON

### Tools

* Visual Studio Code
* Git and GitHub
* Python unittest
* draw.io / diagrams.net

The project only uses Python's standard library, so there are no external packages to install.

## Installation

### 1. Install Python

Python 3.9 or newer is recommended.

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/snauticalcodin/aircraft-maintainance-calculator
```

### 3. Open the project folder

```bash
cd aircraft-maintenance-system
```

### 4. Install the requirements

There are currently no external dependencies, but the requirements file is included for the project setup.

```bash
pip install -r requirements.txt
```

## Running the Program

From the main project folder:

```bash
python src/main.py
```

The program will ask for:

* Aircraft name/model
* Current aircraft hours
* Maintenance task
* Maintenance interval
* Hours at last service
* Estimated maintenance cost

After entering the information, it generates a maintenance report.

### How the calculation works

```text
Next Service = Last Service + Maintenance Interval

Remaining Hours = Next Service - Current Aircraft Hours
```

The program uses these conditions:

* Less than 0 hours remaining → `OVERDUE`
* 0 to 50 hours remaining → `DUE SOON`
* More than 50 hours remaining → `OK`

## Testing

The project contains tests for the aircraft, calculator, and maintenance modules.

Run all tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

The tests check:

* Creating an aircraft
* Invalid flight hours
* Next service calculation
* Remaining service hours
* Invalid maintenance intervals
* Maintenance status
* Overdue tasks

A successful test run should end with:

```text
----------------------------------------------------------------------
Ran 8 tests

OK
```

## Future Improvements

Some things I would like to add later:

* GUI instead of the current terminal interface
* Saving and loading maintenance records
* Maintenance history
* Support for multiple aircraft
* Automatic reminders
* Graphs for maintenance costs
* PDF reports
* More types of maintenance schedules

## Note

This is a student/educational project. The calculations are simplified and should not be used as a replacement for actual aircraft maintenance documentation, manufacturer maintenance manuals, or approved maintenance procedures.
