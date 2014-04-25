import random
import string
import numpy
from fractions import *
from numpy import *

alpha_list = list(string.ascii_lowercase)
alpha_dict = dict((alpha_list[i],i) for i in range(26))


def split_ciphertext(ciphertext,n):
	ciphertext = ciphertext.lower()
	ciphertext = ciphertext.replace(" ","")
	blocks = []
	for i in range (0,len(ciphertext),n):
		blocks.append(ciphertext[i:i+n])
	return blocks



def decrypt_block(block,inv_key):
	letters = list(block)
	
	num_block = []
	for i in range (len(letters)):		
		num_block.append(alpha_dict[letters[i]])
	
	key_block = [0]*len(num_block)	
	for i in range (len(inv_key)):
		for j in range (len(inv_key[i])):
			key_block[i] += int(round(inv_key[i][j] * num_block[j]))
		key_block[i] = key_block[i]%26

	de_block = ['']*len(num_block)	
	for i in range (len(key_block)):					
		de_block[i] = alpha_list[key_block[i]]
	return''.join(de_block)


def Decrypt_Message(ciphertext,inv_key):
	blocks = split_ciphertext(ciphertext,len(inv_key))	
	de_blocks = []
	for block in blocks:				
		de_blocks.append(decrypt_block(block,inv_key))
	return ''.join(de_blocks)
			

#key = [[6,24,1],[13,16,10],[20,17,15]]
#inv_key = modular_inverse(key)

#print inv_key