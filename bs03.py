from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")


# #Создадим отдельную переменную text, куда будут сохраняться все цитаты
# #text = soup.find("span", class_="text")
#
# #Чтобы найти все цитаты с заданным тегом и классом, введи код:
# text = soup.find_all("span", class_="text")
#
# print(text)


#Создадим отдельную переменную text, куда будут сохраняться все цитаты
text = soup.find_all("span", class_="text")
print(text)
#Создадим отдельную переменную author, куда будут сохраняться все авторы
author = soup.find_all("small", class_="author")
print(author)