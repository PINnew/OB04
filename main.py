from abc import ABC, abstractmethod


# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Класс меча
class Sword(Weapon):
    def attack(self):
        print('Боец наносит удар мечом.')


# Класс лука
class Bow(Weapon):
    def attack(self):
        print('Боец наносит удар луком.')


# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец выбирает {weapon.__class__.__name__.lower()}.")

    def fight(self, monster):
        self.weapon.attack()
        monster.take_damage()


# Класс монстра
class Monster:
    def __init__(self):
        self.health = 100

    def take_damage(self):
        self.health -= 50  # Простая механика: каждый удар наносит 50 урона
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"Монстр получил урон! Текущее здоровье: {self.health}.")


# Демонстрация игры
if __name__ == "__main__":
    # Создаем оружие
    sword1 = Sword()
    bow1 = Bow()

    # Создаем бойца и монстра
    fighter = Fighter(sword1)
    monster = Monster()

    # Боец атакует мечом
    fighter.fight(monster)

    # Боец меняет оружие на лук и атакует снова
    fighter.change_weapon(bow1)
    fighter.fight(monster)
