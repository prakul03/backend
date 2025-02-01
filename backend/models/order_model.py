from extensions import db
import uuid
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

# Order Model - Use UUID for order_id
class Order(db.Model):
    __tablename__ = 'orders'
    
    order_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(255), db.ForeignKey('users.uid'), nullable=False)
    total_amount = db.Column(db.Numeric(10,2), nullable=False)
    status = db.Column(db.String(50), default='pending', nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    order_details = db.Column(JSON, nullable=False)

# OrderItem Model - Use UUID for order_item_id
class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    order_item_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = db.Column(db.String(36), db.ForeignKey('orders.order_id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.String(36), db.ForeignKey('products.product_id'), nullable=False)
    seller_id = db.Column(db.String(255), db.ForeignKey('sellers.seller_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    item_details = db.Column(JSON, nullable=False)

# OrderHistory Model - Store history of orders placed by a user
class OrderHistory(db.Model):
    __tablename__ = 'order_history'
    
    history_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(255), db.ForeignKey('users.uid'), nullable=False)
    order_id = db.Column(db.String(36), db.ForeignKey('orders.order_id', ondelete="CASCADE"), nullable=False)
    items = db.Column(JSON, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# SellerOrder Model - Track orders for each seller
class SellerOrders(db.Model):
    __tablename__ = 'seller_orders'
    seller_order_id = db.Column(db.String, primary_key=True)
    seller_id = db.Column(db.String, db.ForeignKey('sellers.seller_id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.String, db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    total_amount = db.Column(db.Float, nullable=False)  # This should be filled in when creating the order
    status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)