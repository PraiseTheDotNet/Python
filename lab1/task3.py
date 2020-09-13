import math


def func(x: float):
    if x > 0:
        return math.sqrt(4 * x)
    elif x == 0:
        return math.e
    else:
        return math.fabs(x)


if __name__ == "__main__":
    print('Введите x')
    x = float(input())
    print(func(x))
