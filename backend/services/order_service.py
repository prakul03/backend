from extensions import db
from models.order_model import Order, OrderItem, OrderHistory, SellerOrders
from models.product_listing_model import ProductListing
import uuid

def create_order(user_id, items):
    total_amount = 0  # Initialize total amount

    # Loop through the items and calculate the total amount
    for item in items:
        total_amount += item["quantity"] * item["price"]

    # Insert the order into the 'orders' table
    order = Order(user_id=user_id, total_amount=total_amount, status='pending')
    db.session.add(order)
    db.session.commit()

    # Now we can create individual seller orders for each item
    for item in items:
        seller_order = SellerOrders(
            seller_order_id=str(uuid.uuid4()),  # Generate a new unique seller order ID
            seller_id=item["seller_id"],
            order_id=order.order_id,  # Link the seller order to the created order
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"],  # Price of the item
            total_amount=item["quantity"] * item["price"],  # Calculating total for the item
            status='pending'
        )
        db.session.add(seller_order)

    # Commit the session to save all the changes
    db.session.commit()

    return order
