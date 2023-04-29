import sqlite3
import hashlib


conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = " Bulati", hashlib.sha256("Yeh_Duniya".encode()).hexdigest()
username2, password2 = " Hai_Magar", hashlib.sha256("Hai_Idhar".encode()).hexdigest()
username3, password3 = " Jaane_Ka", hashlib.sha256("Aane_Ka".encode()).hexdigest()
username4, password4 = " Nahi", hashlib.sha256("Nahi".encode()).hexdigest()


cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
