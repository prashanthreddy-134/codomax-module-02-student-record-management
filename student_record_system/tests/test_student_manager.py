import tempfile
import unittest
from student_manager import StudentManager


SAMPLE = {
    "student_id": "S001",
    "name": "Asha",
    "age": 20,
    "course": "Python",
    "marks": 88,
    "email": "asha@example.com",
}


class StudentManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.manager = StudentManager("csv", self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_and_read(self):
        self.manager.add_student(SAMPLE)
        self.assertEqual(self.manager.get_student("S001")["name"], "Asha")

    def test_duplicate_id_rejected(self):
        self.manager.add_student(SAMPLE)
        with self.assertRaises(ValueError):
            self.manager.add_student(SAMPLE)

    def test_update(self):
        self.manager.add_student(SAMPLE)
        updated = dict(SAMPLE, name="Asha Rao")
        self.assertTrue(self.manager.update_student("S001", updated))
        self.assertEqual(self.manager.get_student("S001")["name"], "Asha Rao")

    def test_delete(self):
        self.manager.add_student(SAMPLE)
        self.assertTrue(self.manager.delete_student("S001"))
        self.assertIsNone(self.manager.get_student("S001"))

    def test_invalid_marks_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student(dict(SAMPLE, marks=150))


if __name__ == "__main__":
    unittest.main()
