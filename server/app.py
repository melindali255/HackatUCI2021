from flask import Flask
from flask import jsonify
from flask import request
import json
from textblob import TextBlob
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
    for i in range(len(array) - 1, -1, -1):
        polarity = TextBlob(array_of_comments[i]).sentiment.polarity
        if polarity < 0:
            array_of_comments.pop()

    return array_of_comments
