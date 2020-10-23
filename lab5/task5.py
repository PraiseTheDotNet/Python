import sys

import numpy as np


if __name__ == '__main__':
    arr = np.array([
        [2, 1, 2, 1],
        [1, 1, 2, 2],
        [2, 2, 1, 1],
        [1, 2, 1, 2]
    ])
    ver = np.sum(arr, axis=0)
    if not np.all(ver == ver[0]):
        print('Не логический квадрад')
        sys.exit()
    hor = np.sum(arr, axis=1)
    if not np.all(hor == hor[0]):
        print('Не логический квадрад')
        sys.exit()
    if not np.array_equal(ver, hor):
        print('Не логический квадрад')
        sys.exit()
    diag_1 = np.sum(arr.diagonal())
    if diag_1 != ver[0]:
        print('Не логический квадрад')
        sys.exit()
    diad_2 = np.sum(np.fliplr(arr).diagonal())
    if diad_2 != ver[0]:
        print('Не логический квадрад')
        sys.exit()
    print('Логический квадрад')

