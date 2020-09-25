import random

if __name__ == '__main__':
    input = [i for i in range(20)]
    random.shuffle(input)
    print('Исходный массив:', input)
    data = []
    start = 0
    for i in range(1, len(input)):
        if input[i] < input[i - 1]:
            part = input[start:i]
            data.append(part)
            start = i
    data.append(input[start:])
    print('Последовательности:', data)
    data.sort(key=len, reverse=True)
    max_length = len(max(data, key=len))
    max_sequence = [x for x in data if len(x) == max_length]
    print('Максимальная длина последовательности:', max_length)
    print('Последовательност(ь|и):', max_sequence)
