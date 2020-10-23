import time


def collatz(n: int):
    res = n
    max_value = n
    iter = 0
    while res != 1:
        if res % 2 == 0:
            res /= 2
        else:
            res = 3 * res + 1
        iter += 1
        max_value = max(res, max_value)
    return (iter, max_value)


def collatz_with_exceptions(n: int):
    try:
        return collatz(n)
    except:
        print('Произошла ошибка')


if __name__ == '__main__':
    number = ''
    while not len(number):
        print('Введите число')
        number = input()
        if not number.isdigit() or int(number) < 2:
            number = ''
            print('Вы ввели неверное значение!')
    n = int(number)

    start_time = time.time()
    (iter, max_value) = collatz(n)
    finish_time = time.time()
    print("Без обработки ошибок: {0} сек.".format(finish_time - start_time))
    print('Число итераций:', iter)
    print('Максимальное число:', max_value)

    start_time = time.time()
    (iter, max_value) = collatz_with_exceptions(n)
    finish_time = time.time()
    print("С обработкой ошибок: {0} сек.".format(finish_time - start_time))
    print('Число итераций:', iter)
    print('Максимальное число:', max_value)
