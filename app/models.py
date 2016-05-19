#!flask/bin/python
from app import db

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(6400), index=True,)
    ingredients = db.relationship('Ingredients', backref='author', lazy='dynamic')
    
    def __init__(self, name, description):
        self.name = id
        self.name = name
        self.description = description

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    drink_name = db.Column(db.Integer, db.ForeignKey('drink.name'))
    gin = db.Column(db.Integer)
    vodka = db.Column(db.Integer)
    syrup = db.Column(db.Integer)
    limejuice = db.Column(db.Integer)
    bitters = db.Column(db.Integer)
    vermouth = db.Column(db.Integer)


def __init__(self, gin, vodka, syrup, limejuice, bitters, vermouth):
    self.name = gin
    self.name = vodka
    self.description = syrup
    self.description = limejuice
    self.description = bitters
    self.description = vermouth



