import matplotlib.pyplot as plt
import numpy as np

# a = np.array([1, 2, 3, 4])
# a = np.zeros((3, 3))            # заполненный 0:
# a = np.ones((2, 5))             # заполненный единицами:
# a = np.random.random((2, 5))    # заполненный рандомными числами от до 1:
# a = np.arange(0, 10, 2)     # заполненный последовательностью чисел. В круглых скобках указываем начало, конец и шаг:
# a = np.linspace(0, 1, 10)        # заполненный числами, равно распределёнными между друг другом. В круглых скобках указываем начало, конец и количество чисел:
# print(a)

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x**2")

plt.grid(True)
plt.show()


