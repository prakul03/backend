from models.user_model import User, UserAddress
from extensions import db

def create_user(uid, name, email):
    print(f"Service: Creating user with UID={uid}, Name={name}, Email={email}")
    
    # Create new user instance
    new_user = User(uid=uid, name=name, email=email)
    
    print(f"Service: User object created: {new_user}")
    
    # Add to the database
    db.session.add(new_user)
    db.session.commit()
    
    print(f"Service: User saved to database with ID={new_user.id}")
    
    return new_user

def add_address_to_user(uid, address):
    user = User.query.filter_by(uid=uid).first()
    
    if not user:
        print(f"Service: User not found with UID={uid}")
        return None
    
    user_address = UserAddress.query.filter_by(uid=uid).first()

    if not user_address:
        user_address = UserAddress(uid=uid, addresses=[address])
    else:
        user_address.addresses.append(address)
    
    db.session.add(user_address)
    db.session.commit()
    
    print(f"Service: Address added for user with UID={uid}")
    
    return user_address

def get_addresses_for_user(uid):
    user_address = UserAddress.query.filter_by(uid=uid).first()
    
    if user_address:
        return user_address.addresses
    else:
        return []  # Return empty list if no addresses are found
