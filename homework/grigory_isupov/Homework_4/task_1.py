my_dict = dict()
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = ['Иван', 'Петр', 'Семен', 'Олег', 'Стас']
my_dict['dict'] = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'}
my_dict['set'] = {'a', 'b', 'c', 'd', 'e'}

# вывожу на экран последний элемент 'tuple'
print(my_dict['tuple'][-1])

# элементу с ключом 'list' добавляю в конец списка еще один элемент и удаляю второй элемент
my_dict['list'].append("Александр")
my_dict['list'].pop(1)

# элементу с ключем 'dict' добавляю элемент с ключем ('i am a tuple',) и значением 'six'
my_dict['dict'][('i am a tuple',)] = 'six'


# элементу с ключем 'set' добавляю новый элемент и удаляю элемент 'а'
my_dict['set'].add('f')
my_dict['set'].remove('a')


print(my_dict)
