import re


def replace_with_regex(input: str):
    text = input
    while re.search(r'(\([^()]*\))', text):
        text = re.sub(r'(\([^()]*\))', '', text)
    return text


def replace_without_regex(input: str):
    result = ''
    open_count: int = 0
    for s in range(len(input)):
        if input[s] == '(':
            open_count += 1
        elif input[s] == ')':
            open_count -= 1
        elif open_count == 0:
            result += input[s]
    return result

if __name__ == '__main__':
    input = '9(е(е()))9((()))9'
    print('С регексом:')
    print(replace_with_regex(input))
    print('Без регекса:')
    print(replace_without_regex(input))