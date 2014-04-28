from numpy import *
import ModInverse
import Encrypt
import Decrypt


plaintext = 'three letters'  #Your plaintext message to be encrypted (must be divisible by n)
n = 3                         #Size of the encryption matrix/key

vals = Encrypt.Encrypt_Message(plaintext,n)
ciphertext = vals['ciphertext']
key = vals['key']
inv_key = ModInverse.modular_inverse(key)
inv_key = inv_key.tolist()
return_message = Decrypt.Decrypt_Message(ciphertext,inv_key)

print 'Key: \n' + str(matrix(key))
print 'Inverse Key: \n' +  str(matrix(inv_key))
print 'Plaintext: ' + plaintext
print 'Ciphertext: ' + ciphertext
print 'Output: ' + return_message