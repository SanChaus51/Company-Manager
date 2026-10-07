import sqlite3 # СИСТЕМНА назва модуля. Міняти не можна!

# con — це ТВОЯ РАНДОМНА назва змінної
con = sqlite3.connect("bot_database.db")
# cursor — це ТВОЯ РАНДОМНА назва змінної
cursor = con.cursor()

# cursor.execute — це ГОЛОВНИЙ АТРИБУТ (команда запуску)
# INSERT INTO ... VALUES — це ГОЛОВНІ СЛОВА SQL (Вставити в ... Значення)
# alab — це ТВОЯ РАНДОМНА назва таблиці, яку ти створив минулого разу!
cursor.execute('''
INSERT INTO alab (id, name, balance, role) 
VALUES (1, 'Dmytro', 2000, 'student');
''')

# con.commit — це ГОЛОВНИЙ АТРИБУТ (залізобетонно зберегти зміни у файл)
con.commit()
# con.close — це ГОЛОВНИЙ АТРИБУТ (закрити міст)
con.close()

print("👤 Першого користувача успішно додано в таблицю!")
