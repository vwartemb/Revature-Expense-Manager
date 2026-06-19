"""
Service layer: business logic only, no DB calls

* Does the password match?
Output should be: (1, "vanessa", "hashedpassword123", "employee")

"""
from dao.user_dao import find_user_by_username
import hashlib

def login(username, password):
    try:
        user = find_user_by_username(username)
        
        if user is None: # for "None" always use "is" 
            return None
        
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        
        if hashed_pass == user[2]:
            return user
        
    except Exception as e:
        print(f"Error logging the user in: {e}")
        return None