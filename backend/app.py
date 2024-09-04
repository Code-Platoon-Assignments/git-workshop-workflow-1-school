import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from person import Person

load_dotenv()

print(os.environ["FLASK_ENV"])
print(os.environ["MY_SECRET_API_KEY"])

app = Flask(__name__)
CORS(app)


person_list = []

# Add some person
person_list.append(
    Person(
        {
            "id": 1, 
            "first_name": "Han", 
            "last_name": "Solo", 
            "email": "han@email.com",
            "force_powers": False,
        }
    )
)
person_list.append(
    Person(
        {
            "id": 2,
            "first_name": "Leia",
            "last_name": "Skywalker",
            "email": "leia@gmail.com",
            "force_powers": True,
        }
    )
)
person_list.append(
    Person(
        {
            "id": 3,
            "first_name": "Luke",
            "last_name": "Skywalker",
            "email": "luke@email.com",
            "force_powers": True,
        }
    )
)


@app.route("/", methods=["GET"])
def base_route():
    return "hello"


@app.route("/person", methods=["GET"])
def get_person():
    print("Adam's print statement on line 34.")
    """get all person"""
    Person_list = [
        {"id": Person.id, "first_name": Person.first_name, "email": Person.email, "force_powers": Person.force_powers}
        for Person in person_list
    ]

    return jsonify(Person_list)


IS_DEBUG_ENABLED = False
if os.environ["FLASK_ENV"] == "dev":
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)
