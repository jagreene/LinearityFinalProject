# Simple Caesar  substitution cipher that encrypts and decrypts a given message, using modular math. 

import numpy as np

text = 'hey'

textVec = np.array([ord(x) for x in text])

shift = 258

shiftVec = shift*np.ones(len(textVec))

ciphertext = shiftVec + textVec

cipherText = np.array([chr(int(x)%256) for x in ciphertext])

print cipherText

ciphertext -= shiftVec

cipherText = np.array([chr(int(x)%256) for x in ciphertext])

print cipherText