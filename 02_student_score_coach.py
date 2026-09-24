students = [
    {"name": "Ali", "score": 82},
    {"name": "Sara", "score": 91},
    {"name": "Hamza", "score": 67},
    {"name": "Ayesha", "score": 88}
]


def is_high_score(score):
    return score >= 80


def show_student(student):
    print(f"{student['name']} - {student['score']}")


for student in students:
    if is_high_score(student["score"]):
        show_student(student)