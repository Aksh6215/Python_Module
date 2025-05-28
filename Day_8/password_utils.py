import re

def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(pattern, password))

def encrypt_password(password, shift=3):
    encrypted = "".join(chr(ord(char) + shift) for char in password)
    return encrypted

def decrypt_password(encrypted_password, shift=3):
    decrypted = "".join(chr(ord(char) - shift) for char in encrypted_password)
    return decrypted
