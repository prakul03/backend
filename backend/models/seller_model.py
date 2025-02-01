from extensions import db
from datetime import datetime

class Seller(db.Model):
    __tablename__ = 'sellers'

    seller_id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Seller {self.name}>"
