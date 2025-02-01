from flask import Blueprint, request, jsonify
from services.product_service import create_product, get_product_by_id, get_all_products

product_bp = Blueprint('product_bp', __name__)

# Route to create a product
@product_bp.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    category = data.get('category')
    meta_tags = data.get('meta_tags')
    images = data.get('images')
    
    product = create_product(name, description, category, meta_tags, images)
    return jsonify({'message': 'Product created', 'product_id': product.product_id}), 201

# Route to get product by ID
@product_bp.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'product_id': product.product_id, 'name': product.name, 'description': product.description, 'category': product.category, 'meta_tags': product.meta_tags, 'images': product.images})

# Route to get all products
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify([{'product_id': p.product_id, 'name': p.name, 'category': p.category} for p in products])
