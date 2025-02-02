from flask import Blueprint, request, jsonify
from services.product_listing_service import create_product_listing, get_product_listings_by_product, get_product_listings_by_seller
from models.seller_model import Seller
from extensions import db  # Ensure you import db for querying

product_listing_bp = Blueprint('product_listing', __name__)

# Create a new product listing
@product_listing_bp.route('/product-listings', methods=['POST'])
def create_listing():
    data = request.get_json()
    
    product_id = data.get("product_id")
    seller_id = data.get("seller_id")
    price = data.get("price")
    quantity = data.get("quantity")
    shipping_cost = data.get("shipping_cost")
    status = data.get("status")
    location = data.get("location")
    
    if not all([product_id, seller_id, price, quantity, shipping_cost, status, location]):
        return jsonify({"error": "All fields are required"}), 400
    
    listing = create_product_listing(product_id, seller_id, price, quantity, shipping_cost, status, location)

    # Fetch seller name from database
    seller = db.session.get(Seller, seller_id)  # Fetch seller object safely
    seller_name = seller.name if seller else "Unknown Seller"

    return jsonify({
        "listing_id": str(listing.listing_id),
        "product_id": str(listing.product_id),
        "seller_id": str(listing.seller_id),
        "seller_name": seller_name,
        "price": float(listing.price),
        "quantity": int(listing.quantity),
        "shipping_cost": float(listing.shipping_cost),
        "status": str(listing.status),
        "location": str(listing.location),
        "created_at": listing.created_at.isoformat()
    }), 201

# Get product listings for a specific product
@product_listing_bp.route('/product-listings/<product_id>', methods=['GET'])
def get_listings_by_product(product_id):
    listings = get_product_listings_by_product(product_id)
    
    if not listings:
        return jsonify({"message": "No listings found for this product"}), 404

    listings_data = []
    for listing in listings:
        seller = db.session.get(Seller, listing.seller_id)
        seller_name = seller.name if seller else "Unknown Seller"

        listings_data.append({
            "listing_id": str(listing.listing_id),
            "price": float(listing.price),
            "quantity": int(listing.quantity),
            "shipping_cost": float(listing.shipping_cost),
            "seller_id": str(listing.seller_id),
            "seller_name": seller_name,
            "status": str(listing.status),
            "location": str(listing.location),
            "created_at": listing.created_at.isoformat()
        }) 
    return jsonify(listings_data), 200

# Get product listings for a specific seller
@product_listing_bp.route('/seller-listings/<seller_id>', methods=['GET'])
def get_listings_by_seller(seller_id):
    listings = get_product_listings_by_seller(seller_id)
    
    if not listings:
        return jsonify({"message": "No listings found for this seller"}), 404

    seller = db.session.get(Seller, seller_id)
    seller_name = seller.name if seller else "Unknown Seller"

    listings_data = [
        {
            "listing_id": str(listing.listing_id),
            "product_id": str(listing.product_id),
            "price": float(listing.price),
            "quantity": int(listing.quantity),
            "shipping_cost": float(listing.shipping_cost),
            "status": str(listing.status),
            "location": str(listing.location),
            "seller_name": seller_name,
            "created_at": listing.created_at.isoformat()
        }
        for listing in listings
    ]
    
    return jsonify(listings_data), 200
