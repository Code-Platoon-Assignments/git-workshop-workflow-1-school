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

all_active_students = []

# Add some students
all_active_students.append(Student({'id': 1, 'first_name': 'Harry', 'last_name': 'Potter'}))
all_active_students.append(Student({'id': 2, 'first_name': 'Hermione', 'last_name': 'Granger'}))
all_active_students.append(Student({'id': 2, 'first_name': 'Ron', 'last_name': 'Weasley'}))

@app.route('/', methods=['GET'])
def base_route():
    return "ping"

@app.route('/students', methods=['GET'])
def get_students():
    """get all students"""
    student_list = [
        {'id': student.id, 'name': student.name}
        for student in all_active_students
    ]

    return jsonify(student_list)

IS_DEBUG_ENABLED = False
if os.environ['FLASK_ENV'] == 'dev':
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)
