import numpy as np


if __name__ == '__main__':
    arr = np.array([[9, 2, 0, 4, 5],
                   [1, 2, 0, 6, 5],
                   [1, 2, 6, 4, 5],
                   [1, 2, 3, 4, 49]])
    cnt = np.count_nonzero(np.count_nonzero(arr == 0, axis=1) == 0)
    print('Количество строк с ненулевыми элементами: ', cnt)
    unique, counts = np.unique(arr, return_counts=True)
    elem: int
    cnt_2: int = 0
    for x in range(len(unique)):
        if (cnt_2 != 0 and unique[x] > elem and counts[x] > 1) or (cnt_2 == 0 and counts[x] > 1):
            cnt_2 = counts[x]
            elem = unique[x]
    print('Максимальный элемент:', elem, 'встречается ', cnt_2, 'раз')
