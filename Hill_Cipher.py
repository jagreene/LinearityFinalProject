import random
import string
import numpy
from fractions import Fraction
from numpy import *
import ModInverse
import Encrypt
import Decrypt

message = 'KIRYUIN SATSUKIIIIIIII'
n = 3

vals = Encrypt.Encrypt_Message(message,n)
ciphertext = vals['ciphertext']
key = vals['key']
inv_key = ModInverse.modular_inverse(key)
inv_key = inv_key.tolist()
return_message = Decrypt.Decrypt_Message(ciphertext,inv_key)

print matrix(key)
print matrix(inv_key)
print message
print ciphertext
print return_message