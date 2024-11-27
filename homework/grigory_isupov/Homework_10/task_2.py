def repeat_me(func):
    def wrapper(*args, count):
        for _ in range(count):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


#Второй вариант
def repeat_me_1(count):
    def decorator(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)

        return wrapper

    return decorator


@repeat_me_1(count=2)
def example_1(text):
    print(text)


example_1('print me')
