def get_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"


def process_students(students):
    highest_name, highest_avg = None, 0
    lowest_name, lowest_avg = None, 0

    for student in students:
        # manual sum and count (no sum())
        total = 0
        count = 0
        for score in student["scores"]:
            total += score
            count += 1

        avg = total / count if count > 0 else 0.0
        grade = get_grade(avg)
        print(f"{student['name']} → Average: {avg:.2f} → Grade: {grade}")

        # track running highest / lowest (no max()/min())
        if highest_name is None or avg > highest_avg:
            highest_name, highest_avg = student["name"], avg
        if lowest_name is None or avg < lowest_avg:
            lowest_name, lowest_avg = student["name"], avg

    if highest_name is not None:
        print(f"Highest: {highest_name} ({highest_avg:.2f})")
        print(f"Lowest: {lowest_name} ({lowest_avg:.2f})")


students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},
]
process_students(students)