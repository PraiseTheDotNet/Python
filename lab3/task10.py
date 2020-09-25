def can_calc_number(arr, number):
    sum = number
    for x in arr:
        if sum % x == 0:
            while sum > 0 and sum % x == 0:
                sum -= x
    return sum == 0


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 9]
    number = 85
    if can_calc_number(arr, number):
        print('Можно')
    else:
        print('Нельзя')