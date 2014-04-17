import os, re, copy, pprint
import LinearityCrypto
import pyperclip

# Importing LinearityCrypto, I want to get the pattern of the cipherword 'OLQIHXIRCKGNZ', by doing wordPat = LinearityCrypto.get_pattern('OLQIHXIRCKGNZ').
# WordPat is, therefore, the pattern with the integers representing the existance of letters '0.1.2.3.4.5.3.6.7.8.9.10.11'.
# Importing the newPythonFile of our "created" dictionary, we search for the potential candidates that fit that pattern by doing: newPythonFile.allPotentialPattern['0.1.2.3.4.5.3.6.7.8.9.10.11']

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getBlankCipherletterMapping():
	""" Returns a dictionary that is a blank cipherletter mapping of 26 keys of the english alphabet. """
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addLettersToMapping(letterMapping,cipherword,candidate):
	""" letterMapping parameter is a dictionary with no values that the function will start with. It ends up having the information from both candidates.
		cipherword parameter is the string balue of the cipherword examined.
		candidates parameter is the potential decrypted words.
	"""
	letterMapping = copy.deepcopy(letterMapping)
	for i in range(len(cipherword)):
		if candidate[i] not in letterMapping[cipherword[i]]:
			letterMapping[cipherword[i]].append(candidate[i])
	return letterMapping

def intersectMappings(Map1,Map2):
	""" Takes the intersection of the two dictionaries maps generated, to produce the most universal map. """
	Map3 = getBlankCipherletterMapping()
	for letter in alphabet:
		if Map1[letter] == []:
			Map3[letter] = copy.deepcopy(Map2[letter])
		elif Map2[letter] == []:
			Map3[letter] = copy.deepcopy(Map1[letter])
		else:
			for i in Map1[letter]:
				if i in Map2[letter]:
					Map3[letter].append(i)
	return Map3