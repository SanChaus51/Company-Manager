import random

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


    def attack(self, enemy):
        damage = random.randint(10, 30)
        enemy.hp -= damage
        print(f"⚔️⚔{self.name} вгатив {enemy.name} на {damage} урону!")

    def heal(self, amount):
        self.hp += amount
        print(f"✨ {self.name} випив зілля і відновив {amount} hp!")


class Mage(Hero):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def fireball(self, enemy):
        if self.mana >= 20:
            self.mana -= 20
            damage = random.randint(30, 50)
            enemy.hp -= damage
            print(f"🔥 {self.name} випустив Фаєрбол у {enemy.name} на {damage} магічного урону! (Залишок мани: {self.mana})")
        else:
            print(f"❌ {self.name} хотів чаклувати, але закінчилася мана!")
            self.attack(enemy)

# persons
hero1 = Mage("Akva", 100, 40)
hero2 = Hero("Kazuma", 100)

print("--- БИТВА ПОЧАЛАСЯ ---")

while hero1.hp > 0 and hero2.hp > 0:
    hero1.fireball(hero2)

    if hero2.hp > 0:
        hero2.attack(hero1)

    print(f"🩸 Стан: {hero1.name} [{hero1.hp} HP] | {hero2.name} [{hero2.hp} HP]\n")

if hero1.hp > 0:
    print(f"🏆 Переміг {hero1.name}!")
else:
    print(f"🏆 Переміг {hero2.name}!")
