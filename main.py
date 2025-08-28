# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    #  Call a method on the manager to get the day's lessons and print them.
    items = manager.get_lessons_by_day(day)
    if not items:
        print("(No lessons)")
        return 
    print(f"{'Time':<8} {'Room':<6} {'Course':<20} {'Teacher':<12}")
    print("-" * 60)
    for course, lesson in items:
        time = lesson.get("time", "")
        room = lesson.get("room", "")
        teacher_name = "Unknown"
        for t in manager.teachers:
            if t.user_id == course.teacher_id:
                teacher_name = t.name
                break
        print(f"{time:<8} {room:<6} {course.name:<20} {teacher_name:<12}")

def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    pass

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        # TODO: Create a menu for the new PST3 functions.
        # Get user input and call the appropriate view function, passing 'manager' to it.
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice.lower() == 'q':
            break
        
if __name__ == "__main__":
    main()