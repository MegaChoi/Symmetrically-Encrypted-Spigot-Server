import socket
import select
import sys
from .util import flatten_parameters_to_bytestring
import json
from Crypto.Signature import pss
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256, SHA1
from Crypto.PublicKey import RSA
""" @author: Aron Nieminen, Mojang AB"""
import base64
import hmac
import hashlib
class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"
    def generateKey():
            key = RSA.generate(1024)
            privateKey = key.export_key('PEM', pkcs=8).decode('utf-8')
            publicKey = key.publickey().export_key().decode('utf-8')
            pv_key_string = key.exportKey()

            with open ("Minecraft_Tools\\server\\privateKey.pem", "w") as f:
                f.write(privateKey)

            with open ("Minecraft_Tools\\MC_Py_API\\mcpi\\publicKey.pem", "w") as f:
                f.write(publicKey)
    
    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""

    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def send(self, f, *data):
        """
        Sends data. Note that a trailing newline '\n' is added here
        The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
        which is mildly distressing as it can't encode all of Unicode.
        """
        # these keys can be generated randomly

        iv = "jvHJ1XFt0IXBrxxx"
        if f == b"send.key":
            keys = "".join(data).encode("UTF-8")
            public_key = RSA.import_key(open("Minecraft_Tools\\MC_Py_API\\mcpi\\publicKey.pem").read())
            cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256, mgfunc=lambda x,y: pss.MGF1(x,y, SHA1))
            AESkeys = cipher.encrypt(keys)
            # print(base64.b64encode(AESkeys).decode())
            s = b"".join([f, b"(", base64.b64encode(AESkeys), b")", b"\n"])
            
        # if command == postToChat then encrypt data
        elif f == b"chat.post":
            # read keys from files
            g = open('Minecraft_Tools\\MC_Py_API\\mcpi\\AESKey.pem','r')
            key1 = g.read()
            g.close()
            g = open('Minecraft_Tools\\MC_Py_API\\mcpi\\MACKey.pem','r')
            key2 = g.read()
            g.close()
            
            # STATION 1: turn the message into bytes
            block_size = AES.block_size
            message = ''.join(data)
            
            # convert string to bytes in UTF-8 format
            message_in_bytes = message.encode('UTF-8')
            # pad the plaintext 
            message_in_bytes = pad(message_in_bytes, block_size)

            # STATION 2: encrypt the message
            # ciphertext
            encryption_object = AES.new(key1.encode("UTF-8"), AES.MODE_CBC, iv.encode("UTF-8"))
            ciphertext_in_bytes = encryption_object.encrypt(message_in_bytes)

            # ciphertext in string format
            string_ciphertext = base64.b64encode(ciphertext_in_bytes)
            # print('Encrypted Text: ' + string_ciphertext.decode('UTF-8'))

            # STATION 3: MAC the ciphertext
            MAC = hmac.new(key2.encode("UTF-8"), string_ciphertext, hashlib.sha256).digest()
            digest = base64.b64encode(MAC)
            # s = b"".join([f, b"(", ciphertext_in_bytes, MAC, b")", b"\n"])
            s = b"".join([f, b"(", string_ciphertext, b")", digest, b"\n"])



        self._send(s)
    
    def _send(self, s):
        """
        The actual socket interaction from self.send, extracted for easier mocking
        and testing
        """
        print(s)
        self.drain()
        self.lastSent = s

        self.socket.sendall(s)

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()