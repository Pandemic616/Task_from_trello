from collections import Counter


class WordsCount:

    def __init__(self, x: str):
        self.x = x

    def counting(self) -> dict[str, int]:
        """Функция подсчета слов и символв в файле"""
        with open(self.x, 'r', encoding='UTF-8') as file:
            return dict(Counter(file.read().split()))


filename = WordsCount(input())
print(filename.counting())
