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
        time = lesson.get("start_time", "")
        room = lesson.get("room", "")
        teacher_name = "Unknown"
        for t in manager.teachers:
            if t.user_id == course.teacher_id:
                teacher_name = t.name
                break
        print(f"{time:<8} {room:<6} {course.name:<20} {teacher_name:<12}")


def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1) Show daily roster")
        print("2) Check in")
        print("3) Switch course")
        print("q) Quit")
        # Create a menu for the new PST3 functions.
        # Get user input and call the appropriate view function, passing 'manager' to it.
        choice = input("Enter choice: ").strip().lower()
        if choice == '1':
            day = input("Enter day (e.g., Monday): ").strip()
            front_desk_daily_roster(manager, day)
        elif choice == "2":
            s_id = input("Student id: ").strip()
            c_id = input("Course id: ").strip()
            if not (s_id.isdigit() and c_id.isdigit()):
                print("Please enter numeric ids.")
                continue
            manager.check_in(int(s_id), int(c_id))
        elif choice == '3': 
            s_id    = input("Student id: ").strip()
            from_id = input("From course id: ").strip()
            to_id   = input("To course id: ").strip()
            if not (s_id.isdigit() and from_id.isdigit() and to_id.isdigit()):
                print("Please enter numeric ids.")
            else:
                manager.switch_course(int(s_id), int(from_id), int(to_id))
        elif choice.lower() == 'q':
            break
        else:
            print("invalid choice, please try again.")
if __name__ == "__main__":
    main()