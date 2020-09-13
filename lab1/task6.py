

def get_fibonacci(a: int):
    if a <= 0:
        return []
    elif a == 1:
        return [0]
    res = [0, 1]
    for x in range(a - 2):
        fib = res[-1] + res[-2]
        res.append(fib)
    return res


if __name__ == "__main__":
    print('Введите a')
    a = int(input())
    print(get_fibonacci(a))
