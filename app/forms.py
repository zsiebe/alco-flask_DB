from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from wtforms_components import IntegerField

class DrinkForm(Form):
    drink_name = StringField('drink name', validators=[DataRequired()])
    description = TextAreaField('description of drink', validators=[DataRequired()])
    vodka = BooleanField('Vodka')
    gin = BooleanField('Gin')
    rum = BooleanField('Rum')
    whisky = BooleanField('Whisky')


    vodka_recipe = IntegerField('drink name',default=0, validators=[NumberRange(
            min=0,
            max=10)]
                         )

