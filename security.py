import hashlib
import os

def secure_hash(password: str):
    salt = os.getenv("APP_SALT", "default_salt")
    return hashlib.sha256((password + salt).encode()).hexdigest()
