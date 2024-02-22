from app import app
from flask_mysqldb import MySQL

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABSE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'goblog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_SOCKET'] = None

mysql.init_app(app)