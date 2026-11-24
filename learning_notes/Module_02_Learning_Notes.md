# Module 02 – Functions, Files & Exception Handling
## Python Programming Internship | Codomax Digital Solutions

**Student:** Prashanth Reddy S  
**Level:** Beginner  
**Module dates:** 29 November 2026 – 03 December 2026

> Learning notes for study and revision. Run the examples yourself and adapt them as you practise.

## 1. Functions

A function is a reusable block of code that performs a particular task. Functions reduce repetition and make programs easier to organize, test, and maintain.

### Defining and calling a function
```python
def greet():
    print("Hello!")

greet()
```
Output:
```text
Hello!
```

### Parameters and arguments
A parameter is a variable in a function definition. An argument is the value passed when calling the function.
```python
def greet_user(name):
    print("Hello,", name)

greet_user("Prashanth")
```
Output: `Hello, Prashanth`

### Return values
`return` sends a result back to the caller.
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```
Output: `30`

### Default and keyword arguments
```python
def introduce(name, city="Bengaluru"):
    return f"{name} lives in {city}"

print(introduce("Prashanth"))
print(introduce(name="Asha", city="Mysuru"))
```

### Variable-length arguments
`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.
```python
def total(*numbers):
    return sum(numbers)

def show_profile(**details):
    for key, value in details.items():
        print(key, value)

print(total(2, 3, 4))
show_profile(name="Asha", course="Python")
```

## 2. Lambda Functions

A lambda is a small anonymous function written as a single expression.
```python
square = lambda number: number * number
print(square(5))
```
Output: `25`

Lambda functions are useful for short operations, such as a sorting key:
```python
students = [("Asha", 82), ("Ravi", 91), ("Meena", 76)]
students_sorted = sorted(students, key=lambda item: item[1])
print(students_sorted)
```

Use a regular `def` function when the logic needs multiple statements or a descriptive reusable name.

## 3. List Comprehensions

A list comprehension creates a list from an iterable, optionally applying an expression and condition.
```python
squares = [number ** 2 for number in range(1, 6)]
print(squares)
```
Output: `[1, 4, 9, 16, 25]`

With a condition:
```python
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print(even_numbers)
```
Output: `[2, 4, 6, 8, 10]`

## 4. File Handling

Python can read from and write to files. The `open()` function opens a file. Using `with` is recommended because it closes the file automatically, including when an error occurs.

Common modes:
- `r`: read an existing file.
- `w`: write; creates or overwrites a file.
- `a`: append to the end of a file.
- `x`: create a new file; raises an error if it already exists.

Example:
```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python file handling.")

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```
Output: `Learning Python file handling.`

## 5. CSV Files

CSV means Comma-Separated Values. It is commonly used for tabular data. Python's built-in `csv` module can read and write CSV files.
```python
import csv

rows = [
    ["student_id", "name", "marks"],
    ["S001", "Asha", 88],
    ["S002", "Ravi", 91],
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## 6. JSON Files

JSON (JavaScript Object Notation) is a text format for structured data. Python's `json` module converts between Python objects and JSON text.

- `json.dump()` writes a Python object to a file.
- `json.load()` reads JSON from a file.
- `json.dumps()` converts a Python object to a JSON string.
- `json.loads()` parses a JSON string.

```python
import json

student = {"student_id": "S001", "name": "Asha", "marks": 88}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print(loaded_student["name"])
```
Output: `Asha`

## 7. Exception Handling

An exception is an error detected while a program is running. Handling exceptions lets a program respond safely instead of terminating unexpectedly.

### try and except
```python
try:
    number = int("abc")
except ValueError:
    print("Please provide a valid integer.")
```
Output: `Please provide a valid integer.`

### else and finally
- `else` runs when the `try` block has no exception.
- `finally` runs whether an exception occurred or not.
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Operation completed.")
```

### Raising an exception
```python
def validate_marks(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return marks

print(validate_marks(85))
```

Catch specific exceptions rather than using a broad `except:` clause. Avoid hiding errors silently.

## 8. Debugging Techniques

Debugging is the process of finding and fixing defects in a program.

Useful techniques:
1. Read the full traceback and identify the line where the error occurred.
2. Check variable values with `print()` statements.
3. Reproduce the issue using a small example.
4. Use breakpoints and step-through debugging in VS Code.
5. Check spelling, indentation, data types, and file paths.
6. Test normal inputs, boundary values, and invalid inputs.

Common errors:
- `SyntaxError`: invalid Python syntax.
- `NameError`: a name is not defined.
- `TypeError`: an operation is used with an unsuitable type.
- `ValueError`: a value has the right general type but is invalid for the operation.
- `FileNotFoundError`: a requested file does not exist.
- `ZeroDivisionError`: division by zero.

## 9. Virtual Environments

A virtual environment isolates project dependencies from other Python projects.

Create one:
```bash
python -m venv .venv
```

Activate on Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:
```bash
source .venv/bin/activate
```

Deactivate:
```bash
deactivate
```

List installed packages:
```bash
python -m pip list
```

Save dependencies:
```bash
python -m pip freeze > requirements.txt
```

Install saved dependencies:
```bash
python -m pip install -r requirements.txt
```

A virtual environment is not the same as a Python installation; it provides an isolated environment for a project.

## 10. CRUD Operations and Student Record Management

CRUD stands for:
- **Create:** add a new student record.
- **Read:** view or search saved records.
- **Update:** edit an existing record.
- **Delete:** remove a record.

A student record may contain a student ID, name, age, course, marks, and email. The Module 02 project uses functions and file handling to store records in CSV or JSON format.

Example record:
```python
student = {
    "student_id": "S001",
    "name": "Asha",
    "age": 20,
    "course": "Python",
    "marks": 88,
    "email": "asha@example.com"
}
```

## 11. Learning Summary

In this module, I studied reusable functions, parameters, return values, lambda functions, and list comprehensions. I learned how to read and write text, CSV, and JSON files, create virtual environments, and handle runtime errors with `try`, `except`, `else`, and `finally`. I applied these concepts in a Student Record Management System that performs create, read, update, and delete operations with local file storage.

## 12. Practice Checklist

- [ ] Define and call functions.
- [ ] Use positional, keyword, and default parameters.
- [ ] Return values from functions.
- [ ] Write lambda functions.
- [ ] Create lists using list comprehensions.
- [ ] Read and write text files.
- [ ] Read and write CSV files.
- [ ] Read and write JSON files.
- [ ] Handle exceptions using try/except/else/finally.
- [ ] Create and activate a virtual environment.
- [ ] Run the Student Record Management System.
- [ ] Test all four CRUD operations in CSV and JSON modes.
