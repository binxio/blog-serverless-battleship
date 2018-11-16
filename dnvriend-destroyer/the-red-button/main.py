# [START gae_python37_app]
import requests
from flask import Flask

app = Flask(__name__)

enabled = False
shots_fired = 0

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/red-button', methods=['GET'])
def red_button():
    global enabled
    enabled = True
    print('Enabling the big gun')
    return 'Enables the big-gun...'


@app.route('/shoot', methods=['GET'])
def shoot():
    global shots_fired
    print('Received order to shoot!')
    if enabled:
        for x in range(0, 1000):
            shots_fired += 1
            print(f'[{shots_fired}]: bang bang!')
            requests.post('https://europe-west1-speeltuin-dennis-vriend.cloudfunctions.net/dnvriend_destroyer', json={'shoot': True})
    else:
        print('Not enabled, not shooting...')
    return 'Someone pulled the trigger'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
