import random as r

class Character:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def be_attacked(self, enemy_damage):
        self.health -= enemy_damage

class User(Character):
    def __init__(self, name, damage, health):
        super().__init__(name, damage, health)


enemy1 = Character(name="Джон", damage=10, health=100)
enemy2 = Character(name="Мединский", damage=100, health=10)
enemy3 = Character(name="Путин", damage=30, health=999)

user = User(name="Флинс", damage=10, health=200)

enemies = [enemy1, enemy2, enemy3]
enemy = r.choice(enemies)
print(f"Ваш противник {enemy.name}")
while True:
    print(f"(за) Ваше здоровье {user.health}, ваша сила атака {user.damage}")
    print(f"Здоровье противника {enemy.health}, атакама противоти {enemy.damage}")

    enemy.be_attacked(user.damage)
    user.be_attacked(enemy.damage)
    print(f"Тебя побили на {enemy.damage}")
    if user.health <= 0:
        print(f"Победил {enemy.name}!")
        break
    elif enemy.health <= 0:
        print(f"Поздравляю вами был повержен {enemy.name}!!")
        break
