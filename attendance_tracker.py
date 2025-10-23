def calculate_attendance_percentage(classes_held, classes_attended):
    if classes_held == 0:
        return 0
    return (classes_attended / classes_held) * 100

if __name__ == "__main__":
    classes_held = int(input("Enter total classes held: "))
    classes_attended = int(input("Enter classes attended: "))
    
    attendance = calculate_attendance_percentage(classes_held, classes_attended)
    
    print(f"Classes Held: {classes_held}")
    print(f"Classes Attended: {classes_attended}")
    print(f"Attendance: {attendance:.0f}%")
