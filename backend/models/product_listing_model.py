from extensions import db
from uuid import uuid4
from datetime import datetime

class ProductListing(db.Model):
    __tablename__ = 'product_listings'

    listing_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    product_id = db.Column(db.String(36), db.ForeignKey('products.product_id'), nullable=False)
    seller_id = db.Column(db.String(36), nullable=False)  # Firebase UID as seller ID
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shipping_cost = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)  # Shipping location of the seller
    status = db.Column(db.String(50), default='active')  # Active or out of stock
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', backref='product_listings', lazy=True)

    def __repr__(self):
        return f"<ProductListing product_id={self.product_id} seller_id={self.seller_id}>"
