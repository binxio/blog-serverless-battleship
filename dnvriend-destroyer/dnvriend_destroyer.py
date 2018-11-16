from flask import escape

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/0.12/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/0.12/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json()
    if request_json and 'name' in request_json:
        name = escape(request_json['name'])
    else:
        name = 'World'
    return 'Hello, {}!'.format(name)