#2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv​

import pandas as pd
df = pd.read_csv('dz.csv')

salarys = df.groupby('City')['Salary'].mean()

print(salarys)