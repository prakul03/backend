from flask import Blueprint, request, jsonify
from services.user_service import create_user, add_address_to_user, get_addresses_for_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    uid = data.get("uid")  # UID from Firebase Authentication
    email = data.get("email")  # Email instead of phone number

    if not uid or not email:
        return jsonify({"error": "UID and email are required"}), 400

    user = create_user(uid, email)
    return jsonify({
        "uid": user.uid,
        "email": user.email,
        "created_at": user.created_at
    }), 201

@user_bp.route('/user/<uid>/addresses', methods=['POST'])
def add_address(uid):
    data = request.get_json()
    address = data.get("address")  # Expecting a JSON object for the address
    
    if not address:
        return jsonify({"error": "Address is required"}), 400
    
    user_address = add_address_to_user(uid, address)
    
    if user_address:
        return jsonify({
            "uid": user_address.uid,
            "addresses": user_address.addresses,
            "created_at": user_address.created_at
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/user/<uid>/addresses', methods=['GET'])
def get_addresses(uid):
    addresses = get_addresses_for_user(uid)
    
    if addresses:
        return jsonify({
            "uid": uid, 
            "addresses": addresses
        }), 200
    else:
        return jsonify({"error": "No addresses found for this user"}), 404
