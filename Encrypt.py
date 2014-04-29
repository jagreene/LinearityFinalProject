import random
import string
import numpy
from fractions import *
from numpy import *


alpha_list = list(string.ascii_lowercase)
alpha_dict = dict((alpha_list[i],i) for i in range(26))


def split_message(message,n):
	"""Splits the plaintext message into blocks of n letters"""
	message = message.lower()
	message = message.replace(" ","")
	blocks = []
	for i in range (0,len(message),n):
		blocks.append(message[i:i+n])
	return blocks


def create_key(n):
	"""Randomly generates an n-by-n matrix (numbers 0-25) to use as a key"""
	key = []
	for i in range(n):
		line = []
		for j in range(n):
			rand = random.randint(0,25)
			line.append(rand)
		key.append(line)	
	det = int(round(numpy.linalg.det(key)))%26	
	if det != 0 and det%2 != 0 and det%13 != 0:   #Makes sure the determinant isn't 0 or divisible by 2 or 13
		return key
	else:		
		return create_key(n)


def encrypt_block(block,key):
	"""Encrypts each block by multiplying it by the key"""
	letters = list(block)
	
	print letters

	num_block = []
	for i in range (len(letters)):		         #Converts the block to numbers
		num_block.append(alpha_dict[letters[i]])

	print num_block
		
	key_block = [0]*len(num_block)	
	for i in range (len(key)):
		for j in range (len(key[i])):            #Multiplies the block by the key (mod 26)
			key_block[i] += key[i][j] * num_block[j]	
		key_block[i] = key_block[i]%26

	print key_block
	
	ciph_block = ['']*len(num_block)	
	for i in range (len(key_block)):             #Converts the block to ciphertext letters
		ciph_block[i] = alpha_list[key_block[i]]
	return''.join(ciph_block)

	print ciph_block

def Encrypt_Message(message,n):
	"""Encrypts a given message using the Hill Cipher
		Inputs: message to be encrypted, and n (size of the key matrix)
		Outputs: ciphertext and key in a dictionary"""
	blocks = split_message(message,n)
	key = create_key(n)
	print 'Key:\n' + str(matrix(key))
	ciph_blocks = []
	for block in blocks:				
		ciph_blocks.append(encrypt_block(block,key))  #Joins the encrypted blocks
	return {'ciphertext':''.join(ciph_blocks),'key':key}  #Returns the ciphertext and the key as a dictionary