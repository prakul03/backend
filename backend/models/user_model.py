from datetime import datetime
from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    
    # Set `uid` as the primary key
    uid = db.Column(db.String(255), primary_key=True, nullable=False)  # Firebase UID (varchar equivalent)
    mail = db.Column(db.String(255), unique=True, nullable=False)  # Email (varchar equivalent)

    def __init__(self, uid, mail):
        print(f"Creating a new User object with UID: {uid}, Mail: {mail}")
        self.uid = uid
        self.mail = mail

    def __repr__(self):
        return f'<User {self.mail}>'

class UserAddress(db.Model):
    __tablename__ = 'user_addresses'

    id = db.Column(db.Integer, primary_key=True)  # New primary key
    uid = db.Column(db.String(255), db.ForeignKey('users.uid'), nullable=False)
    addresses = db.Column(db.JSON, default=[])

    user = db.relationship('User', backref=db.backref('user_addresses', lazy=True))

    def __init__(self, uid, addresses):
        self.uid = uid
        self.addresses = addresses

    def __repr__(self):
        return f'<UserAddress {self.uid}>'
