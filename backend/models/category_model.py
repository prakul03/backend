from extensions import db

class Category(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True)  # Category ID
    category_name = db.Column(db.String(255), nullable=False)  # Category Name
    image_url = db.Column(db.String(255))  # Category Image URL

    def __init__(self, category_name, image_url=None):
        self.category_name = category_name
        self.image_url = image_url

    def __repr__(self):
        return f'<Category {self.category_name}>'
