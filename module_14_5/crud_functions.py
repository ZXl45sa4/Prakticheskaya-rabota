import sqlite3


def initiate_db():
    open('Products.db', 'a')
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    Id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER PRIMARY KEY,
    username  TEXT NOT NULL,
    email TEXT NOT NULL,
    age  INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    # cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
    #                ("new-user", "ex@gmail.com", "28", "1000"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт1", f"описание1", f"100"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт2", f"описание2", f"200"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт3", f"описание3", f"300"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт4", f"описание4", f"400"))

    connection.commit()


def is_included(username):
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM Users WHERE username=?", (username,))
    rez = cursor.fetchone()
    if not rez:
        print('Добавил в базу')
        return True
    else:
        print('Уже в базе')
        return False


def add_user(username, email, age):
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, "1000"))
    connection.commit()
    connection.close()


def get_all_products():
    # record = []
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


def get_all_users():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    list_user = cursor.fetchall()
    connection.commit()
    return list_user


initiate_db()
tovar = []
all_products = get_all_products()
for i in all_products:
    tovar.append({'Название': str(i[1]), 'Описание': str(i[2]), 'Цена': str(i[3])})
print(tovar)

polzovatel = []
all_users = get_all_users()
for j in all_users:
    polzovatel.append({'username': str(j[1]), 'email': str(j[2]), 'age': str(j[3]), 'balance': str(j[4])})
print(polzovatel)
