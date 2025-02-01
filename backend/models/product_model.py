from extensions import db
from uuid import uuid4
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    meta_tags = db.Column(db.JSON, nullable=True)  # Use JSON for storing meta_tags
    images = db.Column(db.JSON, nullable=True)  # Use JSON for storing image paths/URLs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product {self.name}>"