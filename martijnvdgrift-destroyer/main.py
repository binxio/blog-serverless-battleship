from flask import Flask, request, jsonify
import requests
import uuid
import logging
import time
import json

app = Flask(__name__)


def uuid_generator():
    return str(uuid.uuid4())


def timestamp_generator():
    return int(round(time.time() * 1000))


target_url = 'https://nqyg1t2wwh.execute-api.eu-west-1.amazonaws.com/api'


@app.route('/')
def hello_world():
    return 'Hello World!'


# todo: async call for requests, because its now waiting for a response.
@app.route('/shoot', methods=['GET', 'POST'])
def shoot():
    payload = {'timestamp': timestamp_generator(), 'uuid': uuid_generator(), 'name': 'martijn', 'state': 'ping'}
    requests.post(target_url, json=payload)
    return 'Shooting payload: ' + str(json.dumps(payload))


@app.route('/hit', methods=['POST'])
def hit():
    content = request.get_json()
    print('Got hot by: ' + str(content))
    json_data = {'timestamp': timestamp_generator(), 'uuid': uuid_generator(), 'name': 'martijn', 'state': 'pong'}
    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
