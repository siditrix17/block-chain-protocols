import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

sid_enc=raw_input("enter the text to encrypt:")
random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

print'printing the key:',key  #key value

publickey = key.publickey() # pub key export for exchange
print'printing publickey:',publickey  #publickey

encrypted = publickey.encrypt(sid_enc, 24)
#message to encrypt is in the above line 

print 'encrypted message:', encrypted #ciphertext


#decrypted code below



decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print 'decrypted:', decrypted

