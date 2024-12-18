import os
from datetime import datetime, timedelta

# Получаю путь к директории
base_path = os.path.dirname(__file__)

# Получаю путь до папки homework
home_work_path = os.path.dirname(os.path.dirname(base_path))

# Получаю путь к файлу, с данными
hw_13_path = os.path.join(home_work_path, "eugene_okulik", "hw_13", "data.txt")

with open(hw_13_path, encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    # Разделяю строку на номер, дату и текст
    parts = line.replace('. ', ' - ').split(' - ')
    # print(parts)
    number, date_str, action = parts[0], parts[1], parts[2]

    # Преобразую строку в формат даты
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    # Обрабатываем каждую строку в зависимости от действия
    if "на неделю позже" in action:
        new_date = date + timedelta(weeks=1)
        print(f"{number}. {new_date}")
    elif "какой это будет день недели" in action:
        weekday = date.strftime('%A')  # Название дня недели
        print(f"{number}. {weekday}")
    elif "сколько дней назад была эта дата" in action:
        now = datetime.now()
        delta = now - date
        print(f"{number}. {delta.days} дней назад")
