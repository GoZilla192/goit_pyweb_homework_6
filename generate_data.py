import sqlite3
from pathlib import Path
from faker import Faker
from random import randint, shuffle
from datetime import datetime


from constants import *
from db import insert_data


faker = Faker("uk-UA")


def generate_groups():
    # TODO: не должны повторятся
    possible_groups_name = ["IPZ-23-11", "IPZ-22-9", "PM-23-9", "M-23-9", "AT-23-11"]
    shuffle(possible_groups_name)

    data_for_insert = []

    for i in range(GROUP_COUNT):
        data_for_insert.append((possible_groups_name[i],))

    return data_for_insert


def generate_students():
    data_for_insert = []

    for _ in range(STUDENTS_COUNT):
        data_for_insert.append(
            (randint(1, GROUP_COUNT), faker.first_name(), faker.last_name(), randint(18, 40))
        )

    return data_for_insert


def generate_professors():
    data_for_insert = []

    for _ in range(PROFESSORS_COUNT):
        data_for_insert.append((faker.first_name(), faker.last_name(), randint(18, 80)))

    return data_for_insert


def generate_subjects():
    possible_subjects = [
        "Математика",
        "Алгебра",
        "Геометрія",
        "Інформатика",
        "Фізика",
        "Хімія",
        "Біологія",
        "Історія",
    ]
    shuffle(possible_subjects)

    data_for_insert = []

    for i in range(SUBJECTS_COUNT):
        data_for_insert.append(
            (
                randint(1, PROFESSORS_COUNT),
                possible_subjects[i],
            )
        )

    return data_for_insert


def generate_grades():
    diapazon_grades = [0, 100]
    data_for_insert = []

    for student_id in range(1, STUDENTS_COUNT + 1):
        for subject_id in range(1, SUBJECTS_COUNT + 1):
            for _ in range(GRADES_COUNT):
                data_for_insert.append(
                    (
                        student_id,
                        randint(*diapazon_grades),
                        subject_id,
                        faker.date_this_year(),
                    )
                )

    return data_for_insert


def main():
    groups = generate_groups()
    students = generate_students()
    professors = generate_professors()
    subjects = generate_subjects()
    grades = generate_grades()

    insert_data("groups", ["name"], groups)
    insert_data("students", ["group_id", "first_name", "last_name", "age"], students)
    insert_data("professors", ["first_name", "last_name", "age"], professors)
    insert_data("subjects", ["professor_id", "name"], subjects)
    insert_data("grades", ["student_id", "grade", "subject_id", "received_date"], grades)


if __name__ == "__main__":
    main()
