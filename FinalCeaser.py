# Simple Caesar  substitution cipher that encrypts and decrypts a given message, using modular math. 

import numpy as np
import re

text = open('constitution.txt','r')


textVec = np.array([[ord(i) for i in x] for x in text.readlines()]) 
textVec = np.hstack(textVec.flat)
# textVec = textVec.flatten()

# print textVec
shift = 1

shiftVec = shift*np.ones(len(textVec))
# print type(textVec[0])
# print type(shiftVec[0])

ciphertext = shiftVec + textVec

cipherText = np.array([chr(int(x)%256) for x in ciphertext])

cipherText = re.sub(r'\W+','',''.join(cipherText))

print cipherText

ciphertext -= shiftVec

cipherText = np.array([chr(int(x)%256) for x in ciphertext])

# print ''.join(cipherText)

