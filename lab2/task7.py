import re


def format_with_regex(input: str):
    result = input
    result = re.sub(r'(?P<space>[-—\(\{\[.,!?:;\)\]\}])', r' \g<space> ', result)
    result = re.sub(r'\s+', r' ', result)
    result = re.sub(r'(\s(?=[.,!?:;\)\]\}]))|((?<=[\(\{\[])\s+)', r'', result)
    return result


def format_without_regex(input: str):
    word_list = []
    word = ''
    space = False
    last = ''
    for s in input:
        if not s.isspace():
            if s in ['-', '—']:
                if len(word):
                    word_list.append(word)
                    word = ''
                word_list.append(s)
                space = False
            if s.isalnum() and (not space or last in ['(', '[', '{']):
                word += s
                space = False
            elif s.isalnum():
                if len(word):
                    word_list.append(word)
                word = s
                space = False
            elif s in ['(', '[', '{']:
                if len(word):
                    word_list.append(word)
                word = s
                space = False
            elif s in ['.', ',', '!', '?', ';', ':', ')', '[', ']', '{', '}']:
                # if last == '.' and s == '.' or last.isalnum():
                word += s
                # else:
                #     if len(word):
                #         word_list.append(word)
                #     word_list.append(s)
                #     space = False
                #     word = ''
            last = s
        else:
            space = True
    if len(word):
        word_list.append(word)
    return ' '.join(word_list)

if __name__ == '__main__':
    input = "Ехал грека через реку ,видит грека— в реке рак .Сунул грека( рр )руку в реку :рак за руку греку — цап   !  цап цап цап.   .  ."
    print('Входные данные:')
    print(input)
    print('Регекс:')
    print(format_with_regex(input))
    print('Не регекс:')
    print(format_without_regex(input))