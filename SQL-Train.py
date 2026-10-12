import sqlite3  # СИСТЕМНА назва модуля

con = sqlite3.connect("bot_database.db")
cursor = con.cursor()

# ⬇️ 1. СПОЧАТКУ ВИДАЛЯЄМО старі таблиці, щоб повністю оновити структуру
cursor.execute("DROP TABLE IF EXISTS items;")
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS newUp;")

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
con.commit()

print("📦 Все створено та додано ідеально! Перевіряй DB Browser!")

con.close()  # ГОЛОВНИЙ АТРИБУТ (закрити міст)
