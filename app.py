from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import make_response
import json

app = Flask(__name__)


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(request.form.items())
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, host='0.0.0.0', port=8000)