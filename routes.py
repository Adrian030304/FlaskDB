from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            name, age, job = request.form.values()
            new_person = Person(name=name, age=age, job=job)
            db.session.add(new_person)
            db.session.commit()
            people = Person.query.all()
            return render_template('index.html', people=people)
        else:
            people = Person.query.all()
            return render_template('index.html', people=people)
    
    @app.route('/delete/<pid>', methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        people = Person.query.all()
        return render_template('index.html', people=people )