

def get_armstrong_numbers(n: int):
    result = []
    x = 10**(n-1)
    limit = 10**n
    while x < limit:
        sum_of_digits = sum([int(y) ** n for y in str(x)])
        if sum_of_digits == x:
            result.append(x)
        x += 1
    return result


if __name__ == "__main__":
    print(get_armstrong_numbers(3))

