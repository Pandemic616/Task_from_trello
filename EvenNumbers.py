def For(a: int):
    """Функция вывода четных чисел реализованная через For"""
    for i in range(a):
        if i % 2 == 0:
            print(i)


def While(a: int):
    """Функция вывода четных чисел реализовання через While"""
    i = 0
    while i < a:
        if i % 2 == 0:
            print(i)
        i += 2


For(int(input()))
While(int(input()))
