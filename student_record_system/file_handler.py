"""CSV and JSON storage helpers."""
import csv
import json
from pathlib import Path

FIELDS = ["student_id", "name", "age", "course", "marks", "email"]


class CSVHandler:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))
            for row in rows:
                row["age"] = int(row["age"])
                row["marks"] = float(row["marks"])
            return rows
        except (OSError, csv.Error, ValueError, KeyError) as error:
            raise OSError(f"Could not read CSV data: {error}") from error

    def save(self, records):
        try:
            with self.path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(records)
        except OSError as error:
            raise OSError(f"Could not write CSV data: {error}") from error


class JSONHandler:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON root must be a list of student records.")
            return data
        except (OSError, json.JSONDecodeError, ValueError) as error:
            raise OSError(f"Could not read JSON data: {error}") from error

    def save(self, records):
        try:
            with self.path.open("w", encoding="utf-8") as file:
                json.dump(records, file, indent=4)
        except OSError as error:
            raise OSError(f"Could not write JSON data: {error}") from error
