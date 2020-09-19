import re


def insert_without_regex(text: str, string: str, letter: chr):
    return (letter + string).join(text.split(letter))

def insert_with_regex(text: str, string: str, letter: chr):
    return re.sub(letter, letter + string, text)

if __name__ == '__main__':
    # print('Введите текст')
    # text = input()
    text = 'тестовый текст текст текст'
    # print('Введите строку для вставки')
    # insert_str = input()
    insert_str = ' mS'
    #print('Введите букву')
    #letter = input()[0]
    letter = 'т'
    print(insert_without_regex(text, insert_str, letter))
    print(insert_with_regex(text, insert_str, letter))
