import sqlite3 as sql

connection = sql.connect("user.db")

cursorOBJ = connection.cursor()

with connection:
    connection.execute("""
    """)

# CREATE TABLE user (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(50),
#     email VARCHAR(255),
#     password VARCHAR(30)
# );

# INSERT INTO user VALUES(1, "admin", "admin@gmail.com", "admin")