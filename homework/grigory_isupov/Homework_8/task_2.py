import sys

# Увеличиваю ограничение для преобразования больших чисел в строку
sys.set_int_max_str_digits(100000)


def fibonacci(limit=1000001):
    a, b = 0, 1
    count = 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


count_1 = 1
for number in fibonacci(100001):
    if count_1 == 5 or count_1 == 200 or count_1 == 10000:
        print(number)
    elif count_1 == 100000:
        print(number)
        break
    count_1 += 1
