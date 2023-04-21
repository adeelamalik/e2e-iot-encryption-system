import os
from pytea import TEA

global key
key= '1c2e445708f1121ef948b08cc0a3c59d'
# print('key is', key)
# content = 'Hello worldworldworld!'
# tea = TEA(key)
# e = tea.encrypt(content.encode())
# print('encrypt hex:', e.hex())
# d = tea.decrypt(e)
# print('decrypt:', d.decode())

def encrypt(plain_text):
    # key = '939f3a799df18ec9cb0186b4b24936f1'
    key = bytes(key, 'utf-8')
    tea = TEA(key)
    encrypted_text = tea.encrypt(plain_text.encode())
    return encrypted_text.hex()

def decrypt(encrypted_text):
    key1 = bytes.fromhex(key)
    tea1 = TEA(key1)
    decrypted_bytes = bytes.fromhex(encrypted_text)
    decrypted_text = tea1.decrypt(decrypted_bytes)
    return decrypted_text.decode()