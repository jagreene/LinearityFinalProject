import random
import string
import numpy
from fractions import *
from numpy import *


alpha_list = list(string.ascii_lowercase)
alpha_dict = dict((alpha_list[i],i) for i in range(26))


def split_message(message,n):
	message = message.lower()
	message = message.replace(" ","")
	blocks = []
	for i in range (0,len(message),n):
		blocks.append(message[i:i+n])
	return blocks


def create_key(n):
	key = []
	for i in range(n):
		line = []
		for j in range(n):
			rand = random.randint(0,25)
			line.append(rand)
		key.append(line)	
	det = int(round(numpy.linalg.det(key)))%26	
	if det != 0 and det%2 != 0 and det%13 != 0:
		return key
	else:		
		return create_key(n)


def encrypt_block(block,key):
	letters = list(block)
	
	num_block = []
	for i in range (len(letters)):		
		num_block.append(alpha_dict[letters[i]])
		
	key_block = [0]*len(num_block)	
	for i in range (len(key)):
		for j in range (len(key[i])):
			key_block[i] += key[i][j] * num_block[j]	
		key_block[i] = key_block[i]%26
	
	ciph_block = ['']*len(num_block)	
	for i in range (len(key_block)):
		ciph_block[i] = alpha_list[key_block[i]]
	return''.join(ciph_block)


def Encrypt_Message(message,n):
	blocks = split_message(message,n)
	key = create_key(n)
	ciph_blocks = []
	for block in blocks:				
		ciph_blocks.append(encrypt_block(block,key))	
	return {'ciphertext':''.join(ciph_blocks),'key':key}


#print Encrypt_Message('multiples of n',3)