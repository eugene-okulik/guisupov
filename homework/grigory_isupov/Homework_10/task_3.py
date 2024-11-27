def operation_decorator(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '/':
        result = first / second
    elif operation == '*':
        result = first * second

    return result


first = int(input('Введи первое число : '))
second = int(input('Введи второе число : '))
print(calc(first, second))


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# Вариант 1 пока с магией прям по уроку
new_price_list = PRICE_LIST.split()

product = new_price_list[0::2]
price = new_price_list[1::2]
print(dict(zip(product, price)))

# Вариант 2 но как понимаю очень редко такое будет встречаться
new_price_list_1 = {item.split()[0]: item.split()[1] for item in PRICE_LIST.splitlines()}

print(new_price_list_1)

# # Вариант 3 самый не красивый но понятный))
new_price = PRICE_LIST.split()
new_price_list_3 = {new_price[i]: new_price[i + 1] for i in range(0, len(new_price), 2)}

print(new_price_list_3)

# Вариант 4 практически то же самое что и второй вариант
new_price_list_4 = {item.split()[0]: item.split()[1] for item in PRICE_LIST.split('\n')}

print(new_price_list_4)
