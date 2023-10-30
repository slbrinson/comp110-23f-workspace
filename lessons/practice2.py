def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Return the students who were in attendance on certain days of the week."""
    if day in attendance_log:
        attendance_log[day] += [student]
    else:
        attendance_log = [student]
    return attendance_log

# Example usage:
attendance_log = {
    'Monday': ['Alice', 'Bob'],
    'Tuesday': ['Charlie', 'David'],
    'Wednesday': ['Eve']
}

update_attendance(attendance_log, 'Monday', 'Frank')
update_attendance(attendance_log, 'Tuesday', 'Grace')

print(attendance_log)