import numpy as np


def remove_min(arr):
    min = np.min(arr)
    i = 0
    while i < arr.shape[0]:  # кол-во строк
        j = 0
        while j < arr.shape[1]:  # кол-во столбцов
            if arr[i, j] == min:
                print('(', i, ',', j, ') =', i)
                arr = np.delete(arr, i, 0)  # строка
                arr = np.delete(arr, j, 1)  # столбец
                i -= 1
            else:
                j += 1
        i += 1
    return arr


def sort_array(arr):
    columns = []
    arr = arr.transpose()
    for x in range(arr.shape[0]):
        columns.append(arr[x].min())
    ind = np.array(columns).argsort()
    arr = arr[ind]
    return arr.transpose()


if __name__ == '__main__':
    arr = np.array([[19, 2, 9, 4], [4, 1, 6, 5], [7, 8, 3, 5]])
    print(arr)
    arr = remove_min(arr)
    print(arr)
    arr = sort_array(arr)
    print(arr)
