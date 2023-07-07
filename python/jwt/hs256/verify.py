#!/usr/bin/env python3

import jwt

CODE="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjp7InN1YiI6MTIzNDU2LCJuYW1lIjoiSnVzdGluIE92ZW5zIiwiZW1haWwiOiJqb3ZlbnNAZ290dW5peC5uZXQiLCJyb2xlIjoiYWRtaW4ifX0.ouhwjObrk1vlYcJcpz628zZB4FIq1GsgVW_NK-VIiVY"
SECRET="FmF3tqfru1WAGN1KiRezTOZ2YQwEZS6QIVpl1En4orCJS293B69shnsDNve6xUoTHdQNuZGU5cykn3MbeMKwCrt00IIiJAWgHz8WXlqXk7vfJod0cYCzLPdxgBLfKDth"

#header = CODE.split(".")
#print(header[0])

header = jwt.get_unverified_header(CODE)
alg = header["alg"]
decode = jwt.decode(CODE, SECRET, algorithms=alg)
print(decode)
