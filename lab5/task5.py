import numpy as np


if __name__ == '__main__':
    arr = np.array([
        [2, 1, 2, 1],
        [1, 1, 2, 2],
        [2, 2, 1, 1],
        [1, 2, 1, 2]
    ])
    ver = np.sum(arr, axis=0)
    hor = np.sum(arr, axis=1)
    print(ver)
    print(hor)
    diag_1 = np.sum(arr.diagonal())
    diad_2 = np.sum(np.fliplr(arr).diagonal())
    print(diag_1)
    print(diad_2)
    res = diad_2 == diag_1 and np.all(ver == diag_1) and np.all(hor == diag_1)
    if res:
        print('Логический квадрад')
    else:
        print('Не логический квадрад')
