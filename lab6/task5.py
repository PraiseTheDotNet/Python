import matplotlib.pyplot as plt
import numpy as np


def print_menu(title: str, data: list) -> str:
    print(title)
    for x in range(len(data)):
        print('{0}) {1}'.format(x, data[x]))
    res = -1

    while res == -1:
        print('Введите номер:')
        text = input()
        try:
            res = int(text)
            if res < 0 or res >= len(data):
                raise ValueError()
        except:
            print('Неверное значение, повторите ввод')
            res = -1
    print('Выбрано:', data[res])
    return data[res]


if __name__ == '__main__':
    colors = ['red', 'green', 'blue', 'black', 'yellow', 'gray']
    widths = [2, 4, 6, 8, 10, 12, 14]
    lines = ['-', '--', '-.', ':']
    color = print_menu('Выберите цвет', colors)
    width = print_menu('Выберите толщину', widths)
    line = print_menu('Выберите тип линии', lines)
    x = np.linspace(0, 100, 100)
    plt.plot(x, np.sqrt(x), color=color, linestyle=line, linewidth=width)
    plt.show()
