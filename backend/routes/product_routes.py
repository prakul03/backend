from flask import Blueprint, request, jsonify
from services.product_service import get_products_by_category

product_bp = Blueprint('product', __name__)

@product_bp.route('/category/<int:category_id>/products', methods=['GET'])
def get_products_by_category_route(category_id):
    # Call the service to get products by category
    products = get_products_by_category(category_id)
    
    if products:
        # Return product details including images in JSON format
        return jsonify([{
            'product_id': product.uid,
            'name': product.name,
            'description': product.description,
            'category_id': product.category_id,
            'images': product.images
        } for product in products]), 200
    else:
        return jsonify({"error": "No products found for this category"}), 404
