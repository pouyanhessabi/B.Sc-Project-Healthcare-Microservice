import mysql.connector
from flask import Flask, render_template, request
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


@app.route('/')
def index():
    expertises = read_expertise_from_db()
    return render_template('default.html', expertises=expertises)


@app.route('/search_doctors_web', methods=['POST'])
def search_web():
    expertise = request.form.get('expertise')
    return search(expertise)


@app.route('/search_doctors_another_service', methods=['POST'])
def search_another_service():
    dict_expertise = request.get_json(force=True)
    expertise = separate_value_before_colon(list(dict_expertise.keys())[0])
    return search(expertise)


def search(expertise: str):
    doctors_tuple = load_doctors_by_expertise(expertise)
    doctors = create_doctors_list(doctors_tuple)
    print('expertise search', expertise)
    print('doctors', doctors)
    return render_template('search.html', expertise=expertise, doctors=doctors)


def load_doctors_by_expertise(expertise: str):
    my_cursor = mysql_db.cursor()
    where_data = (expertise,)
    my_cursor.execute('select * from doctor where expertises = %s order by rate DESC', where_data)
    doctors = my_cursor.fetchall()
    return doctors


def doctor_tuple_to_dictionary(doctor: tuple):
    id_, email, password, name, code, rate, expertises, clinic, image_src = doctor
    doctor_dictionary = {
        'id': id_, 'email': email, 'password': password, 'name': name, 'code': code, 'rate': rate,
        'expertises': expertises, 'clinic': clinic, "image_src": image_src
    }

    return doctor_dictionary


def create_doctors_list(doctors: list):
    doctors_list = []
    for doctor in doctors:
        doctors_list.append(doctor_tuple_to_dictionary(doctor))
    return doctors_list


def read_expertise_from_db():
    my_cursor = mysql_db.cursor()
    my_cursor.execute("SELECT name FROM expertise")
    expertise = [row[0].strip() for row in my_cursor.fetchall()]
    return expertise


def separate_value_before_colon(string):
    colon_index = string.find(":")
    if colon_index != -1:
        result = string[:colon_index].strip()
    else:
        result = string  # Handle the case where no colon is found
    return result
