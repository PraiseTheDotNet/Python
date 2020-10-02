import re


if __name__ == '__main__':
    f = open('files/input.txt','r', encoding="utf-8")
    lines = f.readlines()
    f.close()

    dictionary = {}

    for line in lines:
        words = re.findall(r'\w+', line)
        #  первое слово - англ
        #  остальные - русский
        for russian_word in words[1:]:
            dictionary.setdefault(russian_word, [])
            dictionary[russian_word].append(words[0])
    f = open('files/output.txt', 'w', encoding="utf-8")
    word_list = list(dictionary.items())
    word_list.sort(key=lambda x: x[0])
    for (word, translate) in word_list:
        translate.sort()
        f.write('{0} - {1}\n'.format(word, ', '.join(translate)))
    f.close()