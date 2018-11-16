import json
import random
import time
import uuid

import requests
from flask import jsonify

targets = {
    'thijs': 'https://nqyg1t2wwh.execute-api.eu-west-1.amazonaws.com/api',
    'martijn': 'https://speeltuin-martijn-vd-grift.appspot.com/hit'
}


def get_bullet(uuid: str, timestamp: int) -> dict:
    return {
        "timestamp": timestamp,
        "uuid": uuid,
        "name": "dennisvriend",
        "state": "ping"
    }


def get_uuid() -> str:
    return str(uuid.uuid4())


def get_timestamp():
    return int(round(time.time() * 1000))


def shoot_at(target: str) -> None:
    uuid = get_uuid()
    timestamp = get_timestamp()
    print(f'[SHOOT_AT:{target}]:dennisvriend,{uuid},{timestamp}')
    requests.post(targets.get(target), json=get_bullet(get_uuid(), get_timestamp()))


def shoot():
    "shoot at a random target"
    if bool(random.getrandbits(1)):
        shoot_at('thijs')
    else:
        shoot_at('martijn')


def dnvriend_destroyer(request):
    try:
        got_hit_with_bullet = {}
        if request.get_json().get('shoot'):
            shoot()
        else:
            got_hit_with_bullet = request.get_json()
            got_hit_with_bullet.update({'state': 'pong'})
            received_payload = json.dumps(got_hit_with_bullet)
            timestamp = get_timestamp()
            uuid = got_hit_with_bullet['uuid']
            name = got_hit_with_bullet['name']
            print(f'[GOT_HIT_BY:{name}]:{name},{uuid},{timestamp},{received_payload}')
        return jsonify(got_hit_with_bullet), 200
    except Exception as e:
        print(f'Error: e')
        return jsonify({
            'error': str(e),
            'usage': 'please post a message with a valid body'
        }), 500
