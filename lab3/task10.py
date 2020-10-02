def can_calc_number(arr, number):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            current_sum = sum(arr[i:j])
            if current_sum == number and j - i > 1:
                return True

    return False


if __name__ == '__main__':
    arr = [2, 3, 4, 7, 9]
    number = 5
    if can_calc_number(arr, number):
        print('Можно')
    else:
        print('Нельзя')