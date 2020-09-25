import re


def parse_with_regex(input: str):
    return re.findall(r'[а-яА-Яa-zA-Z]+', input)


def parse_without_regex(input: str):
    word_list = []
    word = ''
    for s in input:
        if s.isalpha():
            word += s
        elif len(word):
            word_list.append(word)
            word = ''
    if len(word):
        word_list.append(word)
    return word_list


def group_words(word_list):
    word_list.sort()
    count = 0
    words = []
    for i in range(len(word_list)):
        if i < len(word_list) - 1 and word_list[i] == word_list[i + 1]:
            count += 1
        else:
            if count == 0:
                words.append((word_list[i], 1))
            else:
                words.append((word_list[i], count + 1))
                count = 0
    return words

def print_data(word_list, name):
    print('\nСписок слов', name, ':')
    word_list = group_words(word_list)
    word_list.sort(key=lambda tup: len(tup[0]), reverse=True)
    for (word, count) in word_list:
        if count > 1:
            print(word, '(', count, ')', end=', ')
        else:
            print(word, end=', ')


if __name__ == '__main__':
    input = "Ехал грека через реку ,видит грека— в реке рак .Сунул грека( рр )руку в реку :рак за руку греку — цап   !  цап цап цап.   .  ."
    print_data(parse_with_regex(input), 'с регексом')
    print_data(parse_without_regex(input), 'без регекса')