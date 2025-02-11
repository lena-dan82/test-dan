# Кто кого...
class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
    def attack(self, other):
        print(f"{self.name} наносит удар {other.name}.")
    def apply_damage(self,damage):
        self.health -=damage
        print(f"У {self.name} осталось {self.health} здоровья.")
    def is_alive(self):
        return self.health > 0


class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.round = 0
        self.isActive = True
        self.start()
    def start(self):
        print("\nИгра началась!")
        while self.isActive == True:
            self.round += 1
            print(f"\nРаунд {self.round}:")
            self.isActive = self.next_round()
        if  self.player.is_alive != True:
            print(f"Победил {self.player.name }")
        else:
            print(f"Победил {self.computer.name }")
        print("\nИгра закончилась!")
    def next_round (self):
        if self.round % 2 != 0:
            self.player.attack(self.computer)
            self.computer.apply_damage(self.player.attack_power)
            return self.computer.is_alive()
        else:
            self.computer.attack(self.player)
            self.player.apply_damage(self.computer.attack_power)
            return self.player.is_alive()

p = Hero("Витязь")
c = Hero("Вражина")
g = Game(p,c)



