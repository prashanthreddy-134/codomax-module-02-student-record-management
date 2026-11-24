"""Business logic for student records with CSV or JSON persistence."""
from pathlib import Path
from file_handler import CSVHandler, JSONHandler


REQUIRED_FIELDS = ("student_id", "name", "age", "course", "marks", "email")


class StudentManager:
    def __init__(self, storage_format="csv", data_dir=None):
        if storage_format not in {"csv", "json"}:
            raise ValueError("Storage format must be 'csv' or 'json'.")
        self.storage_format = storage_format
        self.data_dir = Path(data_dir) if data_dir else Path(__file__).parent / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.file_path = self.data_dir / f"students.{storage_format}"
        self.handler = CSVHandler(self.file_path) if storage_format == "csv" else JSONHandler(self.file_path)

    @staticmethod
    def _validate(student):
        missing = [field for field in REQUIRED_FIELDS if field not in student]
        if missing:
            raise ValueError(f"Missing fields: {', '.join(missing)}")
        clean = dict(student)
        clean["student_id"] = str(clean["student_id"]).strip()
        clean["name"] = str(clean["name"]).strip()
        clean["course"] = str(clean["course"]).strip()
        clean["email"] = str(clean["email"]).strip()
        if not all(clean[key] for key in ("student_id", "name", "course", "email")):
            raise ValueError("ID, name, course, and email cannot be empty.")
        try:
            clean["age"] = int(clean["age"])
            clean["marks"] = float(clean["marks"])
        except (TypeError, ValueError) as error:
            raise ValueError("Age must be an integer and marks must be numeric.") from error
        if clean["age"] <= 0:
            raise ValueError("Age must be a positive integer.")
        if not 0 <= clean["marks"] <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        return clean

    def get_all_students(self):
        return self.handler.load()

    def get_student(self, student_id):
        return next((s for s in self.get_all_students()
                     if s["student_id"] == str(student_id)), None)

    def add_student(self, student):
        clean = self._validate(student)
        records = self.get_all_students()
        if any(s["student_id"] == clean["student_id"] for s in records):
            raise ValueError(f"Student ID '{clean['student_id']}' already exists.")
        records.append(clean)
        self.handler.save(records)

    def update_student(self, student_id, updated_student):
        clean = self._validate(updated_student)
        if clean["student_id"] != str(student_id):
            raise ValueError("Student ID cannot be changed.")
        records = self.get_all_students()
        for index, record in enumerate(records):
            if record["student_id"] == str(student_id):
                records[index] = clean
                self.handler.save(records)
                return True
        return False

    def delete_student(self, student_id):
        records = self.get_all_students()
        remaining = [s for s in records if s["student_id"] != str(student_id)]
        if len(remaining) == len(records):
            return False
        self.handler.save(remaining)
        return True
