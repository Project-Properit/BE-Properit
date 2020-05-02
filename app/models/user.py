from app.models import db


def save(new_object):
    db.session.add(new_object)
    db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    admin = db.Column(db.Boolean)
    email = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))


class LogoutToken(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(200), unique=True)
