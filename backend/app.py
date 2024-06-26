from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ['FLASK_ENV'])
print(os.environ['MY_SECRET_API_KEY'])

app = Flask(__name__)
CORS(app)


class Student:
    """student"""
    def __init__(self, data):
        self.id = data.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')

students_list = []

# Add some students
students_list.append(Student({'id': 1, 'first_name': 'Han', 'last_name': 'Solo', 'email' : 'han@email.com'}))
students_list.append(Student({'id': 2, 'first_name': 'Leia', 'last_name': 'Skywalker', 'email' : 'leia@gmail.com'}))
students_list.append(Student({'id': 3, 'first_name': 'Luke', 'last_name': 'Skywalker', 'email' : 'luke@email.com'}))

@app.route('/', methods=['GET'])
def base_route():
    return "ding"

@app.route('/students', methods=['GET'])
def get_students():
    print("Adam's print statement on line 34.")
    """get all students"""
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'email': student.email}
        for student in students_list
    ]

    return jsonify(student_list)

IS_DEBUG_ENABLED = False
if os.environ['FLASK_ENV'] == 'dev':
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)
