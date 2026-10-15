import random as r

class Character:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

class User(Character):
    def __init__(self, name, damage, health):
        super().__init__(name, damage, health)


enemy1 = Character(name="Джон", damage=10, health=100)
enemy2 = Character(name="Арага", damage=100, health=10)
enemy3 = Character(name="Путин", damage=30, health=999)

user = User(name="Флинс", damage=10, health=200)

enemies = [enemy1, enemy2, enemy3]
enemy = r.choice(enemies)
print(f"Ваш противник {enemy.name}")
while True:
    print(f"(за) Ваше здоровье {user.health}, ваша сила атака {user.damage}")
    print(f"Здоровье противника {enemy.health}, атакама противоти {enemy.damage}")
