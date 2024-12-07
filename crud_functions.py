import sqlite3
connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    #cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
    #               (1, 'Счастье', '❤', 100))
    #cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
    #               (2, 'Уют', '❤❤', 200))
    #cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
    #               (3, 'Любовь', '❤❤❤', 300))
    #cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
    #               (4, 'Радость', '❤❤❤❤', 400))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    connection.commit()
    users = cursor.fetchall()
    ans = []
    for user in users:
        print(user)
        ans.append(user)
    return ans

    connection.commit()
    connection.close()


connection.commit()
connection.close()
