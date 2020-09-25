

if __name__ == '__main__':
    input = [-1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
    min = -1
    max = -1
    for x in range(len(input)):
        if min == -1 and input[x] >= 0:
            min = x
        elif input[x] < 0:
            max = x
    print(input)
    input[min + 1:max] = sorted(input[min + 1:max])
    print(input)