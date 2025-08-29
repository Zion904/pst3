# MSMS v3 (PST3) — Object-Oriented Redesign 

## 1) Overview
This is the **Music School Management System (MSMS)** redesigned for **PST3** using object-oriented programming.

- **Models**: domain entities (`User`, `StudentUser`, `TeacherUser`, `Course`)
- **Controller**: one central brain `ScheduleManager` (load/save JSON, roster, check-in, switch course)
- **View (CLI)**: `main.py` only handles input/output and delegates to the controller
- **Data**: `data/msms.json` (students, teachers, courses, attendance)

The goal is to demonstrate **clean data flow**, **single source of truth**, and **two-way consistency** between student/course enrollments.

## 2) How to Run 
```bash
python main.py

