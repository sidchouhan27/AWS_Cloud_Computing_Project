import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS users""")
cur.execute("""CREATE TABLE users (Username text,Password text,firstname text, lastname text, email text, count integer)""")

conn.commit()
conn.close()
