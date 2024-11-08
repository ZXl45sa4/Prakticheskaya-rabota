import sqlite3

connection = sqlite3.connect("not_telegram.db")
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

# Заполните её 10 записями:

# for i in range(1, 11):
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i}", f"example{i}@gmail.com", f"{i*10}", 1000))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:

# for i in range(1, 11, 2):
#     cursor.execute(f"UPDATE Users "
#                    f"SET balance = '500' "
#                    f"WHERE email = 'example{i}@gmail.com'")

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute(f"DELETE FROM Users WHERE username= 'user{i}'")

# Сделайте выборку всех записей при помощи fetchall(),
# где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
cursor.execute("SELECT username, email, age, balance "
               "FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()

for user in users:
    print(user)

connection.commit()
connection.close()
