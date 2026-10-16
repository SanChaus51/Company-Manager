import sqlite3  # СИСТЕМНА назва модуля

con = sqlite3.connect("bot_database.db")
cursor = con.cursor()

# ⬇️ 1. СПОЧАТКУ ВИДАЛЯЄМО старі таблиці, щоб повністю оновити структуру
cursor.execute("DROP TABLE IF EXISTS items;")
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS newUp;")
cursor.execute("DROP TABLE IF EXISTS TnUP;")
cursor.execute("DROP TABLE IF EXISTS DUOnUP;")

con.commit()

# ⬇️ 2. СТВОРЮЄМО ТАБЛИЦЮ ТОВАРІВ
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price INTEGER
);
''')

# ⬇️ СТВОРЮЄМО ТАБЛИЦЮ ЗАМОВЛЕНЬ (Тепер із ціною 'price' та кількістю 'quantity')
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    price INTEGER,
    quantity INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS newUp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    named TEXT,
    fix INTEGER,
    sum INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TnUP (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_car TEXT,
    price_car INTEGER,
    quantity_car INTEGER,
    count_car INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS DUOnUP (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nam TEXT,
    region TEXT,
    people INTEGER
);
''')

con.commit()

# ⬇️ 3. ДОДАЄМО ТОВАРИ В МАГАЗИН (Тут усе було супер)
cursor.execute("INSERT INTO items (title, price) VALUES ('mouse', 600);")
cursor.execute("INSERT INTO items (title, price) VALUES ('iphone', 45000);")
cursor.execute("INSERT INTO items (title, price) VALUES ('gta', 1200);")

# ⬇️ ДОДАЄМО СТРАВИ (Тепер чітко передаємо спочатку ЦІНУ, а потім КІЛЬКІСТЬ штук!)
cursor.execute("INSERT INTO orders (item_name, price, quantity) VALUES ('pizza', 40, 1);")
cursor.execute("INSERT INTO orders (item_name, price, quantity) VALUES ('chicken', 300, 1);")
cursor.execute("INSERT INTO orders (item_name, price, quantity) VALUES ('burger', 50, 2);")
cursor.execute("INSERT INTO orders (item_name, price, quantity) VALUES ('cola', 10, 3);")

cursor.execute("INSERT INTO newUp (named, fix, sum) VALUES ('brick', 2, 54);")
cursor.execute("INSERT INTO newUp (named, fix, sum) VALUES ('car', 4, 67);")
cursor.execute("INSERT INTO newUp (named, fix, sum) VALUES ('house', 1, 14);")
cursor.execute("INSERT INTO newUp (named, fix, sum) VALUES ('shop', 3, 44);")
cursor.execute("INSERT INTO newUp (named, fix, sum) VALUES ('PC', 11, 124);")

cursor.execute("INSERT INTO TnUP (name_car, price_car, quantity_car, count_car) VALUES ('BMW', 20000, 8, 200);")
cursor.execute("INSERT INTO TnUP (name_car, price_car, quantity_car, count_car) VALUES ('Mercedes', 22000, 7, 600);")
cursor.execute("INSERT INTO TnUP (name_car, price_car, quantity_car, count_car) VALUES ('Audi', 21000, 9, 170);")

cursor.execute("INSERT INTO DUOnUP (nam, region, people) VALUES ('Kyiv', 'k', 1800000);")
cursor.execute("INSERT INTO DUOnUP (nam, region, people) VALUES ('Lviv', 'l', 800000);")
cursor.execute("INSERT INTO DUOnUP (nam, region, people) VALUES ('Odesa', 'o', 1350000);")
con.commit()

cursor.execute('''
SELECT * FROM newUp ORDER BY sum DESC;''')

pen_cil = cursor.fetchall()

print("GAY your loot is sortett for up GAY")
for fel in pen_cil:
    print(fel)

cursor.execute('''
SELECT * FROM TnUp ORDER BY price_car DESC;''')

mashinki_list = cursor.fetchall()

print("--- CARS MORE EXPENSIVE ---")
for fel in mashinki_list:
    print(fel)

cursor.execute('''
SELECT * FROM DUOnUp ORDER BY people DESC;''')

city_list = cursor.fetchall()

print("==- city in Ukraine -==")
for fel in city_list:
    print(fel)
print("📦 Все створено та додано ідеально! Перевіряй DB Browser!")

con.close()  # ГОЛОВНИЙ АТРИБУТ (закрити міст)
