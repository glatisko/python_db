import sqlite3

connection = sqlite3.connect('users-sqlite.db')

cursor = connection.cursor()

# CREATE TABLE
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
	(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name TEXT, 
   		last_name TEXT,
		email_address TEXT)''')

# INSERT DATA
users_to_insert = [('Sarah', 'Perry', 'sarah.perry@gmail.com'),
	('Felix', 'Martin', 'felix_martin@gmail.com'),
	('John', 'Patrick', 'johnny.patrick@outlook.com'),
	('Jessica', 'Jones', 'jess.jones@hotwire.com'),
	('Percy', 'Colton', 'percy_c@outlook.com')]

cursor.executemany('''INSERT INTO Users(first_name, last_name,
	email_address) VALUES (?,?,?)''', users_to_insert)

# FILTER TABLE
last_name = ('Martin',)   #!!!this is alway a tuple
cursor.execute("SELECT * FROM Users WHERE last_name=?", last_name)
print(cursor.fetchall())

# no filter
#cursor.execute("SELECT * FROM Users")
#print(cursor.fetchall())

connection.commit()
connection.close()