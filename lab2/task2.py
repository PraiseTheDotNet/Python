import re


def calc_with_regex(input: str):
    return sum([int(x) for x in re.findall(r'[-]?\d+', input)])

def calc_without_regex(input: str):
    sum = 0
    start: int = -1
    for i in range(len(input) + 1):
        if i < len(input) and (input[i].isdigit() and start == -1):
            start = i
        elif i == len(input) or (start != -1 and not input[i].isdigit()):
            coef = 1
            if start > 0 and input[start-1] == '-':
                coef = -1
            sum += coef * int(input[start:i])
            start = -1
    return sum


if __name__ == '__main__':
    input = '512 + 242342 --324234 ...32435 34343 2257'
    print(calc_with_regex(input))
    print(calc_without_regex(input))