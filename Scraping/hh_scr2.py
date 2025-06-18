#Код, написанный с использованием новых селекторов.
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://nn.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(6)

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.vacancy-info--ieHKDTkezpEj0Gsx')

parsed_data = []

for vacancy in vacancies:
    try:
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-header-section-2')
        title = title_element.text
        link = title_element.get_attribute('href')
        company = vacancy.find_element(By.CSS_SELECTOR, 'span data-qa="vacancy-serp__vacancy-employer-text"').text

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'compensation-labels--vwum2s12fQUurc2J').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)