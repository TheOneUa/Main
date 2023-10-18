import sys
import math
import binascii

a = input()
b = input()
c = input()

xor = hex(int(a, 16) ^ int(b, 16) ^ int(c, 16))
xored = xor[2:]

res = bytearray.fromhex(xored).decode()
print(res)