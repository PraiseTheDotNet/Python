from os import listdir, mkdir, rename
from os.path import join, isfile, isdir, getctime
import time


if __name__ == '__main__':
    dir = 'D:\Downloads'
    files = [file for file in listdir(dir) if isfile(join(dir, file))]
    for file in files:
        date_time = time.strptime(time.ctime(getctime(join(dir,file))))
        date = '{0:02d}.{1:02d}.{2}'.format(date_time.tm_mday, date_time.tm_mon, date_time.tm_year)
        date_dir = join(dir, date)
        if not isdir(date_dir):
            mkdir(date_dir)
        rename(join(dir, file), join(date_dir, file))
    print('Сортировка по датам завершена')
