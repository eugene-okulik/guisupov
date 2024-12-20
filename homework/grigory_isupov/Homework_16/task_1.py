import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
# Формирую путь к файлу
base_path = os.path.dirname(__file__)
home_work_path = os.path.dirname(os.path.dirname(base_path))
csv_file_path = os.path.join(home_work_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

missing_data = []  # Создаю список, в который буду ложить строки, не совпадающие с БД
line_number = 1  # Для удобства реализую счетчик строк

with open(csv_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    headers = next(file_data)  # Пропускаю первую строку

    cursor = db.cursor(dictionary=True)

    for row in file_data:
        line_number += 1
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

        # Формирую запрос по полному совпадению
        query = """
                SELECT 
                    students.name AS 'имя студента',
                    students.second_name AS 'фамилия студента',
                    `groups`.title AS 'название группы',
                    books.title AS 'название книг',
                    subjets.title AS 'предмет',
                    lessons.title AS 'занятия',
                    marks.value AS 'оценки'
                FROM students
                LEFT JOIN `groups` ON students.group_id = `groups`.id
                LEFT JOIN books ON books.taken_by_student_id = students.id
                LEFT JOIN marks ON marks.student_id = students.id
                LEFT JOIN lessons ON marks.lesson_id = lessons.id
                LEFT JOIN subjets ON lessons.subject_id = subjets.id
                WHERE students.name = %s 
                  AND students.second_name = %s
                  AND `groups`.title = %s
                  AND books.title = %s
                  AND subjets.title = %s
                  AND lessons.title = %s
                  AND marks.value = %s
            """

        cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
        result = cursor.fetchone()

        # Проверяю результат
        if result is None:
            missing_data.append((line_number, row))  # Сохраняю в список номер строки и данные

# Вывожу на печать результат
if missing_data:
    print("\nПо этим строкам в файле нет полного совпадения с БД:")
    for line_num, data in missing_data:
        print(f"Строка {line_num}: {', '.join(data)}")
else:
    print("Все строки в файле есть в БД")

db.close()
