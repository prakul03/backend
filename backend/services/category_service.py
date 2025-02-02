from models.category_model import Category
from extensions import db

def get_all_categories():
    categories = Category.query.all()

    if categories:
        category_data = []
        for category in categories:
            category_data.append({
                'id': category.category_id,
                'name': category.category_name,  # Ensure category_name is being used
                'image_url': category.image_url
            })
        return category_data
    else:
        return []
