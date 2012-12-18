from Crypto.PublicKey import RSA
import os
import base64

from minerva.common.constants import RSA_KEYSIZE

def generate_RSA_keypair():
    return RSA.generate(RSA_KEYSIZE, os.urandom)
 
def generate_public_key(mod, exp):
    rsa_key = RSA.construct((long(mod), long(exp)))
    return rsa_key.publickey()  
    
def get_public_key(private):
    return private.publickey()

def _rsa_decrypt(key, message):
    return key.decrypt(message)

def _rsa_decrypt_and_decode(key, message):
    return key.decrypt(base64.b64decode(message))

def _rsa_encrypt(key, message):
    return key.encrypt(message, 32)[0]

def _rsa_encrypt_and_encode(key, message):
    return base64.b64encode(key.encrypt(message, 32)[0])
  
def rsa_encrypt_client(client, message):
    public_key = generate_public_key(client.public_key.mod,
                                    client.public_key.exp)
    return _rsa_encrypt_and_encode(public_key, message)
