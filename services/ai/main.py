import os
from datetime import date

import mysql.connector
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

from services.ai.disease_detection import detect_disease_from_symptom
from services.ai.mapper import mapper_method
from services.ai.shared_method import create_dictionary_from_formatted_ui_list
from services.auth.models import UserDisease

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
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
    items = read_symptoms()
    return render_template('symptoms.html', items=items)


@app.route('/disease', methods=['POST'])
def disease_detection():
    symptoms = request.form.getlist('item[]')
    diseases = detect_disease_from_symptom(symptoms)
    save_to_db_user_disease(diseases)
    formatted_diseases = [f'{key}: {value}' for key, value in diseases.items()]
    return render_template('disease.html', diseases=formatted_diseases)


@app.route('/expertise', methods=['POST'])
def map_to_expertise():
    diseases = request.form.getlist('disease[]')
    expertises = mapper_method(create_dictionary_from_formatted_ui_list(diseases))
    return render_template('expertise.html', expertises=expertises)


def read_symptoms():
    items = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data\\symptoms.txt')
    with open(file_path, 'r') as file:
        for line in file:
            items.append(line.strip())
    return items


def get_user_id():
    return session.get("_user_id")


def save_to_db_user_disease(diseases: dict):
    user_id = get_user_id()
    for disease in diseases:
        user_dis = UserDisease(user_id=user_id, disease=disease, rate=float(diseases[disease]), req_date=date.today())
        if is_new_user_disease(user_id, disease):
            db.session.add(user_dis)
    db.session.commit()


def is_new_user_disease(user_id, disease):
    my_cursor = mysql_db.cursor()
    where_data = (user_id, disease, date.today())
    my_cursor.execute('select * from user_disease where user_id = %s and disease = %s and req_date = %s', where_data)
    user_disease = my_cursor.fetchall()
    """"session.execute(select(User.name, User.fullname)).first()"""""
    # user_disease = UserDisease.query.filter_by(user_id=user_id, disease=disease, req_date=date.today())
    if not user_disease:
        return True
    else:
        return False
