courses = [
    {"name": "Python", "score": 88},
    {"name": "Git", "score": 92},
    {"name": "Math", "score": 74},
    {"name": "SQL", "score": 81}
]


def is_strong(score):
    return score >= 80


def show_course(course):
    print(f"{course['name']} - {course['score']}")


def average_score(courses):
    total = 0

    for course in courses:
        total += course["score"]

    return total / len(courses)


print("Strong courses:")

for course in courses:
    if is_strong(course["score"]):
        show_course(course)

average = average_score(courses)

print(f"Average score: {average}")