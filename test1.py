from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """ Вычисляет квадратный корень. """

    return sqrt(number)


def calc(your_number: float) -> str:
    """ Проверяет что переменная меньше 0. """

    if your_number >= 0:
        res = calculate_square_root(your_number)
        return print(f'Мы вычислили квадратный корень из введённого '
                     f'вами числа. Это будет: {res}')


calc(25.5)
