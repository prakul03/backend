from models.seller_model import Seller
from extensions import db

def create_seller(seller_id, name,email):
    seller = Seller(
        seller_id=seller_id,
        name=name,
        email=email
    )
    db.session.add(seller)
    db.session.commit()
    return seller

def get_seller_by_id(seller_id):
    return Seller.query.filter_by(seller_id=seller_id).first()
