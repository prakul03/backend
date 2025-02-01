from flask import Blueprint, jsonify
from services.category_service import get_all_categories

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def fetch_all_categories():
    categories = get_all_categories()

    if categories:
        return jsonify({"categories": categories}), 200
    else:
        return jsonify({"message": "No categories found"}), 404
