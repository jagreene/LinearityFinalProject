from numpy import *
import ModInverse
import Encrypt
import Decrypt


plaintext = 'three letters'  #Your plaintext message to be encrypted (must be divisible by n)
n = 3                         #Size of the encryption matrix/key

print 'Plaintext: ' + plaintext
vals = Encrypt.Encrypt_Message(plaintext,n)
ciphertext = vals['ciphertext']
print 'Ciphertext: ' + ciphertext
key = vals['key']
inv_key = ModInverse.modular_inverse(key)
inv_key = inv_key.tolist()
print 'Inverse Key: \n' +  str(matrix(inv_key))
return_message = Decrypt.Decrypt_Message(ciphertext,inv_key)
print 'Output: ' + return_message