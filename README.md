# REST API example application

This is a solution for a lab displaying basic functionality of Flask API & requests package for Alta3 Research Python Certification

The project consists of 2 `.py` files.

`alta3research-flask01.py` is a minimal Flask configuration for GET endpoints such as:
`/`,
`/hello/<name>`

The responses are json encoded.

`alta3research-requests02.py` runs a simplistic get request to the [Open Notify API]("http://api.open-notify.org/") displaying Astros

## Prerequisites

Application uses [Python](https://www.python.org/) 3.x.x and [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [requests](https://requests.readthedocs.io/en/master/), these need to be installed additionally by following commands.

    python3 -m pip install requests
    python3 -m pip install flask

## Run the Flask app

    python3 alta3research-flask01.py

# REST API

The REST API to the example app is described below.

## Get list of Books

### Request

`GET /`

    curl http://localhost:5000/

### Response

Content represented in `books.json`

## Get key-value json with dynamic string

### Request

`GET /hello/<name>`

    curl http://localhost:5000/hello/<name>

### Response

    {"name":<name>}

## Run the Requests app

    python3 alta3research-requests02.py

### Response

Application returns a list of astros from the [Open Notify API](http://api.open-notify.org/) and displays it to the console.
