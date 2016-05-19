from app import db

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    drink_name = db.Column(db.Integer, db.ForeignKey('drink.name'))
    gin = db.Column(db.integer)
    vodka = db.Column(db.integer)
    syrup = db.Column(db.integer)
    limejuice = db.Column(db.integer)
    bitters = db.Column(db.integer)
    vermouth = db.Column(db.integer)

    def __repr__(self):
        return '<Post %r>' % (self.body)
