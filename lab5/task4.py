import numpy as np


if __name__ == '__main__':
    file_path = 'D:\\dev\\Maga\\Python\\lab5\\files\\task4\\input.txt'
    arr = np.loadtxt(file_path)
    count:int = 0
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            all = True
            for k in range(max(0, y - 1), min(arr.shape[0], y + 2)):
                if not all:
                    break
                for l in range(max(0, x - 1), min(arr.shape[1], x + 2)):
                    if not(y == k and l == x):
                        all = arr[y, x] < arr[k, l]
                        if not all:
                            break
            if all:
                count = count + 1
                print('({0}, {1}) = {2}'.format(x, y, arr[y, x]))
    print('Количество локальных минимумов:', count)

