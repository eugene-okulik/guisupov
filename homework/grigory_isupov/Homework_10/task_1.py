import random


def my_first_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print("finished")
        return result

    return wrapper


@my_first_decorator
def check_even(x):
    if x % 5 == 0:
        print("Четное")
    else:
        print("Не четное")


check_even(random.randint(1, 100))
