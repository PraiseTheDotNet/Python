import random


if __name__ == '__main__':
    a = 100
    n = 20
    input = [random.randrange(0, a) for i in range(n)]
    print('Исходная последовательность:', input)
    first = [i for i in input if (i > a / 6) and (i < 5 * a / 6)]
    input = [x for x in input if x not in first]
    print('После удаления:', input)
    print('Удаленные элементы:', first)
