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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note_part2.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tagname

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note_title = db.Column(db.String(80),  nullable=False)
    note_content = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.note_title

def get_notes(session):
    return session.query(Note).all()

def create_note(note_title, session):                               #try -except oraz else jest do obsługi błędów, żeby nie dodało dwa razy tego samego imienia
         note = Note(note_title=note_title)
         session.add(note)
         session.commit()

def remove_note(note_id, session):
    note = session.query(Note).filter_by(id=note_id).one()
    session.delete(note)
    session.commit()

def get_tags(session):
    return session.query(Tag).all()

def create_tag(name, session):
    try:                                #try -except oraz else jest do obsługi błędów, żeby nie dodało dwa razy tego samego imienia
         tag = Tag(tagname=name)
         session.add(tag)
         session.commit()
    except sqlalchemy.exc.IntegrityError as e:
         print(e)
         session.rollback()
         return False
    else:
         return True

def remove_tag(name, session):
    tag = session.query(Tag).filter_by(tagname=name).one()
    session.delete(tag)
    session.commit()


@app.route('/')
def hello():
    return render_template('form_do_zadania.html', data=get_tags(db.session),
                           tytul="Użytkownicy", no_error=True)

@app.route('/add')
def add():
    args = request.args
    create_tag(args["tag"], db.session)

    return render_template('form_do_zadania.html', data=get_tags(db.session),
                           tytul="Dodano Tag")

@app.route('/remove')
def remove():
    args = request.args
    remove_tag(args["tag"], db.session)

    return render_template('form_do_zadania.html', data=get_tags(db.session),
                           tytul="Usunięto Tag")

@app.route('/add_note')
def add_note():
    args = request.args
    create_tag(args["note"], db.session)

    return render_template('form_do_zadania.html', data=get_notes(db.session),
                           tytul="Dodano notatke")

@app.route('/remove_note')
def remove_note():
    args = request.args
    remove_tag(args["note"], db.session)

    return render_template('form_do_zadania.html', data=get_notes(db.session),
                           tytul="Usunięto notatke")