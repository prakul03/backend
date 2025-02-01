from flask import Blueprint, request, jsonify
from services.order_service import create_order
from models.order_model import Order, OrderItem, OrderHistory, SellerOrders
from extensions import db

order_bp = Blueprint('order_bp', __name__)


order_bp.route('/place_order', methods=['POST'])
def place_order():
    user_id = request.json["user_id"]  # Get user ID from request
    items = request.json["items"]  # Get items from request
    
    # Call create_order function and get the created order
    order = create_order(user_id, items)
    
    # Return the order data as a response
    return jsonify({"order_id": order.order_id, "total_amount": order.total_amount}), 201

@order_bp.route('/orders/<user_id>', methods=['GET'])
def get_user_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    order_list = [
        {"order_id": order.order_id, "total_amount": str(order.total_amount), "status": order.status, "created_at": order.created_at}
        for order in orders
    ]
    return jsonify(order_list)

@order_bp.route('/seller_orders/<seller_id>', methods=['GET'])
def get_seller_orders(seller_id):
    seller_orders = SellerOrders.query.filter_by(seller_id=seller_id).all()
    order_list = [
        {"order_id": order.order_id, "product_id": order.product_id, "quantity": order.quantity, "status": order.status}
        for order in seller_orders
    ]
    return jsonify(order_list)
