from os import listdir, mkdir
from os.path import join, isdir, splitext

if __name__ == '__main__':
    x = 'files/task4/input'
    y = 'files/task4/output'
    dirs = [('', 0)]
    while len(dirs):
        (path, lvl) = dirs.pop()
        current = join(x, path)
        create = join(y, path)
        mkdir(create)
        elements = listdir(current)
        for element in elements:
            if isdir(join(current, element)):
                dirs.append((join(path, element), lvl + 1))
            elif splitext(element)[1] == '.txt':
                filePath = join(current, element)
                f = open(filePath, 'r', encoding="utf-8")
                lines = f.read().splitlines()
                f.close()
                f = open(join(create, element), 'w', encoding="utf-8")
                f.write(str(len(lines)) + '\n')
                for l in lines:
                    f.write(l + '\n')
                f.write(str(lvl))
                f.close()
    print('Копирование структуры завершено')
