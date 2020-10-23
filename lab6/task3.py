import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'files/task3.txt'
    f = open(path, 'r', encoding="utf-8")
    data = f.read().splitlines()
    f.close()
    precipitation = {}
    for line in data:
        info = line.split(' ')
        precipitation[info[0]] = int(info[1])
    print(precipitation)