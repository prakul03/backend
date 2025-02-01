from extensions import db

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String, nullable=False)
    product_listing_id = db.Column(db.String, nullable=False)
    product_id = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
