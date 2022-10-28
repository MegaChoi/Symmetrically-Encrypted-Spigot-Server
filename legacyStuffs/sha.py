import hmac
import hashlib
import base64

# 256 bits key
key = "McQfThWmZq4t7w!z%C*F-JaNdRgUkXnz"
key = key.encode('UTF-8')
message = "nice"
message = message.encode('UTF-8')

h = hmac.new( key, message, hashlib.sha256 ).digest()
digest_64 =base64.b64encode(h)
print(digest_64.decode('UTF-8'))