from flask import Blueprint, request, jsonify
from services.product_listing_service import create_product_listing, get_product_listings_by_product, get_product_listings_by_seller

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
    
    return jsonify({
        "listing_id": listing.listing_id,
        "product_id": listing.product_id,
        "seller_id": listing.seller_id,
        "price": listing.price,
        "quantity": listing.quantity,
        "shipping_cost": listing.shipping_cost,
        "status": listing.status,
        "location": listing.location,
        "created_at": listing.created_at
    }), 201

# Get product listings for a specific product
@product_listing_bp.route('/product-listings/<product_id>', methods=['GET'])
def get_listings_by_product(product_id):
    listings = get_product_listings_by_product(product_id)
    
    if not listings:
        return jsonify({"message": "No listings found for this product"}), 404
    
    listings_data = [
        {
            "listing_id": listing.listing_id,
            "price": listing.price,
            "quantity": listing.quantity,
            "shipping_cost": listing.shipping_cost,
            "status": listing.status,
            "location": listing.location,
            "created_at": listing.created_at
        }
        for listing in listings
    ]
    
    return jsonify(listings_data), 200

# Get product listings for a specific seller
@product_listing_bp.route('/seller-listings/<seller_id>', methods=['GET'])
def get_listings_by_seller(seller_id):
    listings = get_product_listings_by_seller(seller_id)
    
    if not listings:
        return jsonify({"message": "No listings found for this seller"}), 404
    
    listings_data = [
        {
            "listing_id": listing.listing_id,
            "product_id": listing.product_id,
            "price": listing.price,
            "quantity": listing.quantity,
            "shipping_cost": listing.shipping_cost,
            "status": listing.status,
            "location": listing.location,
            "created_at": listing.created_at
        }
        for listing in listings
    ]
    
    return jsonify(listings_data), 200
