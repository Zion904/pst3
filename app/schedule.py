import json
from app.student import StudentUser
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        # TODO: Initialize the new attendance_log attribute as an empty list.
        self.attendance_log = []
        # ... (next_id counters) ...
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # Load students, teachers, and courses as before.
            self.students = []
            for stu_dict in data.get("students", []):
                self.students.append(StudentUser.from_dict(stu_dict))

            # 老师
            self.teachers = []
            for teacher_dict in data.get("teachers", []):
                self.teachers.append(TeacherUser.from_dict(teacher_dict))

            # 课程
            self.courses = []
            for course_dict in data.get("courses", []):
                self.courses.append(Course.from_dict(course_dict))

                # Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
            self.attendance_log = data.get("attendance", [])
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
            self.students, self.teachers, self.courses, self.attendance_log = [], [], [], []
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # Create a 'data_to_save' dictionary.
        data_to_save = {
            "students": [s.to_dict() for s in self.students],
            "teachers": [t.to_dict() for t in self.teachers],
            "courses": [c.to_dict() for c in self.courses],
            # Add the attendance_log to the dictionary to be saved.
            # Since it's already a list of dicts, no conversion is needed.
            "attendance": self.attendance_log,
            # ... (next_id counters) ...
        }
        # Write 'data_to_save' to the JSON file.
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4,ensure_ascii = False)

    def get_lessons_by_day(self, day):
        """return [(course_obj, lesson_dict), ...], used for print lessons"""
        results = []
        for course in self.courses:
            for lesson in course.lessons:
                if str(lesson.get("day", "")).lower() == str(day).lower():
                    results.append((course, lesson))
        return results
    
    

    def check_in(self, student_id, course_id):
        """Records a student's attendance for a course after validation."""
        # This implementation remains the same, but it will now function correctly.
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        
        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False
        
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        check_in_record = {"student_id": student_id, "course_id": course_id, "timestamp": timestamp}
        
        # This line will now work without causing an AttributeError.
        self.attendance_log.append(check_in_record)
        self._save_data() # This will now correctly save the attendance log.
        print(f"Success: Student {student.name} checked into {course.name}.")
        return True

    # Also implement find_student_by_id and find_course_by_id helper methods.
    def find_student_by_id(self, student_id):
        for s in self.students:
            if s.user_id == int(student_id):
                return s
            return None
        
    def find_course_by_id(self, course_id):
        for c in self.courses:
            if c.id == int(course_id):
                return c
            return None