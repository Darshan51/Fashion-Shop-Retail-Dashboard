from db import db


class UserModel(db.Model):
    # Define the table for in regard of SQLALCHEMY
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(70))
    lastname = db.Column(db.String(70))
    username = db.Column(db.String(70))
    password = db.Column(db.String(70))

    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        #   SELECT * FROM users WHERE username = ?
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
