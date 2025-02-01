from extensions import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(255), unique=True, nullable=False)  # Firebase UID (varchar equivalent)
    name = db.Column(db.String(255), nullable=False)  # Name (varchar equivalent)
    email = db.Column(db.String(255), unique=True, nullable=False)  # Email (varchar equivalent)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Created At timestamp

    def __init__(self, uid, name, email):
        print(f"Creating a new User object with UID: {uid}, Name: {name}, Email: {email}")
        self.uid = uid
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name}>'
    

class UserAddress(db.Model):
    __tablename__ = 'user_addresses'

    uid = db.Column(db.String(255), db.ForeignKey('users.uid'), primary_key=True)
    addresses = db.Column(db.JSON, default=[])

    user = db.relationship('User', backref=db.backref('user_addresses', lazy=True))

    def __init__(self, uid, addresses):
        self.uid = uid
        self.addresses = addresses

    def __repr__(self):
        return f'<UserAddress {self.uid}>'
