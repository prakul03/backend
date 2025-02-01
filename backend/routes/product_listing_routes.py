from flask import Blueprint, request, jsonify
from services.product_listing_service import create_product_listing, get_product_listings_by_product_id

product_listing_bp = Blueprint('product_listing_bp', __name__)

# Route to create a product listing
@product_listing_bp.route('/product_listing', methods=['POST'])
def add_product_listing():
    data = request.get_json()
    product_id = data.get('product_id')
    seller_id = data.get('seller_id')
    price = data.get('price')
    quantity = data.get('quantity')
    shipping_cost = data.get('shipping_cost')
    location = data.get('location')

    try:
        # Create product listing
        listing = create_product_listing(product_id, seller_id, price, quantity, shipping_cost, location)
        return jsonify({'message': 'Product Listing created', 'listing_id': listing.listing_id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error creating product listing'}), 500

# Route to get all listings for a product
@product_listing_bp.route('/product/<product_id>/listings', methods=['GET'])
def get_product_listings(product_id):
    listings = get_product_listings_by_product_id(product_id)
    if not listings:
        return jsonify({'message': 'No listings found for this product'}), 404
    return jsonify([{
        'listing_id': l.listing_id,
        'seller_id': l.seller_id,
        'price': l.price,
        'quantity': l.quantity,
        'location': l.location,
        'status': l.status,
        'created_at': l.created_at.isoformat()
    } for l in listings])
