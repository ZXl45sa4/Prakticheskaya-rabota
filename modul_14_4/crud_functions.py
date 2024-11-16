import sqlite3


def initiate_db():
    open('Products.db', 'a').close()
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
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт1", f"описание1", f"100"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт2", f"описание2", f"200"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт3", f"описание3", f"300"))
    # cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                (f"Продукт4", f"описание4", f"400"))
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


initiate_db()
tovar = []
all_products = get_all_products()
for i in all_products:
    tovar.append({'Название': str(i[1]), 'Описание': str(i[2]), 'Цена': str(i[3])})
print(tovar)
