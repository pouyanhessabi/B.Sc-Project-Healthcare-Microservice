from datetime import date

import mysql.connector
import requests
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

from services.ai.disease_detection import model_init, detect_disease_from_symptom
from services.ai.mapper import mapper_method
from services.ai.model import UserDisease, UserExpertise
from services.ai.shared_method import create_dictionary_from_formatted_ui_list, \
    create_formatted_list_from_dictionary_to_ui

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

ai_model = model_init(load_model=True)


@app.route('/')
def index():
    symptoms = read_symptoms_from_db()
    return render_template('symptoms.html', items=symptoms)


@app.route('/disease', methods=['POST'])
def disease_detection():
    symptoms = request.form.getlist('item[]')
    diseases = detect_disease_from_symptom(ai_model, symptoms)
    save_to_db_user_disease(diseases)
    formatted_list = create_formatted_list_from_dictionary_to_ui(diseases)
    return render_template('disease.html', diseases=formatted_list)


@app.route('/expertise', methods=['POST'])
def map_to_expertise():
    diseases = request.form.getlist('disease[]')
    expertises = mapper_method(create_dictionary_from_formatted_ui_list(diseases))
    save_to_db_user_expertise(expertises)
    formatted_list = create_formatted_list_from_dictionary_to_ui(expertises)
    return render_template('expertise.html', expertises=formatted_list)


@app.route('/search', methods=['POST'])
def search():
    expertise = request.form.get('expertise')
    print("expertise to search:", expertise)
    req_url = f'http://localhost:5002/search_doctors_another_service'
    response = requests.post(req_url, json={expertise: " "})
    return response.text


def read_symptoms_from_db():
    my_cursor = mysql_db.cursor()
    my_cursor.execute("SELECT name FROM symptom")
    symptoms = [row[0].strip() for row in my_cursor.fetchall()]
    return symptoms


def get_user_id():
    return session.get("_user_id")


def save_to_db_user_disease(diseases: dict):
    user_id = get_user_id()
    if user_id is None:
        user_id = 0
    for disease in diseases:
        if is_new_user_disease(user_id, disease):
            user_dis = UserDisease(user_id=user_id, disease=disease, ratio=float(diseases[disease]),
                                   req_date=date.today())
            db.session.add(user_dis)
    db.session.commit()


def is_new_user_disease(user_id, disease):
    my_cursor = mysql_db.cursor()
    where_data = (user_id, disease, date.today())
    my_cursor.execute('select * from user_disease where user_id = %s and disease = %s and req_date = %s', where_data)
    user_disease = my_cursor.fetchall()
    if not user_disease:
        return True
    else:
        return False


def save_to_db_user_expertise(expertises: dict):
    user_id = get_user_id()
    if user_id is None:
        user_id = 0
    for expertise in expertises:
        if is_new_user_expertise(user_id, expertise):
            user_expertise = UserExpertise(user_id=user_id, expertise=expertise, ratio=float(expertises[expertise]),
                                           req_date=date.today())
            db.session.add(user_expertise)
    db.session.commit()


def is_new_user_expertise(user_id, expertise):
    my_cursor = mysql_db.cursor()
    where_data = (user_id, expertise, date.today())
    my_cursor.execute('select * from user_expertise where user_id = %s and expertise = %s and req_date = %s',
                      where_data)
    user_expertise = my_cursor.fetchall()
    if not user_expertise:
        return True
    else:
        return False
