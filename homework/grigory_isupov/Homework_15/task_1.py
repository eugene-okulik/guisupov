import mysql.connector as mysql
import random

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
# 1. Cоздаю студента
cursor = db.cursor(dictionary=True)
create_students = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = ('Mars', 'Laky')
cursor.execute(create_students, values)

student_id = cursor.lastrowid
print(f"Cоздан студент с id: {student_id}")

db.commit()

#  Создаю несколько книг (books) и указываю, что  созданный студент взял их
books = [("Python Testing", student_id), ("Advanced SQL", student_id)]

create_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(create_books, books)
db.commit()

# 3. Добавляю группу
group_title = "The best off the best"
group_start_date = "2024-12-01"
group_end_date = "2025-02-28"

create_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
cursor.execute(create_group, (group_title, group_start_date, group_end_date))
group_id = cursor.lastrowid
print(f"Создана группа с id: {group_id}")
db.commit()

# 4. Обновляю данные по студенту, добавляю его в группу
student_update_group = 'UPDATE students SET group_id = %s WHERE id = %s'
cursor.execute(student_update_group, (group_id, student_id))
print(f"Студент с id {student_id}, добавлен в группу с id {group_id}")
db.commit()

# 4. Добавляю предметы
subjects = ["Astronomy", "Geology"]
create_subjects = 'INSERT INTO subjets (title) VALUES (%s)'
subject_ids = []

for subject in subjects:
    cursor.execute(create_subjects, (subject,))
    subject_ids.append(cursor.lastrowid)

astronomy_id, geology_id = subject_ids
print(f"id предметов: Astronomy - {astronomy_id}, Geology - {geology_id}")
db.commit()

# 5. Добавляю занятия
lessons = [
    ("lesson_astronomy_1", astronomy_id),
    ("lesson_astronomy_2", astronomy_id),
    ("lesson_geology_1", geology_id),
    ("lesson_geology_2", geology_id)
]

create_lessons = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
lesson_ids = []

for lesson in lessons:
    cursor.execute(create_lessons, lesson)
    lesson_ids.append(cursor.lastrowid)

lesson_astronomy_1_id, lesson_astronomy_2_id, lesson_geology_1_id, lesson_geology_2_id = lesson_ids
print(f"ID занятий: Astronomy 1 = {lesson_astronomy_1_id}, Astronomy 2 = {lesson_astronomy_2_id}, "
      f"Geology 1 = {lesson_geology_1_id}, Geology 2 = {lesson_geology_2_id}")
db.commit()

# 6. Проставляю оценки
marks = [
    (random.randint(1, 5), lesson_astronomy_1_id, student_id),
    (random.randint(1, 5), lesson_astronomy_2_id, student_id),
    (random.randint(1, 5), lesson_geology_1_id, student_id),
    (random.randint(1, 5), lesson_geology_2_id, student_id)
]

create_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.executemany(create_marks, marks)

db.commit()

# Получаею все оценки студента
cursor.execute(
    """
    SELECT value AS 'оценки', lesson_id AS 'предмет' 
    FROM marks WHERE student_id = %s
       """, (student_id,)
)
print("Все оценки студента:")
for row in cursor.fetchall():
    print(row)

# Получаею все книги, которые находятся у студента
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print("\nВсе книги студента:")
for row in cursor.fetchall():
    print(row)

# Получаю всю информацию по студенту
cursor.execute(
    """
    SELECT 
        students.id AS 'id студента',
        students.name AS 'имя студента',
        students.second_name AS 'фамилия студента',
        `groups`.title AS 'название группы',
        books.title AS 'название книг',
        marks.value AS 'оценки',
        lessons.title AS 'занятия',
        subjets.title AS 'предмет'
    FROM students
    LEFT JOIN `groups` ON students.group_id = `groups`.id
    LEFT JOIN books ON books.taken_by_student_id = students.id
    LEFT JOIN marks ON marks.student_id = students.id
    LEFT JOIN lessons ON marks.lesson_id = lessons.id
    LEFT JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.id = %s
    """,
    (student_id,)
)
print("\nВся информация по студенту:")
for row in cursor.fetchall():
    print(row)

db.close()
