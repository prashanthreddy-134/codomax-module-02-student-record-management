# Student Record Management System

A beginner-friendly command-line Python application demonstrating functions, parameters, return values, file handling, CSV, JSON, exception handling, and CRUD operations.

## Features

- Create, read, search, update, and delete student records.
- Store records persistently in CSV or JSON format.
- Validate required fields, age, marks, and duplicate student IDs.
- Handle invalid input and file errors.
- Uses only the Python standard library.

## Student fields

`student_id`, `name`, `age`, `course`, `marks`, `email`

## Requirements

- Python 3.9 or newer
- No external packages required

## Setup

```bash
python --version
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

## Run with CSV storage (default)

```bash
python main.py
```

Data is saved in `data/students.csv`.

## Run with JSON storage

```bash
python main.py --format json
```

Data is saved in `data/students.json`.

CSV and JSON are separate storage files. Choose one format for a given run; the application does not automatically synchronize the two files.

## Run tests

From this folder:

```bash
python -m unittest discover -s tests -v
```

## CRUD menu

1. Add student
2. View all students
3. Search student by ID
4. Update student
5. Delete student
6. Exit

## Concepts demonstrated

- Functions and reusable modules
- Parameters, arguments, and return values
- File handling with `with`
- CSV and JSON serialization
- Exception handling and input validation
- Virtual environments
- Unit testing

## Example record

```json
{
    "student_id": "S001",
    "name": "Asha",
    "age": 20,
    "course": "Python",
    "marks": 88.0,
    "email": "asha@example.com"
}
```

## Limitations

This is a local, single-user learning project. It does not include authentication, a database server, a graphical interface, or concurrent multi-user access.
