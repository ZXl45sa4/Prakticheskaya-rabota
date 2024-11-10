import sqlite3

connection = sqlite3.connect("not_telegram_2.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute(f"DELETE FROM Users WHERE id = '6'")

# Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]  # один элемент
print(total1)

# Посчитать сумму всех балансов.
cursor.execute("SELECT SUM(balance) FROM Users")
total1 = cursor.fetchone()[0]  # один элемент
print(total1)

# Вывести в консоль средний баланс всех пользователей
cursor.execute("SELECT AVG(balance) FROM Users")
total1 = cursor.fetchone()[0]  # один элемент
print(total1)

# cursor.execute("SELECT * FROM Users")

users = cursor.fetchall()

for user in users:
    print(user)

connection.commit()
connection.close()
