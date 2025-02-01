# In app.py

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from extensions import db
from config import Config
from routes.user_routes import user_bp as user_routes
from routes.product_routes import product_bp
from routes.product_listing_routes import product_listing_bp
from routes.seller_routes import seller_bp
from routes.order_routes import order_bp

# Initialize Flask app
app = Flask(__name__)

# Allow cross-origin requests (from localhost:3000)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Load the configuration from config.py
app.config.from_object(Config)

# Initialize db
db.init_app(app)

# Register Blueprints with URL prefixes
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(product_listing_bp, url_prefix='/product_listings')
app.register_blueprint(seller_bp, url_prefix='/sellers')

# Handle OPTIONS requests for CORS preflight
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

if __name__ == '__main__':
    app.run(debug=True)
