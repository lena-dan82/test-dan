#Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

#Исходные данные:
#Есть класс Fighter, представляющий бойца.
#Есть класс Monster, представляющий монстра.
#Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

#Шаг 1: Создайте абстрактный класс для оружия
#Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
#Шаг 2: Реализуйте конкретные типы оружия
#Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
#Шаг 3: Модифицируйте класс Fighter
#Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
#Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
#Шаг 4: Реализация боя
#Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.

#Пример результата:
#Боец выбирает меч.
#Боец наносит удар мечом.
#Монстр побежден!
#Боец выбирает лук.
#Боец наносит удар из лука.
#Монстр побежден!
from abc import ABC, abstractmethod

class Fighter:
    def __init__(self):
        self.naim = "Боец"
        self.weapon = None
    def change_weapon(self,weapon):
        self.weapon = weapon
        print(f"{self.naim} выбирает {self.weapon.naim}.")
    def attack_weapon(self):
        self.weapon.attack()
        print ("Монстр побежден!")


class Monster:
    def __init__(self):
        self.naim = "Монстр"

class Weapon(ABC):
    @abstractmethod
    def attack(self, ):
        pass


class Sword(Weapon):
    def __init__(self):
        self.naim = "Меч"
    def attack(self, ):
        print ("Боец наносит удар мечом.")

class Bow(Weapon):
    def __init__(self):
        self.naim = "Лук"
    def attack(self, ):
        print ("Боец наносит удар из лука.")

class Spear(Weapon):
    def __init__(self):
        self.naim = "Копье"
    def attack(self, ):
        print ("Боец наносит удар копьем.")

f = Fighter()
m = Monster()
s = Sword()
b = Bow()
k = Spear()
f.change_weapon(s)
f.attack_weapon()
f.change_weapon(b)
f.attack_weapon()
f.change_weapon(k )
f.attack_weapon()