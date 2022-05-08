class Word:

    def __init__(self, file: str):
        self.file = file

    def word_search_in_for(self) -> None:
        """Метод пропуска по слову и остоновки по ключивому слову используя цикл FOR"""
        with open(self.file, 'r', encoding='UTF-8') as file:
            for word in file:
                if word.strip() in 'Привет':
                    continue
                elif word.strip() in 'Пока':
                    continue
                elif word.strip() in 'Яблоко':
                    break
                else:
                    print(word)
            else:
                print('Cлово не найдено')

    def word_search_in_while(self) -> None:
        """Метод пропуска по слову и остоновки по ключивому слову используя цикл WHILE"""
        with open(self.file, 'r', encoding='UTF-8') as file:
            while word := file.readline():
                word = word.strip()
                if 'Привет' in word:
                    continue
                elif 'Пока' in word:
                    continue
                elif 'Яблоко' in word:
                    break
                else:
                    print(word)
            else:
                print('Слово не найдено')


filename = Word(input())
filename.word_search_in_for()
filename.word_search_in_while()
g