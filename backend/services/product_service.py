# product_service.py (Assumed logic to create products and product listings)
from models.product_model import Product
from extensions import db

def create_product(name, description, category, meta_tags=None, images=None):
    product = Product(
        name=name,
        description=description,
        category=category,
        meta_tags=meta_tags,
        images=images
    )
    db.session.add(product)
    db.session.commit()
    return product

def get_product_by_id(product_id):
    return Product.query.filter_by(product_id=product_id).first()

def get_all_products():
    return Product.query.all()
