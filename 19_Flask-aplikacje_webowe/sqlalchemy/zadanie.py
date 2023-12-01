# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tagname


def get_tags(session):
    return session.query(Tag).all()


def create_tag(name, session):
     tag = Tag(tagname=name)
     session.add(tag)
     session.commit()


@app.route('/')
def hello():
    return render_template('form.html', data=get_tags(db.session),
                           tytul="Użytkownicy", no_error=True)


@app.route('/add')
def add():
    args = request.args
    no_error = create_tag(args["name"], db.session)
    if no_error:
        tytul = "Dodano Tag"
    else:
        tytul = "Taki Tag już istnieje"

    return render_template('form.html', data=get_tags(db.session),
                           no_error=no_error,
                           tytul=tytul)
