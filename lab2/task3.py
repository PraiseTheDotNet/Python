import re


def inset_with_regex(input: str):
    return re.sub(r'(.)\1*(?!$)', '\g<0>*', input)

def inset_without_regex(input: str):
    result = ''
    index = 0
    for i in range(1, len(input) + 1):
        if i == len(input):
            result += input[index:]
        elif input[i] != input[index]:
            result += input[index:i] + '*'
            index = i
    return result

if __name__ == '__main__':
    input = 'ппрол'
    input_2 = 'ееннне'
    print(inset_with_regex(input))
    print(inset_without_regex(input))

    print(inset_with_regex(input_2))
    print(inset_without_regex(input_2))