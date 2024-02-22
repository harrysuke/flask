import pymysql
from app import app
#from tables import Results
from db_config import mysql
from flask import flash, render_template, request, redirect, url_for, session
#from werkxeug.security import generate_password_hash, check_password_hash

@app.route('/')
def users():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        return render_template('users.html', rows = rows)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "localhost", port = int("5000")) 