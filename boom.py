class Boom:

    def __new__(cls, *args, **kwargs):
        numbers = args[0]
        if not all(num.isdigit() for num in numbers):
            raise ValueError
        return object.__new__(cls)

    def __init__(self, numbers: list[str]):
        self.numbers = numbers

    def do(self) -> str:
        for countdown in self.numbers:
            if countdown == '7':
                return 'BOOOOM'
        else:
            return 'there is no 7 in the list'


boom = Boom(list(input()))
print(boom.do())
