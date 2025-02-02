from extensions import db
from models.cart_model import Cart
from models.product_listing_model import ProductListing  # Import the product listing model

# Add item to cart
def add_item_to_cart(uid, product_listing_id, product_id, quantity):
    # Check if the product listing exists and has enough quantity
    product_listing = ProductListing.query.filter_by(listing_id=product_listing_id).first()
    if not product_listing:
        return {"error": "Product listing not found"}, 404

    if quantity > product_listing.quantity:
        return {"error": "Not enough stock available"}, 400

    # Add item to cart
    cart_item = Cart(uid=uid, product_listing_id=product_listing_id, product_id=product_id, quantity=quantity)
    db.session.add(cart_item)

    # Update the product listing's stock
    product_listing.quantity -= quantity
    db.session.commit()

    return {"message": "Item added to cart"}, 200


# Update item quantity in cart
def update_item_quantity(uid, product_listing_id, quantity):
    # Get the cart item
    cart_item = Cart.query.filter_by(uid=uid, product_listing_id=product_listing_id).first()
    if not cart_item:
        return {"error": "Cart item not found"}, 404

    # Get the corresponding product listing
    product_listing = ProductListing.query.filter_by(listing_id=product_listing_id).first()
    
    if not product_listing:
        return {"error": "Product listing not found"}, 404

    # Check if we can update quantity without exceeding the stock limit
    if quantity > product_listing.quantity + cart_item.quantity:
        return {"error": "Not enough stock available"}, 400

    # Update the cart item quantity
    cart_item.quantity = quantity
    product_listing.quantity -= (quantity - cart_item.quantity)  # Adjust stock after updating the quantity
    db.session.commit()

    return {"message": "Cart item updated"}, 200


# Remove item from cart
def remove_item_from_cart(uid, product_listing_id):
    # Find the cart item
    cart_item = Cart.query.filter_by(uid=uid, product_listing_id=product_listing_id).first()
    if not cart_item:
        return {"error": "Cart item not found"}, 404

    # Find the corresponding product listing and update stock
    product_listing = ProductListing.query.filter_by(listing_id=product_listing_id).first()
    product_listing.quantity += cart_item.quantity  # Return the stock to the product listing

    # Remove the item from the cart
    db.session.delete(cart_item)
    db.session.commit()

    return {"message": "Item removed from cart"}, 200

def get_cart_items(uid):
    # Assuming you're querying the database for cart items
    return Cart.query.filter_by(uid=uid).all()
