from pythonMC.mcpi.minecraft import Minecraft
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256, SHA1
import base64
import hmac
import hashlib


key1 = base64.b64encode(get_random_bytes(16)).decode()
# MAC key
key2 = base64.b64encode(get_random_bytes(24)).decode()
# join the keys together 
data = key1 + key2
mc = Minecraft.create()
mc.sendAESKey(data)
# mc.postToChat("thijmgtjkmtgkjtj the message")
