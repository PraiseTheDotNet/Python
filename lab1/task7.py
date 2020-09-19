from itertools import permutations

def get_if_correct(a, b, c, number):
    val = a * 100 + b * 10 + c
    if val > 100 and val != number:
        return val

if __name__ == "__main__":
    print('Введите трёхзначное число')
    number = int(input())
    a = number % 10
    b = number // 10 % 10
    c = number // 100

    num_1 = get_if_correct(a, b, c, number)
    num_2 = get_if_correct(a, c, b, number)
    num_3 = get_if_correct(b, a, c, number)
    num_4 = get_if_correct(b, c, a, number)
    num_5 = get_if_correct(c, a, b, number)
    num_6 = get_if_correct(c, b, a, number)

    if num_1:
        print(num_1)
    if num_2 and num_2 != num_1:
        print(num_2)
    if num_3 and num_3 != num_2 and num_3 != num_1:
        print(num_3)
    if num_4 and num_4 != num_3 and num_4 != num_2 and num_4 != num_1:
        print(num_4)
    if num_5 and num_5 != num_4 and num_5 != num_3 and num_5 != num_2 and num_5 != num_1:
        print(num_5)
    if num_6 and num_6 != num_5 and num_6 != num_4 and num_6 != num_3 and num_6 != num_2 and num_6 != num_1:
        print(num_6)