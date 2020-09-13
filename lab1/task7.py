from itertools import permutations


if __name__ == "__main__":
    print('Введите трёхзначное число')
    number = input()
    numbers = set([x for x in [int(''.join(p)) for p in permutations(number)] if x >= 100])
    print(numbers)