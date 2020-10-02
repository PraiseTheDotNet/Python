import random

if __name__ == '__main__':
    input = [i for i in range(20)]
    random.shuffle(input)
    print('Исходный массив:', input)
    data = []
    start = 0
    for i in range(1, len(input) + 1):
        if i == len(input) or input[i] < input[i - 1]:
            part = input[start:i]
            if len(data) != 0:
                if len(data[0]) < len(part):
                    data.clear()
                    data.append(part)
                elif len(data[0]) == len(part):
                    data.append(part)
            else:
                data.append(part)
            start = i

    max_length = len(data[0])
    print('Максимальная длина последовательности:', max_length)
    print('Последовательност(ь|и):', data)
