from selenium import webdriver
from selenium.webdriver import Keys

#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By

#Библиотека с поиском элементов на сайте
import time


#Если мы работаем с Chrome
browser = webdriver.Chrome()

#В кавычках указываем URL сайта, на который нам нужно зайти
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")

#В кавычках указываем название, которое присвоится скриншоту
browser.save_screenshot("oop.png")

#Задержка в 5 секунд
time.sleep(5)

#Добавляем перезагрузку страницы:
browser.refresh()

#Задержка в 5 секунд
time.sleep(5)

#Закрываем браузер
browser.quit()
