import numpy as np


if __name__ == '__main__':
    n = np.array([0, 2, 0, 1, 3, 5, 0, 0, 5, 0, 4, 0])
    #print(np.max(n[1:][(n == 0)[:-1]]))
    max_index = -1
    for x in range(len(n)):
        if n[x] == 0 and x + 1 < len(n):
            if max_index == -1:
                max_index = x + 1
            else:
                if n[max_index] < n[x + 1]:
                    max_index = x + 1

    print('Максимальный элемент находится в индексе:', max_index)
    if max_index != -1:
        print(n[max_index])