from cryptography.fernet import Fernet
from key import farnet_key

import base64
def encryptText(text):
    chipher = Fernet(base64.b64encode(farnet_key))
    encrypted = chipher.encrypt(bytes(text, 'utf-8'))
    return encrypted
