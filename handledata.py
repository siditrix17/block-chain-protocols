#accessControlProtocol
from ecdsa import SigningKey
import base64
import hashlib
#from Crypto import Random()
#from Crypto.Cipher import AES

#pip install kademlia                              #this part is for implementing DHT  
#for implementing DHT :-
from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

# log to std out
class dht:

def quit(result):
    print "Key result:", result
    reactor.stop()

def get(result, server):
    return server.get("a key").addCallback(quit)

def done(found, server):
    log.msg("Found nodes: %s" % found)
    return server.set("a key", "a value").addCallback(get, server)

def server():
 log.startLogging(sys.stdout)
 server = Server()
 # next line, or use reactor.listenUDP(5678, server.protocol)
 server.listen(5678)
 server.bootstrap([('127.0.0.1', 1234)]).addCallback(done, server)
 reactor.run()


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

def handledataTx(pk_k,m):                      #main function
 rw=1
 c,Xp,rw=encode(m)
 if (CheckPolicy(pk,Xp))==True: 
  x=hashing(pk)
   L=L.append(x)
   pk,pk2,POLICYus=encode(x)
 Axp=hashing(pk or Xp)
 if (rw=0):
   Hc=hashing(c)
   L=L.append(Axp)
   L=L.append(Hc)
   d=dht()
   d.get(Hc,server)=c
   return Hc
 elif (c in L):
   return d.quit(result)

handledataTX()

