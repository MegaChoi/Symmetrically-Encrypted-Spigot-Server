import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256, SHA1
from Crypto.Signature import pss


data = "ezfdjsaklf;jsdlajfds;laj".encode("utf-8")
public_key = RSA.import_key(open("legacyStuffs\public.pem").read())
cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256, mgfunc=lambda x,y: pss.MGF1(x,y, SHA1))
ciphertext = cipher.encrypt(data)
print(base64.b64encode(ciphertext).decode())




# key = RSA.generate(1024)
# f = open('private.pem','wb')
# f.write(key.export_key('PEM', pkcs=8))
# f.close()

# publicKey = key.publickey().export_key()
# f = open('public.pem','wb')
# f.write(publicKey)
# f.close()
# f = open('AESkey.pem','r')
# print(type(f.read()))
# f.close()