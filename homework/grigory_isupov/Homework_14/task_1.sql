
-- 1 Создаю студента (student)
insert into students (name, second_name) VALUES ('Ostap', 'Bender')

Python Testing with pytest
-- 2 Создаю несколько книг (books) и указываю, что  созданный студент взял их

INSERT INTO books (title, taken_by_student_id) VALUES ('Python Testing','3793'), ('Testing','3793')


-- 3 Создаю группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) VALUES ('The best', 'november 2024', 'january 2025')

UPDATE students SET group_id = 2408 WHERE id = 3793

-- 4 Создаю несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Alchemy'), ('Magiс')


-- 5 Создаю по два занятия для каждого предмета (lessons)

INSERT INTO lessons (title, subject_id)
VALUES ('lesson_magic_1', 3711 ), ('lesson_magic_2', 3711 ), ('lesson_alchemy_1', 3710), ('lesson_alchemy_2', 3710)


-- 6 Ставлю своему студенту оценки (marks) для всех созданных вами занятий

INSERT INTO marks (value, lesson_id, student_id)
VALUES ( 5, 7232 , 3793), ( 3, 7233 , 3793), ( 4, 7234 , 3793), ( 6, 7235 , 3793)



/*
Получаю всю информацию из базы данных:
 */

-- 1 Все оценки студента

SELECT value as 'оценки', lesson_id as 'предмет'
FROM marks m WHERE student_id  = 3793

-- 2 Все книги, которые находятся у студента

SELECT * FROM  books b WHERE taken_by_student_id = 3793


-- 3 Вся информация по студенту


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
WHERE students.id = 3793