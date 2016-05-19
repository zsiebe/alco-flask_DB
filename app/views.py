from flask import Flask
from flask import render_template, flash, redirect
from app import models
from forms import DrinkForm
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')
db = SQLAlchemy(app)



@app.route('/')
def show_index():
    return render_template('index.html',
                            title='FUCK YOU TITLE', drinks = models.Drink.query.all())


@app.route('/see_drink/<drink>')
def see_drink(drink):
    return render_template('drink.html',
                           title='FUCK YOU TITLE', drinks=models.Drink.query.get(drink))


@app.route('/make_drink/<drink>')
def make_drink(drink):
    return "making: " + drink


@app.route("/add_drink", methods=['GET', 'POST'])
def add_drink():
    form = DrinkForm()
    if form.validate_on_submit():
        flash("added drink with drink_name " + form.drink_name.data)
        d = models.Drink(name=str(form.drink_name.data), description=str(form.description.data))
        db.session.add(d)
        db.session.commit()
        return redirect('/')
    else:
        filename = None
        return render_template('form.html',
                           title='FUCK YOU TITLE',
                           form=form, filename=filename)



if __name__ == '__main__':
    app.run(debug=True)

