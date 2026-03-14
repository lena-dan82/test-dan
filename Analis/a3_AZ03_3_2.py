# Нужно обработать данные в csv файле, нужно убрать в конце каждой строчки ₽/мес. и преобразовать в тип данных число. Напиши код на Python

import csv

def clean_price(price):
    return price.replace(' ', '')

# Чтение данных из исходного CSV файла и их обработка
input_file = 'd_prices.csv'
output_file = 'd_cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        if any(clean_row):  # Убрать пустые строки!
            writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")