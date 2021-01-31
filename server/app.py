from flask import Flask
from flask import jsonify
from flask import request
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "helo world"


@app.route('/verify-comments')
def verify():
    comments = request.args.get('comments')
    parsed_comments = json.loads(comments)
    clean_comments = really_long_machine_learning_thing(parsed_comments)
    return jsonify(clean_comments)


def really_long_machine_learning_thing(array_of_comments: list):
    array_of_comments.pop()
    return array_of_comments
