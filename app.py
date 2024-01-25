from flask import Flask, render_template, request
import pymysql


app = Flask(__name__)

conn = pymysql.connect(
        host= "localhost",
        port = 3306,
        user = "root",
        password = "Dhanaraju@07",
        db = "users"
        
        )


def insert_details(name,age,city):
    cur=conn.cursor()
    cur.execute("INSERT INTO user (name,age, city) VALUES (%s,%s,%s)", (name,age,city))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM user")
    details = cur.fetchall()
    return details

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def get_users_data():
    details = db.get_details()
    return render_template('users.html', users=details)

@app.route('/create_user', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        db.insert_details(name, age, city)
        details = db.get_details()
        return render_template('create_user.html', var=details[-1]) 
    else:
        return render_template('create_user.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
