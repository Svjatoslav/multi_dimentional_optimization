import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def graph_3d(self):
    aa, bb = 3, 4
    plt.ion()  # включение интерактивного режима отображения графиков
    fig = plt.figure()
    ax = Axes3D(fig)
    a_plt = np.arange(-5, 5, 0.1)
    b_plt = np.arange(-5, 5, 0.1)
    a, b = np.meshgrid(a_plt, b_plt)

    dots = a.copy()
    for i in range(0, len(a_plt)):
        for j in range(0, len(b_plt)):
            dot = [a[i][j], b[i][j]]
            dots[i][j] = self.target_function(dot)

    ax.plot_surface(a, b, dots, color='y', alpha=0.5)

    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('E')
    ar = [aa,bb]

    point = ax.scatter(aa, bb, self.target_function(ar), c='red')  # отображение точки красным цветом




    for n in (self.X_step_points_array):
        # aa = aa - lmd1 * dEda(y, aa, bb)
        # bb = bb - lmd2 * dEdb(y, aa, bb)


        ax.scatter(n[0], n[1], self.target_function(n), c='red')

        # перерисовка графика и задержка на 10 мс
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(1)

        print(aa, bb)

    plt.ioff()   # выключение интерактивного режима отображения графиков
    plt.show()


