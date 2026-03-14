# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()
url = 'https://www.divan.ru/nizhny-novgorod/category/divany-i-kresla'
driver.get(url)
time.sleep(5)

prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

with open('d_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    for price in prices:
        writer.writerow([price.text])

driver.quit()


