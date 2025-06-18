#Код, написанный экспертом в уроке.
# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()
# Если мы используем Chrome, пишем
# driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz223=on&af=on&ca=on&pc=on&pa=on&priceFromGeneral=500000&currencyIdGeneral=-1"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'search-registry-entry-block')

# Выводим на экран
print(vacancies)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
   try:
   # Находим элементы внутри вакансий по значению

     number = vacancy.find_element(By.CSS_SELECTOR, 'div.registry-entry__header-mid__number').text
     print(number)
     # Находим названия вакансии
     title = vacancy.find_element(By.CSS_SELECTOR, 'div.registry-entry__body-value').text
     print(title)
     # Находим названия компаний
     company = vacancy.find_element(By.CSS_SELECTOR, 'div.registry-entry__body-href').text
     print(company)
     # Находим зарплаты
     salary = vacancy.find_element(By.CSS_SELECTOR, 'div.price-block__value').text
     print(salary)
     # Находим ссылку с помощью атрибута 'href'
     link = vacancy.find_element(By.CSS_SELECTOR, 'div.registry-entry__header-mid__number')
     link = link.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
     #link = vacancy.find_element(By.CSS_SELECTOR, 'target._blank').get_attribute('href')
     print(link)
     # Вносим найденную информацию в список
     parsed_data.append([number, title, company, salary, link])

   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except:
     print("произошла ошибка при парсинге")
     continue

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['№', 'Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)