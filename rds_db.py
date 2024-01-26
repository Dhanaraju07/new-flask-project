import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Dhanaraju@07",
    db="users"
)

def insert_details(name, age, city):
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS users')
    cur.execute("INSERT INTO user (username, age, city) VALUES (%s, %s, %s)", (name, age, city))
    conn.commit()

def get_details():
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS users')
    cur.execute("SELECT * FROM user")
    details = cur.fetchall()
    return details