from . import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        hashed_pw = bcrypt.generate_password_hash(password)
        self.password = hashed_pw
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password,password)