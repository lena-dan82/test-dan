from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

# Солнечная система

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(2)

def page_next():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    print(hatnotes)
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    time.sleep(1)

def link_next(find):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(find)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    a = browser.find_element(By.LINK_TEXT, find)
    a.click()
    time.sleep(1)

def paragraph_next(num):
    print("")
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    print(paragraphs[num].text)
    # todo отслеживание не превышения индекса
    # for paragraph in paragraphs:
    #     print(paragraph.text)

def game():
    print("Добро пожаловать в помощник по ВИКИ!")
    interes = input("Что Вас интересует?\n")
    link_next(interes)
    p = 1
    while True:
        print("\nВыберите действие:")
        print("1 - Перейти к поясняющей подчиненной теме")
        print("2 - Полистать текст по данному запросу")
        print("3 - Выйти из помощника")
        f = input()
        #print(f)
        if f == "1":
            page_next()
        elif f == "2":
            paragraph_next(p)
            p += 1
        else:
            browser.quit()
            break
    print("Всего хорошего.")

game()

