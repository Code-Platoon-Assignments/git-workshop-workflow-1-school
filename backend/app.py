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
        self.name = data.get('name')

all_the_students = []

# Add some students
all_the_students.append(Student({'id': 1, 'name': 'Harry'}))
all_the_students.append(Student({'id': 2, 'name': 'Hermione'}))
all_the_students.append(Student({'id': 3, 'name': 'Ron'}))

@app.route('/', methods=['GET'])
def base_route():
    return "ding"

@app.route('/students', methods=['GET'])
def get_students():
    print("Adam's print statement on line 34.")
    """get all students"""
    student_list = [
        {'id': student.id, 'name': student.name}
        for student in all_the_students
    ]

    return jsonify(student_list)

IS_DEBUG_ENABLED = False
if os.environ['FLASK_ENV'] == 'dev':
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)
