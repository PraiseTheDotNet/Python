import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'files/task3.txt'
    f = open(path, 'r', encoding="utf-8")
    data = f.read().splitlines()
    f.close()
    months = []
    precipitations = []
    for line in data:
        info = line.split(' ')
        months.append(info[0])
        precipitations.append(int(info[1]))

    plt.figure(figsize=(24, 8))

    plt.subplot(221)
    plt.bar(months, precipitations)
    plt.grid(True)

    plt.subplot(222)
    plt.plot(months, precipitations)
    plt.grid(True)

    plt.subplot(223)
    plt.barh(months, precipitations)
    plt.grid(True)

    plt.subplot(224)
    plt.pie(precipitations, labels=months)
    plt.grid(True)

    plt.savefig('files/Precipitations.png')