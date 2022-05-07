array_1 = ['a', 'b', 'c']
array_2 = [1, 2, 3]


class Dictionary:

    def __init__(self, x: list[str], y: list[int]):
        self.x = x
        self.y = y

    def creating_a_dictionary(self) -> dict[str, int]:
        """Функция создания словоря из двух массивов"""
        return dict(zip(self.x, self.y))


new_dict = Dictionary(array_1, array_2)
print(new_dict.creating_a_dictionary())
