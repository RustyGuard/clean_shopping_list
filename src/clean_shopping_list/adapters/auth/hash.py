import base64
import hashlib

import bcrypt


def hash_password(password: str, password_secret: str) -> bytes:
    return bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.encode()).digest()), password_secret.encode('utf-8'))
