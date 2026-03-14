# Нужно построить график гистограмму для получившихся цен из файла ”cleaned_prices.csv” с использованием модуля matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'd_cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()