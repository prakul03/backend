from flask import Blueprint, request, jsonify
from services.user_service import create_user, add_address_to_user, get_addresses_for_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()    
    uid = data.get("uid")  #UID from Firebase Authentication
    name = data.get("name")
    email = data.get("email")
    if not uid or not name or not email:
        return jsonify({"error": "UID, name, and email are required"}), 400
    user = create_user(uid, name, email)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    }), 201

@user_bp.route('/user/<uid>/addresses', methods=['POST'])
def add_address(uid):
    data = request.get_json()
    address = data.get("address")
    
    if not address:
        return jsonify({"error": "Address is required"}), 400
    
    user_address = add_address_to_user(uid, address)
    
    if user_address:
        return jsonify({
            "uid": user_address.uid,
            "addresses": user_address.addresses
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/user/<uid>/addresses', methods=['GET'])
def get_addresses(uid):
    addresses = get_addresses_for_user(uid)
    
    if addresses:
        return jsonify({"uid": uid, "addresses": addresses}), 200
    else:
        return jsonify({"error": "No addresses found for this user"}), 404
