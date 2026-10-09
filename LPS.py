import random  # 🎲 Підключаємо модуль рандому


class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # ⚔️ Оновлений метод атаки. Тепер damage вираховується автоматично!
    def attack(self, enemy):
        damage = random.randint(10, 30)  # Генеруємо випадковий удар від 10 до 30
        enemy.hp -= damage
        print(f"⚔️ {self.name} вгатив {enemy.name} на {damage} урону!")


# --- ЗОНА БИТВИ (Основний код без відступів) ---

# Створюємо двох бійців (дамо обом по 100 HP для чесного бою)
hero1 = Hero("Akva", 100)
hero2 = Hero("Kazuma", 100)

print("--- 🏁 БИТВА ПОЧАЛАСЯ --- \n")

# 🔄 Цикл працює автоматично, поки ОДВА ГЕРОЇ мають здоров'я більше нуля!
while hero1.hp > 0 and hero2.hp > 0:

    # 1. Аква робить свій хід
    hero1.attack(hero2)

    # Перевіряємо, чи вижив Казума після удару, щоб відповісти
    if hero2.hp > 0:
        hero2.attack(hero1)

    # Виводимо поточний стан здоров'я після кожного раунду
    # Якщо HP падає нижче 0, виведемо красивий 0 за допомогоюmax()
    hp1 = max(0, hero1.hp)
    hp2 = max(0, hero2.hp)
    print(f"🩸 Стан: {hero1.name} [{hp1} HP] | {hero2.name} [{hp2} HP]\n")

# --- СУДДІВСЬКА СЕКЦІЯ ---
if hero1.hp > 0:
    print(f"🏆 Переміг {hero1.name}! (Залишилось {hero1.hp} HP)")
else:
    print(f"🏆 Переміг {hero2.name}! (Залишилось {hero2.hp} HP)")
