import bcrypt

def encrypt_password(password: str) -> str:
    salt = bcrypt.gensalt()
    encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return encrypted_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    stored_hash_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), stored_hash_bytes)