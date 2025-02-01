from flask import Blueprint, request, jsonify
from services.cart_services import add_item_to_cart, update_item_quantity, remove_item_from_cart

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart', methods=['POST'])
def add_to_cart():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    if not uid or not product_listing_id or not product_id or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    return add_item_to_cart(uid, product_listing_id, product_id, quantity)


@cart_blueprint.route('/cart', methods=['PUT'])
def update_cart_item():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')
    quantity = request.json.get('quantity')

    if not uid or not product_listing_id or not quantity:
        return jsonify({"error": "Missing required fields"}), 400

    return update_item_quantity(uid, product_listing_id, quantity)


@cart_blueprint.route('/cart', methods=['DELETE'])
def remove_from_cart():
    uid = request.headers.get('uid')
    product_listing_id = request.json.get('product_listing_id')

    if not uid or not product_listing_id:
        return jsonify({"error": "Missing required fields"}), 400

    return remove_item_from_cart(uid, product_listing_id)
