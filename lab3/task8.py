import random

def find_1(data):
    return (set([x for x in range(len(data) + 1)]) - set(data)).pop()

def find_2(data):
    for x in range(len(data) + 1):
        if x not in data:
            return x
    return []

if __name__ == '__main__':
    n = 10
    input = random.sample(range(0, n + 1), n + 1)[:n]
    print(input)
    print('Элемент:', find_1(input))
    print('Элемент:', find_2(input))