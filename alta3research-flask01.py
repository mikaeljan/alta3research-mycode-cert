#!/usr/bin/env python
# encoding: utf-8
import json
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    with open('books.json', encoding='UTF-8') as json_file:
        data = json.load(json_file)
        return jsonify(data)

@app.route("/hello/<name>", methods=['GET'])
def hello(name):
    resp = jsonify({"name": name})
    return resp

@app.errorhandler(HTTPException)
def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
