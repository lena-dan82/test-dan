#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird (Animal):
    def __init__(self, name, age, plumage):
        super().__init__(name, age)
        self.plumage = plumage

    def make_sound(self):
        print("чик-чирик")


class Mammal (Animal):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age)
        self.coat_color = coat_color

    def make_sound(self):
        print("мяу")


class Reptile (Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        print("шшшш")


animal_sound = [Bird("Аист", 3, "Ч/Б"),
                Mammal("Кошак", 10, "Беж"),
                Reptile("Уж", 1, "Сизый")]
for animal in animal_sound:
    animal.make_sound()



class Employee():
    def __init__(self,surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def to_go(self):
        pass
    def speak(self):
        pass


class ZooKeeper (Employee):
    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)

    def feed_animal(self,animal):
        print(f"{self.name} кормит {animal.name}а.")

class Veterinarian (Employee):
    def __init__(self, surname, name, age):
        super().__init__(surname, name, age)

    def heal_animal(self,animal):
        print(f"{self.name} лечит {animal.name}а.")



class Zoo():
    def __init__(self):
        self.animals = []
        self.employee = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк.")

    def add_employee(self, employee):
        self.employee.append(employee)
        print(f"Принят {employee.name} в сотрудники зоопарка.")


zoopark =  Zoo()

Аист = Bird("Аист", 3, "Ч/Б")
Кошак = Mammal("Кошак", 10, "Беж")
Уж = Reptile("Уж", 1, "Сизый")

zoopark.add_animal(Аист)
zoopark.add_animal(Кошак)
zoopark.add_animal(Уж)

zookeeper = ZooKeeper("Данилов","Дмитрий", 18)
vet = Veterinarian("Данилов", "Иван",18)

zoopark.add_employee(zookeeper)
zoopark.add_employee(vet)

zookeeper.feed_animal(Аист)
vet.heal_animal(Кошак)

file1="Zoopark_fail.txt"
with open(file1, "w", encoding="utf-8") as file:
    file.write(f"Состав зоопарка:\n")
    file.write(f"Животные: {zoopark.animals} \n")
    file.write(f"Сотрудники: {zoopark.employee}")


with open(file1, "r", encoding="utf-8") as file:
    print(file.read( ))