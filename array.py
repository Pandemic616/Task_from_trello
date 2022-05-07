array = [0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9, 10, 11, 12, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]


def remove_duplicates(x: list[int]) -> list[int]:
    """Функция удаления дубликатов в списке без изменения порядка"""
    temp = []
    for i in x:
        if i not in temp:
            temp.append(i)
    return temp


print(remove_duplicates(array))
