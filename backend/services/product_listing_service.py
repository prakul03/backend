from models.product_listing_model import ProductListing
from extensions import db

# Create a new product listing
def create_product_listing(product_id, seller_id, price, quantity, shipping_cost, status, location):
    listing = ProductListing(
        product_id=product_id,
        seller_id=seller_id,
        price=price,
        quantity=quantity,
        shipping_cost=shipping_cost,
        status=status,
        location=location
    )
    db.session.add(listing)
    db.session.commit()
    return listing

# Get product listings for a specific product
def get_product_listings_by_product(product_id):
    listings = ProductListing.query.filter_by(product_id=product_id).all()
    return listings

# Get product listings for a specific seller
def get_product_listings_by_seller(seller_id):
    listings = ProductListing.query.filter_by(seller_id=seller_id).all()
    return listings
