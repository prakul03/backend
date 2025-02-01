from models.user_model import User, UserAddress
from extensions import db

def create_user(uid, mail):
    print(f"Service: Creating user with UID={uid}, Mail={mail}")
    
    # Create a new user instance
    new_user = User(uid=uid, mail=mail)
    
    print(f"Service: User object created: {new_user}")
    
    # Add to the database and commit
    db.session.add(new_user)
    db.session.commit()
    
    print(f"Service: User saved to database with ID={new_user.uid}")
    
    return new_user

def add_address_to_user(uid, address):
    user = User.query.filter_by(uid=uid).first()
    
    if not user:
        print(f"Service: User not found with UID={uid}")
        return None
    
    # Always create a new UserAddress record each time
    user_address = UserAddress(uid=uid, addresses=[address])
    
    # Add the new address record to the database
    db.session.add(user_address)
    
    # Commit changes to the database
    db.session.commit()
    
    print(f"Service: New address added for user with UID={uid}")
    
    return user_address


def get_addresses_for_user(uid):
    # Query all UserAddress entries with the same UID
    user_addresses = UserAddress.query.filter_by(uid=uid).all()  # Use .all() to get all matching entries
    
    addresses = []
    
    # Iterate over each UserAddress and add the addresses to the list
    for user_address in user_addresses:
        # Flatten the list of addresses
        addresses.extend(user_address.addresses)  # This will merge all addresses into a single list

    return addresses  # Return all addresses