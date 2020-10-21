import numpy as np


def fill_array_first(my_array, arr_width, arr_height):
    trigger = True
    limit = False
    i = 0
    x = 0
    y = 0
    max_value = 0
    while i < arr_width * arr_height:
        i += 1
        my_array[(arr_height - 1 if y >= arr_height else y), (arr_width - 1 if x >= arr_width else x)] = i
        if (not limit and (x == 0 and y == max_value and trigger or x == max_value and y == 0 and not trigger)
                or limit and (trigger and y == arr_height - 1 or not trigger and x == arr_width - 1)):
            trigger = not trigger
            max_value += 1
            if max_value == arr_width or max_value == arr_height:
                limit = True
            if not limit:
                if trigger:
                    x = max_value
                else:
                    y = max_value
            else:
                if not trigger:
                    if y < arr_height - 1:
                        y += 1
                    else:
                        x += 1
                elif x < arr_width - 1:
                    x += 1
                else:
                    y += 1

        else:
            if trigger:
                x -= 1
                y += 1
            else:
                x += 1
                y -= 1
            if x < 0 or y < 0:
                if x < 0:
                    x += 1
                else:
                    y += 1
                trigger = not trigger


def fill_array_second(array, width, height):
    i = 0
    x = 0
    y = 0
    s_x = 0
    f_x = width - 1
    s_y = 0
    f_y = height - 1
    horizontal = True
    revesed = False
    while i < width * height:
        i += 1
        array[y, x] = i
        # по горизонтали и в обратном порядке
        if horizontal and revesed:
            if x - 1 >= s_x:
                x -= 1
            else:
                f_y -= 1
                horizontal = False
                y -= 1
        # по горизонтали и в прямом порядке
        elif horizontal and not revesed:
            if x + 1 <= f_x:
                x += 1
            else:
                s_y += 1
                y += 1
                horizontal = False
        elif not horizontal and revesed:
            if y - 1 >= s_y:
                y -= 1
            else:
                s_x += 1
                horizontal = True
                revesed = False
                x += 1
        else:
            if y + 1 <= f_y:
                y += 1
            else:
                f_x -= 1
                x -= 1
                revesed = True
                horizontal = True





if __name__ == '__main__':
    print('Введите ширину:')
    width = int(input())
    print('Введите высоту:')
    height = int(input())
    arr = np.zeros((height, width), dtype=np.int32)
    print('Введите способ:')
    fill_mode = int(input())
    if fill_mode == 1:
        fill_array_first(arr, width, height)
    else:
        fill_array_second(arr, width, height)
    file_path = 'D:\\dev\\Maga\\Python\\lab5\\files\\task6\\output.txt'
    np.savetxt(file_path, arr, fmt='%d', delimiter='\t')
