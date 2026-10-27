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
        self.max_health = self.health

    def heal(self,enemy_damage):
        aid = r.randint(int(enemy_damage*0.5), int(enemy_damage*1.4))
        if self.health < self.max_health - aid:
            self.health += aid
            print(f"ТЫ ОТХИЛИЛСЯ НА {aid} HP, ЧЕРТ, ТЕПЕРЬ У ТЕБЯ {self.health} HP")
        else:
            print("Невозможно востановиться")


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

    user_input = input("\nЕсли ты не хочешь откинуться напиши 1\nЕсли ты хочешь убить его напиши 2\nВаш ответ: ")
    if user_input == "1":
        user.heal(enemy.damage)
    elif user_input == "2":
        enemy.be_attacked(user.damage)
        user.be_attacked(enemy.damage)
        print(f"Тебя побили на {enemy.damage}")
        if user.health <= 0:
            print(f"Победил {enemy.name}!")
            break
        elif enemy.health <= 0:
            print(f"Поздравляю вами был повержен {enemy.name}!!")
            break
