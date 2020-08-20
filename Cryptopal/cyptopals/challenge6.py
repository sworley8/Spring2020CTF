from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

def hamming_distance(a, b):
    return sum(bin(byte).count('1') for byte in bxor(a,b))

with open("6.txt") as file:
        ciphertext = b64decode(file.read())


