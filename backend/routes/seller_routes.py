from flask import Blueprint, request, jsonify
from services.seller_service import create_seller, get_seller_by_id

seller_bp = Blueprint('seller_bp', __name__)

# Route to create a seller
@seller_bp.route('/seller', methods=['POST'])
def add_seller():
    data = request.get_json()
    seller_id = data.get('seller_id')  # Firebase UID
    name = data.get('name')
    contact_email = data.get('contact_email')
    
    seller = create_seller(seller_id, name, contact_email)
    return jsonify({'message': 'Seller created', 'seller_id': seller.seller_id}), 201

# Route to get seller by ID
@seller_bp.route('/seller/<seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = get_seller_by_id(seller_id)
    if not seller:
        return jsonify({'message': 'Seller not found'}), 404
    return jsonify({'seller_id': seller.seller_id, 'name': seller.name, 'contact_email': seller.contact_email})
