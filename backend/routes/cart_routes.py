from flask import Blueprint, request, jsonify
from services.cart_services import add_item_to_cart, update_item_quantity, remove_item_from_cart, get_cart_items
from models.product_model import Product  # Import the Product model

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart', methods=['POST'])
def add_to_cart():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    print(f"Received data for POST /cart: uid={uid}, product_listing_id={product_listing_id}, product_id={product_id}, quantity={quantity}")

    # Check for missing fields
    if not uid:
        print("Error: Missing 'uid'")
    if not product_listing_id:
        print("Error: Missing 'product_listing_id'")
    if not product_id:
        print("Error: Missing 'product_id'")
    if not quantity:
        print("Error: Missing 'quantity'")

    if not uid or not product_listing_id or not product_id or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    return add_item_to_cart(uid, product_listing_id, product_id, quantity)


@cart_blueprint.route('/cart', methods=['PUT'])
def update_cart_item():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')
    quantity = request.json.get('quantity')

    print(f"Received data for PUT /cart: uid={uid}, product_listing_id={product_listing_id}, quantity={quantity}")

    # Check for missing fields
    if not uid:
        print("Error: Missing 'uid'")
    if not product_listing_id:
        print("Error: Missing 'product_listing_id'")
    if not quantity:
        print("Error: Missing 'quantity'")

    if not uid or not product_listing_id or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    return update_item_quantity(uid, product_listing_id, quantity)


@cart_blueprint.route('/cart', methods=['DELETE'])
def remove_from_cart():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')

    print(f"Received data for DELETE /cart: uid={uid}, product_listing_id={product_listing_id}")

    # Check for missing fields
    if not uid:
        print("Error: Missing 'uid'")
    if not product_listing_id:
        print("Error: Missing 'product_listing_id'")

    if not uid or not product_listing_id:
        return jsonify({"error": "Missing required fields"}), 400

    return remove_item_from_cart(uid, product_listing_id)

# Serialize the Cart SQLAlchemy model instance and include product name
def serialize_cart(cart):
    # Query the product name using product_id
    product = Product.query.filter_by(uid=cart.product_id).first()
    product_name = product.name if product else "Unknown Product"  # Default to "Unknown Product" if not found

    return {
        'id': cart.id,
        'uid': cart.uid,
        'product_listing_id': cart.product_listing_id,
        'product_name': product_name,  # Include the product name
        'quantity': cart.quantity
    }

@cart_blueprint.route('/cart/<uid>', methods=['GET'])
def get_all_items(uid):
    cart_items = get_cart_items(uid)  # Assuming this returns a list of Cart objects

    if not cart_items:
        return jsonify({"message": "No items in cart"}), 404

    cart_items_data = [serialize_cart(item) for item in cart_items]

    return jsonify(cart_items_data)
