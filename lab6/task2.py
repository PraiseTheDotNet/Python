from os import listdir
from os.path import join, splitext
import re
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'files/tests'
    elements = [x for x in listdir(path) if join(path, x) and splitext(x)[1] == '.txt']
    for x in range(len(elements)):
        print('{0}) {1}'.format(x, elements[x]))
    print('Введите номер файла:')
    number = -1
    while number == -1:
        val = input()
        if val.isdigit() and int(val) in range(len(elements)):
            number = int(val)
        else:
            print('Неверное значение!')

    f = open(join(path, elements[number]), 'r', encoding="utf-8")
    text = f.readlines()
    f.close()
    word_count = {}
    for line in text:
        words = re.findall(r'\w+', line)
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1], reverse=True)
    top = word_list[:50]
    words = [x for (x, y) in top]
    counts = [y for (x, y) in top]
    plt.barh(words, counts)
    plt.ylabel("Слова")
    plt.xlabel("Сколько раз встречается")
    plt.show()

