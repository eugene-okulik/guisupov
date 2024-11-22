data_1 = "результат операции: 42"
data_2 = "результат операции: 514"
data_3 = "результат работы программы: 9"
data_4 = "результат: 2"


def result(var):
    return int(var.split()[-1]) + 10


print(result(data_1), '\n', result(data_2), '\n', result(data_3), '\n', result(data_4), '\n', sep='')
