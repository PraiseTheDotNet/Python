import re

def get_list_of_numbers(input: str):
    return [int(x) for x in re.findall(r'\d+', input)]

def get_sum_of_parents(data :list):
    if len(data) <= 1:
        return data
    res = []
    for x in range(len(data)):
        res.append(data[x - 1] + data[(x + 1) % len(data)])
    return res

if __name__ == '__main__':
    input = '5 6'
    data = get_list_of_numbers(input)
    print(input)
    print(' '.join([str(x) for x in get_sum_of_parents(data)]))
