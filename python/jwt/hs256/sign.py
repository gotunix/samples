#!/usr/bin/env python3
import jwt
from datetime import datetime, timedelta, timezone


header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "sub": 123456,
    "name": "Justin Ovens",
    "email": "jovens@gotunix.net",
    "role": "admin"
}

SIGNING_KEY = "FmF3tqfru1WAGN1KiRezTOZ2YQwEZS6QIVpl1En4orCJS293B69shnsDNve6xUoTHdQNuZGU5cykn3MbeMKwCrt00IIiJAWgHz8WXlqXk7vfJod0cYCzLPdxgBLfKDth"

encoded = jwt.encode({'payload': payload}, SIGNING_KEY, algorithm="HS256")
print(encoded)
