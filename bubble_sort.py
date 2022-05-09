import pytest


class Sorter:

    def __init__(self, unsort: list[int]):
        self.unsort = unsort
        self.count = len(self.unsort)

    def bubble_sort_in_for(self) -> list[int]:
        """Метод пузырьковой сортировки через FOR

        :return: отсортированый список
        """
        for i in range(0, self.count - 1):
            for x in range(self.count - 1):
                if self.unsort[x] > self.unsort[x + 1]:
                    self.unsort[x], self.unsort[x + 1] = self.unsort[x + 1], self.unsort[x]
        return self.unsort

    def bubble_sort_in_while(self) -> list[int]:
        """Метод пузырьковой сортировки через WHILE

        :return: отсортированый список
        """
        counter = 0
        while self.count > counter:
            for x in range(self.count - 1):
                if self.unsort[x] > self.unsort[x + 1]:
                    self.unsort[x], self.unsort[x + 1] = self.unsort[x + 1], self.unsort[x]
            counter += 1
        return self.unsort


@pytest.mark.parametrize(
    ('array', '_object', 'result'),
    [
        ([3, 8, 5, 7], Sorter, [3, 5, 7, 8]),
        ([9, 5, 6, 7, 4], Sorter, [4, 5, 6, 7, 9]),
        ([], Sorter, []),
        ([1, 2, 3, 4, 5], Sorter, [1, 2, 3, 4, 5]),
    ]
)
def test_bubble_sort(array: list[int], _object: Sorter, result: list[int]) -> None:
    """Тестирования класса сортировки
    
    :param array: не отсортированый массив
    :param _object: класс Sorter
    :param result: отсортированый массив
    :return: 
    """""
    new_array_for: list[int] = _object(array).bubble_sort_in_for()
    new_array_while: list[int] = _object(array).bubble_sort_in_while()
    assert new_array_for == result
    assert new_array_while == result
