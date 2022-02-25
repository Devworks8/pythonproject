lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [00.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students_list = [lloyd, alice, tyler]


def main():
    print_student_data(students_list)
    print(get_average(lloyd))
    print("\n{0}".format(get_class_average(students_list)))
    print("\n{0}".format(get_letter_grade(get_class_average(students_list))))


def print_student_data(students):
    for student in students:
        print("Student Name: {0}\n"
              "Homework: {1}\n"
              "Quizzes: {2}\n"
              "Tests: {3}\n".format(student["name"],
                                  student["homework"],
                                  student["quizzes"],
                                  student["tests"]))


def average(numbers):
    return float(sum(numbers)) / len(numbers)


def get_average(student):
    homework = average(student["homework"]) * 0.1
    quiz = average(student["quizzes"]) * 0.3
    test = average(student["tests"]) * 0.6

    return homework + quiz + test


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "D"


def get_class_average(students):
    results = []

    for student in students:
        results.append(get_average(student))

    return average(results)


if __name__ == "__main__":
    main()
