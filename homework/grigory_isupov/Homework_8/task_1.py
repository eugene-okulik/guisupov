import random


def random_bonus_salary(salary):
    bonus = [True, False]

    random_bonus = random.choice(bonus)
    if random_bonus:
        print(f"{salary}, {random_bonus} - '${salary + random.randint(1, 2000)}'")
    else:
        print(f"{salary}, {random_bonus} - '${salary}'")


random_bonus_salary(salary=int(input("Введи число : ")))
