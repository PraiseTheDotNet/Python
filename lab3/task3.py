import random

def check_1(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
    return True


#  еще можно было сделать через set и len(set) )))))
def check_2(arr):
    unique = []
    for i in arr:
        if i in unique:
            return False
        else:
            unique.append(i)
    return True

if __name__ == '__main__':
    input = [random.randrange(0, 100) for _ in range(10)]
    print('Исходный набор', input)
    print('Уникальный набор' if check_1(input) else 'Не уникальный')
    print('Уникальный набор' if check_2(input) else 'Не уникальный')