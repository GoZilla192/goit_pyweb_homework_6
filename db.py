import sqlite3

from constants import DATABASE_NAME


def initialize_db():
    create_groups_sql = """
        CREATE TABLE IF NOT EXISTS "groups" (
            "id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    """
    create_students_sql = """
        CREATE TABLE IF NOT EXISTS "students" (
            "id"	INTEGER NOT NULL UNIQUE,
            "group_id"	INTEGER,
            "first_name"	TEXT,
            "last_name"	TEXT,
            "age"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT),
            CONSTRAINT "fk_students_groups_id" 
                FOREIGN KEY("group_id") REFERENCES "groups"("id")
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );
    """
    create_professors_sql = """
        CREATE TABLE IF NOT EXISTS "professors" (
            "id"	INTEGER NOT NULL UNIQUE,
            "first_name"	TEXT,
            "last_name"	TEXT,
            "age"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    """
    create_subjects_sql = """
        CREATE TABLE IF NOT EXISTS "subjects" (
            "id"	INTEGER NOT NULL UNIQUE,
            "professor_id"	INTEGER,
            "name"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT),
            CONSTRAINT "fk_subjects_professors_id" 
                FOREIGN KEY("professor_id") REFERENCES "professors"("id")
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );
    """
    create_grades_sql = """
        CREATE TABLE IF NOT EXISTS "grades" (
            "id"	INTEGER NOT NULL UNIQUE,
            "student_id"	INTEGER,
            "grade"	INTEGER,
            "subject_id"	INTEGER,
            "received_date"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT),
            CONSTRAINT "fk_grades_students_id" 
                FOREIGN KEY("student_id") REFERENCES "students"("id")
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            CONSTRAINT "fk_grades_subjects_id" 
                FOREIGN KEY("subject_id") REFERENCES "subjects"("id")
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );
    """

    tables_sql = [
        create_groups_sql,
        create_students_sql,
        create_professors_sql,
        create_subjects_sql,
        create_grades_sql,
    ]

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        for table_sql in tables_sql:
            cursor.execute(table_sql)
            conn.commit()



def insert_data(table: str, columns: list[str], data_for_insert: list[tuple]):
    sql_query = f"INSERT INTO {table}({','.join(columns)}) VALUES (?"
    sql_query += ",?" * (len(data_for_insert[0]) - 1)
    sql_query += ")"

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.executemany(sql_query, data_for_insert)
        conn.commit()


initialize_db()
