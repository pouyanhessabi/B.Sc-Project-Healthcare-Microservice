import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'new9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/healthcare'
db = SQLAlchemy(app)
db.init_app(app)

mysql_db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='healthcare'
)


@app.route('/search_clinic')
def search_clinic(expertise):
    return f"expert is {expertise}"
