import math


def get_x(a: float, b: float, c: float):
    if a == 0 and b != 0:
        return [-c / b]
    if a == 0 and b == 0:
        return []
    if a == 0 and b == 0 and c == 0:
        return ['любое число']
    d = b ** 2 - 4 * a * c
    if d < 0:
        return []
    elif d == 0:
        return [-b / (2 * a)]
    else:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        return [x_1, x_2]

if __name__ == "__main__":
    print('Введите a')
    a = float(input())
    print('Введите b')
    b = float(input())
    print('Введите c')
    c = float(input())
    result = get_x(a, b, c)
    if not result:
        print('Нет корней')
    elif len(result) == 1:
        print('X =', result[0])
    else:
        print('X1 =', result[0], 'X2 =', result[1])