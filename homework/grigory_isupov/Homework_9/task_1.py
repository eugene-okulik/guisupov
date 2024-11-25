import datetime

date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')

print(f'Месяц: {python_date.strftime('%B')}')
print(f'{python_date.strftime('%d.%m.%Y, %H:%M')}')

print(python_date)

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

new_list = list(filter(lambda x: x > 28, temperatures))

print(f'Самая высокая температура: {max(new_list)}')
print(f'Самая низкая температура: {min(new_list)}')
print(f'Средняя температура: {sum(new_list) / len(new_list):.2f}')
