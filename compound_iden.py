#author:siditrix

from ecdsa import SigningKey
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import socket

def sigkey():# SECP256k1 is the Bitcoin elliptic curve
 print'public key :-'
 pk = SigningKey.generate(curve=ecdsa.SECP256k1)
 print pk
 print'signing key or verifing key:'
 sk = sk.get_verifying_key()
 print sk
 # Gsig=['sk','pk']

#this is a tuple of signature keys
#now for encryption part , sk will be used as Genc key

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]
def iv():
"""
"""
return chr(0) * 16
class AESCipher(object):
""

 def __init__(self, key):
 self.key = key
  #self.key = hashlib.sha256(key.encode()).digest()
 
 def encrypt(self, message):
 """
 It is assumed that you use Python 3.0+
 , so plaintext's type must be str type(== unicode).
 """
 message = message.encode()
 raw = pad(message)
 cipher = AES.new(self.key, AES.MODE_CBC, iv())
 enc = cipher.encrypt(raw)
 return base64.b64encode(enc).decode('utf-8')
 
 def decrypt(self, enc):
 enc = base64.b64decode(enc)
 cipher = AES.new(self.key, AES.MODE_CBC, iv())
 dec = cipher.decrypt(enc)
 return unpad(dec).decode('utf-8')

sigkey()
key=sk
message=input("enter message:")
enc = AESCipher(key).encrypt(message)
#for decryption use : dec= AESCipher(key).decrypt(_enc)

#u shares this info (public signing and verifying key with s)
# pk and sk

#s shares the pk and sk of s using the above same functions
#this part is for s and will be compiled by s separately , i have merged this part in one program but this will be over a channel 

def signkey():# SECP256k1 is the Bitcoin elliptic curve
 print'public key :-'
 pk2 = SigningKey.generate(curve=ecdsa.SECP256k1)
 print pk2
 print'signing key or verifing key:'
 sk2 = sk.get_verifying_key()
 print sk2
 # Gsig=['sk2','pk2']
signkey()

return pk,pk2,sk
exit(0)

