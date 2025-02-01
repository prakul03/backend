from extensions import db
import uuid
from datetime import datetime

class ProductListing(db.Model):
    __tablename__ = 'product_listings'

    listing_id = db.Column(db.String(255), primary_key=True, default=str(uuid.uuid4()))  # Listing ID (UUID as String)
    product_id = db.Column(db.String(255), db.ForeignKey('products.uid'), nullable=False)  # Product ID (Foreign Key to Product)
    seller_id = db.Column(db.String(255), db.ForeignKey('sellers.seller_id'), nullable=False)  # Seller ID (Foreign Key to Seller)
    price = db.Column(db.Float, nullable=False)  # Price of the product
    quantity = db.Column(db.Integer, nullable=False)  # Quantity available
    shipping_cost = db.Column(db.Float, nullable=False)  # Shipping cost for the product
    status = db.Column(db.String(50), nullable=False)  # Status (e.g., active, sold out)
    location = db.Column(db.String(255), nullable=False)  # Location of the seller
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of the listing creation

    product = db.relationship('Product', backref=db.backref('product_listings', lazy=True))  # Relationship with Product
    seller = db.relationship('Seller', backref=db.backref('product_listings', lazy=True))  # Relationship with Seller

    def __init__(self, product_id, seller_id, price, quantity, shipping_cost, status, location):
        self.product_id = product_id
        self.seller_id = seller_id
        self.price = price
        self.quantity = quantity
        self.shipping_cost = shipping_cost
        self.status = status
        self.location = location

    def __repr__(self):
        return f'<ProductListing {self.listing_id}>'
