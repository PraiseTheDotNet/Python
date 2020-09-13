

if __name__ == "__main__":
    print('Введите трёхзначное число')
    x = input()
    res = sum([int(i) for i in x])
    print(res)