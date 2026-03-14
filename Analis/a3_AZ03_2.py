# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
# массив из 5 случайных чисел

import matplotlib.pyplot as plt
import numpy as np

random_array_X = np.random.rand(5)
random_array_Y = np.random.rand(5)

plt.scatter(random_array_X, random_array_Y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")
plt.show()
