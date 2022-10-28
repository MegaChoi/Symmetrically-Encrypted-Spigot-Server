from Crypto.PublicKey import RSA

keySize = 1024

key = RSA.generate(keySize)

privateKey = key.export_key('PEM', pkcs=8).decode('utf-8')
publicKey = key.publickey().export_key().decode('utf-8')

pv_key_string = key.exportKey()

with open ("private.pem", "w") as f:
    f.write(privateKey)

with open ("public.pem", "w") as f:
    f.write(publicKey)