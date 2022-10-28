from mcpi.connection import Connection
from mcpi.minecraft import Minecraft
from Crypto.PublicKey import RSA
import base64
from Crypto.Random import get_random_bytes
import time
mc = Minecraft.create()

def generate_private_and_public_Keys():
    Connection.generateKey()

def generate_AES_and_MAC_Keys():
    AESKey = base64.b64encode(get_random_bytes(16)).decode()
    # MAC key
    MACKey = base64.b64encode(get_random_bytes(24)).decode()
    # Save the keys on python side
    with open ("Minecraft_Tools\\MC_Py_API\\mcpi\\AESKey.pem", "w") as f:
        f.write(AESKey)

    with open ("Minecraft_Tools\\MC_Py_API\\mcpi\\MACKey.pem", "w") as f:
        f.write(MACKey)
    # join the keys together 
    data = AESKey + MACKey
    mc = Minecraft.create()
    mc.sendSymmetricKey(data)

def studentId():
    student_id = [
    "s3947359", #Zenabden
    "s3952670", #Duc
    "S3943775", #Sandrup
    "s3944263", #Matt

    ]

    result = ""
    for student in student_id:
        result += student[-2:]

    return result  



generate_private_and_public_Keys()
generate_AES_and_MAC_Keys()
time.sleep(1)
mc.postToChat(studentId())

