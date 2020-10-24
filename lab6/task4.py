import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    plt.subplot(projection='polar')
    r = 2.5
    phi = np.arange(0, 3 * np.pi / 2, step=0.1)
    ro = 2 * r * (1 + np.cos(phi))
    plt.plot(phi, ro, marker='*', color="green", linestyle="None")
    plt.legend(['Кардиоида'], title='Функция', loc='upper left', )
    plt.show()