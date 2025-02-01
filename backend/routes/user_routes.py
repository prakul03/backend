from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_addresses_for_user, add_address_to_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    uid = data.get("uid")  # UID from Firebase Authentication
    mail = data.get("mail")  # Email instead of phone number

    if not uid or not mail:
        return jsonify({"error": "UID and mail are required"}), 400

    user = create_user(uid, mail)
    return 201


@user_bp.route('/<uid>', methods=['POST'])
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
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route('/<uid>/addresses', methods=['GET'])
def get_addresses(uid):
    # Retrieve all addresses for the given user
    addresses = get_addresses_for_user(uid)
    
    if addresses:
        return jsonify({
            "uid": uid, 
            "addresses": addresses
        }), 200
    else:
        return jsonify({"error": "No addresses found for this user"}), 201
