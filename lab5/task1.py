import numpy as np


if __name__ == '__main__':
    print('Введите n')
    n = int(input())
    a = np.random.uniform(-10, 10, n)
    print(a)
    min = np.min(a)
    max = np.max(a)
    print('Минимум:', min)
    print('Максимум:', max)
    y = np.random.uniform(min, max)
    print('Y:', y)
    res = a[np.where(np.abs(a) > np.abs(y))]
    print('Числа, большие по модулю модуля y:', res)
    print('Произведение чисел:', np.prod(res))
    others = np.setdiff1d(a, res)
    print('Оставшиеся числа:', others)
    print('Сумма модуля чисел:', np.sum(np.abs(others)))

