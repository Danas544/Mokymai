import sqlite3

conn = sqlite3.connect("mokymai.db")
c = conn.cursor()

with conn:
    c.execute("SELECT DISTINCT vardas FROM DARBUOTOJAI")
    a = c.fetchall()
    print(a)
