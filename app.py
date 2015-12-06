from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
from flask import make_response
import json
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = "ieuwnbcierubnv9p34n98c43hpc982n89cbnp9q2h3!$#@#@$"


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/options')
def options():
    return render_template('options.html', options=DEFAULTS)


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    flash("Looking good!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(request.form.items())
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, host='0.0.0.0', port=8000)