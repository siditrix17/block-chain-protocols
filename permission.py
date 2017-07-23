#permission check against block-chain
#checkpolicy(PK-ksig,Xp)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ecdsa import SigningKey
import base64
import hashlib
from Crypto import Random()
from Crypto.Cipher import AES

def encode(s):
  # s is the message to be parsed
 print"ENCODED string:",s.encode(encoding='base64',errors='strict')
 return s
 
def signpk():
 pk = SigningKey.generate(curve=ecdsa.SECP256k1)
 return pk_k
 #this is PK(ksig)

def hashing(pk):
  m = hashlib.sha256()
  m.update(pk)
  A_policy=m.digest()
  return A_policy

Xp=[]   #set of permission allowed by user

def CheckPolicy(pk_k,Xp):
 allow=0
 #to input list of permissions from user side 
 POLICYus=['location','contacts','phone_number']    #policy contains permission required 
 L=[]    #act as memory buffer
     #policies allowed by user
 sign=signpk()
 x=hashing(sign)
 L.append(x)
 if (L):
   parse=encode(x)
  if sign==pk or (sign==pk and Xp in POLICYus):
    allow=1
  else:
    exit(0)
 exit(0)

CheckPolicy()
