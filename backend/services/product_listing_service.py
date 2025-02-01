from models.product_listing_model import ProductListing
from models.product_model import Product  # Make sure Product model exists for validation
from extensions import db
from sqlalchemy.orm.exc import NoResultFound

def create_product_listing(product_id, seller_id, price, quantity, shipping_cost, location):
    # Check if the product_id exists in the products table
    try:
        product = Product.query.filter_by(product_id=product_id).one()  # Ensure product exists
    except NoResultFound:
        raise ValueError(f"Product with ID {product_id} does not exist.")

    # Create a new product listing
    listing = ProductListing(
        product_id=product_id,
        seller_id=seller_id,
        price=price,
        quantity=quantity,
        shipping_cost=shipping_cost,
        location=location
    )

    try:
        db.session.add(listing)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating product listing: {str(e)}")

    return listing

def get_product_listings_by_product_id(product_id):
    # Get all listings for a given product_id, no changes needed for multiple sellers
    return ProductListing.query.filter_by(product_id=product_id).all()
