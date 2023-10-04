import os
from datetime import date

# from sqlalchemy import and_
import mysql.connector
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

from services.auth.models import UserDisease
from .disease_detection import detect_disease

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


def read_symptoms():
    items = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data\\symptoms.txt')
    with open(file_path, 'r') as file:
        for line in file:
            items.append(line.strip())
    return items


@app.route('/submit', methods=['POST'])
def detect_disease_from_symptom():
    symptoms = request.form.getlist('item[]')
    print(symptoms)
    raw_disease = detect_disease(symptoms)
    # get the five highest value of dictionary(disease)
    diseases = dict(sorted(raw_disease.items(), key=lambda x: x[1], reverse=True)[:5])
    save_to_db_user_disease(diseases)

    return render_template('disease_expertise.html', diseases=diseases, expertises=diseases)


@app.route('/')
def index():
    items = read_symptoms()
    return render_template('detection.html', items=items)


def mapper(diseases: dict):
    pass


def is_new_user_disease(user_id, disease):
    # TODO
    my_cursor = mysql_db.cursor()
    where_data = (user_id, disease, date.today())
    my_cursor.execute('select * from user_disease where user_id = %s and disease = %s and req_date = %s', where_data)
    # user_disease = UserDisease.query.filter((UserDisease.user_id == user_id,
    # UserDisease.disease == disease,UserDisease.req_date == date.today())).all()
    user_disease = my_cursor.fetchall()
    # statement = select(UserDisease).where
    # (UserDisease.user_id == user_id and UserDisease.disease == disease and UserDisease.req_date == date.today())
    # user_disease = orm_session.execute(statement)
    if not user_disease:
        return True
    else:
        return False


def save_to_db_user_disease(diseases: dict):
    user_id = session.get("_user_id")
    for disease in diseases:
        user_disease = UserDisease(user_id=user_id, disease=disease, rate=float(diseases[disease]),
                                   req_date=date.today())
        if is_new_user_disease(user_id, disease):
            db.session.add(user_disease)
            print("xc")
    db.session.commit()
