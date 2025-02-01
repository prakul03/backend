from models.product_model import Product

def get_products_by_category(category_id):
    # Retrieve products filtered by category_id
    products = Product.query.filter_by(category_id=category_id).all()
    
    # If no products are found, return an empty list
    if not products:
        return []

    # Return the list of products
    return products
