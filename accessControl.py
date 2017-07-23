#accessControlProtocol
from ecdsa import SigningKey
import base64
import hashlib
#from Crypto import Random()
#from Crypto.Cipher import AES

def encode(s):
  # s is the message to be parsed
 #print"ENCODED string:",s.encode(encoding='base64',errors='strict')
 return s
 
def signpk():
 pk_k = SigningKey.generate(curve=ecdsa.SECP256k1)
 return pk_k #this is PK(ksig)

def hashing(pk):
  m = hashlib.sha256()
  m.update(pk)
  return m.digest()

pk, pk2, sk = signkey()
POLICY_us = CheckPolicy()
L = []
pk_k = signpk()
hashed = hashing(pk_k)
L.append(hashed)

def handleAccessTX(pk_k, message):
	allow = 0
	parsed = encode(message)
	if pk_k == pk_us:
		L[hashed] = message
		allow = 1
	return allow
