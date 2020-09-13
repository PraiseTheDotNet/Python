# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def swipe_1(a: int, b: int):
    c = a
    a = b
    b = c
    print('Первый способ', a, b)

def swipe_2(a: int, b: int):
    a, b = b, a
    print('Второй способ', a, b)

def swipe_3(a: int, b: int):
    a = a + b
    b = a - b
    a = a - b
    print('Третий способ', a, b)

def swipe_4(a: int, b: int):
    a = a - b
    b = a + b
    a = -a + b
    print('Четвертый способ', a, b)

def swipe_5(a: int, b: int):
    a = a ^ b
    b = b ^ a
    a = a ^ b
    print('Пятый способ', a, b)

def task_1():
    print('Введите a')
    a : int
    b: int
    a = int(input())
    print('Введите b')
    b = int(input())
    swipe_1(a, b)
    swipe_2(a, b)
    swipe_3(a, b)
    swipe_4(a, b)
    swipe_5(a, b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/