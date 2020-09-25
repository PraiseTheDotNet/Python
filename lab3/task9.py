def get_intersections(input_1, input_2):
    second = input_2.copy()
    result = []
    for x in input_1:
        if x in second:
            result.append(x)
            second.remove(x)
    return result



if __name__ == '__main__':
    input_1 = [1, 2, 2, 3, 4, 7, 7]
    input_2 = [2, 3, 3, 4, 5, 5, 6, 7, 7, 7]
    print('Пересечение:', get_intersections(input_1, input_2))
