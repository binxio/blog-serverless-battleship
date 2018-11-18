from chalice import Chalice

app = Chalice(app_name='pong')


@app.route('/',methods=['GET', 'POST'])
def index():
    return { 'pong': app.current_request.json_body }


