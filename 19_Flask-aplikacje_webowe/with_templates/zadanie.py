# flask --app zadanie run
#
from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('form.html', data=data, tytul='Cześć' + [name])




@app.route('/show')
def add():
    args = request.args
    print(args)
    data.append(args["name"])

    return render_template('form.html', data=data, tytul='Dodano do listy')

