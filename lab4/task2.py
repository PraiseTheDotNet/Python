from os import listdir
from os.path import isfile, join
import random

def parse_human(filePath):
    f = open(filePath, 'r', encoding="utf-8")
    lines = f.read().splitlines()
    f.close()
    key = lines[1] + ' ' + lines[3]
    age = lines[4] + ': ' + lines[5]
    eat = lines[6] + ': ' + lines[7]
    music = lines[8] + ': ' + lines[9]
    dream = lines[10] + ': ' + lines[11]
    return (key, [age, eat, music, dream])


if __name__ == '__main__':
    files = listdir('files/task2')
    dict = {}
    for file in files:
        path = join('files/task2', file)
        if (isfile(path)):
            (key, value) = parse_human(path)
            dict[key] = value
    (fullname, data) = random.choice(list(dict.items()))
    categories = data.copy()
    print('Угадай человека по категории')
    while len(categories):
        category = random.choice(categories)
        categories.remove(category)
        print(category, '\nОтвет:')
        user_fullname = input()
        if user_fullname == fullname:
            print('Поздравляем, вы угадали человека!')
            break;
        else:
            print('Нет, это другой человек')

    if not len(categories):
        print('Вы не угадали человека\nПравильный ответ:', fullname)


