from os import urandom
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

from minerva.common.constants import AES_KEYSIZE, AES_MODE


def generate_AES_key():
    return urandom(AES_KEYSIZE).encode('hex')

pad = lambda s: s + (AES_KEYSIZE - len(s) % AES_KEYSIZE) * chr(AES_KEYSIZE - len(s) % AES_KEYSIZE)
unpad = lambda s : s[0:-ord(s[-1])]

def _aes_encrypt(key, message):
    cipher = AES.new(key, AES_MODE)
    return cipher.encrypt(pad(message))
    
def _aes_encrypt_and_encode(key, message):
    return b64encode(_aes_encrypt(key, message))

def _aes_decrypt(key, message):
    cipher = AES.new(key, AES_MODE)
    return unpad(cipher.decrypt(message))
    
def _aes_decrypt_and_decode(key, message):
    cipher = AES.new(key, AES_MODE)
    return unpad(cipher.decrypt(b64decode(message)))

