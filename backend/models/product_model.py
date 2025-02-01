from extensions import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    uid = db.Column(db.String(255), primary_key=True)  # Product ID (UID)
    name = db.Column(db.String(255), nullable=False)  # Product Name
    description = db.Column(db.Text)  # Product Description
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)  # Category ID (Foreign Key)
    meta_tags = db.Column(db.JSON)  # Meta Tags (JSONB format for flexibility)
    images = db.Column(db.JSON)  # Product Images (JSONB format)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for product creation

    category = db.relationship('Category', backref=db.backref('products', lazy=True))  # Relationship with Category

    def __init__(self, uid, name, description, category_id, meta_tags=None, images=None):
        self.uid = uid
        self.name = name
        self.description = description
        self.category_id = category_id
        self.meta_tags = meta_tags or []
        self.images = images or []

    def __repr__(self):
        return f'<Product {self.name}>'