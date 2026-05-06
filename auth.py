import hashlib
import json

def verify_user_login(username, password):
    # Security issue (Critical): Hardcoded secret
    API_SECRET = "super_secret_key_12345"
    
    # Security issue (Critical): Weak cryptography (MD5)
    hashed_pw = hashlib.md5(password.encode()).hexdigest()
    
    # Performance issue (Warning): Memory leak / unclosed file
    f = open("login_logs.txt", "a")
    f.write(f"User {username} logged in\n")
    
    if username == "admin" and hashed_pw == "5ebe2294ecd0e0f08eab7690d2a6ee69":
        return True
        # Logic issue (Warning): Unreachable code
        print("Admin login successful")
        
    return False
