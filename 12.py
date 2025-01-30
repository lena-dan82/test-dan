class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says tweet!")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says roar!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says hiss!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the zoo staff.")

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)
    print(f"Zoo saved to {filename}.")

def load_zoo(filename):
    with open(filename, 'rb') as file:
        zoo = pickle.load(file)
    print(f"Zoo loaded from {filename}.")
    return zoo
### Демонстрация работы


if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo()

    # Добавляем животных
    parrot = Bird("Parrot", 2)
    lion = Mammal("Lion", 5)
    snake = Reptile("Snake", 3)

    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Демонстрируем полиморфизм
    animal_sound(zoo.animals)

    # Добавляем сотрудников
    zookeeper = ZooKeeper("Alice")
    vet = Veterinarian("Bob")

    zoo.add_staff(zookeeper)
    zoo.add_staff(vet)

    # Используем методы сотрудников
    zookeeper.feed_animal(parrot)
    vet.heal_animal(lion)

    # Сохраняем и загружаем состояние зоопарка
    save_zoo(zoo, 'zoo_data.pkl')
    loaded_zoo = load_zoo('zoo_data.pkl')

#Этот код демонстрирует создание зоопарка, добавление животных и сотрудников, взаимодействие между ними, а также сохранение и загрузку состояния зоопарка.