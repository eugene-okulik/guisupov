data_1 = "результат операции: 42"
data_2 = "результат операции: 514"
data_3 = "результат работы программы: 9"

num_1 = int(data_1[data_1.index(":") + 1:].strip()) + 10
num_2 = int(data_2[data_2.index(":") + 1:].strip()) + 10
num_3 = int(data_3[data_3.index(":") + 1:].strip()) + 10

print(num_1)
print(num_2)
print(num_3)
