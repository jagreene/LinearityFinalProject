import pandas as pd
import numpy as np
import bigrams as bg
import re


def determineVowls(cipherText):

    cipherText = re.sub('[1-9.(), ]', '', cipherText)
    fullFreqDict = bg.createFreqDict()
    cipherFreqDict = {}
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for key, value in fullFreqDict.iteritems():
        cipherFreqDict.update({key: 0})

    total = 0
    if len(cipherText) % 2 != 0:
        cipherText = cipherText[:len(cipherText) - 1]

    for bigram in xrange(0, len(cipherText), 2):
        cipherFreqDict[cipherText[bigram:bigram + 2]] += 1.0
        total += 1.0

    for key, value in cipherFreqDict.iteritems():
        cipherFreqDict[key] /= total

    cipherFreqDict = sorted(cipherFreqDict.iteritems())

    row = 0
    column = 0
    cipherFreqMatrix = np.zeros((26, 26))
    for bigrams, bigramFreqs in cipherFreqDict:
        if row < 26:
            cipherFreqMatrix[row, column] = bigramFreqs
            row += 1

        else:
            row = 0
            column += 1
            cipherFreqMatrix[row, column] = bigramFreqs
            row += 1

    A = bg.determineEngBigramFreq()
    [U, S, V] = np.linalg.svd(A)
    [P, T, Q] = np.linalg.svd(cipherFreqMatrix)

    vowels = []
    consonants = []
    neuters = []

    # for i in xrange(0, 26):
    #     if U[i, 1] > 0 and V[i, 1] < 0:
    #         vowels.append(alphabet[i])
    #     elif U[i, 1] < 0 and V[i, 1] > 0:
    #         consonants.append(alphabet[i])
    #     else:
    #         neuters.append(alphabet[i])

    for i in xrange(0, 26):
        if P[i, 1] > 0 and Q[i, 1] < 0:
            vowels.append(alphabet[i])
        elif P[i, 1] < 0 and Q[i, 1] > 0:
            consonants.append(alphabet[i])
        else:
            neuters.append(alphabet[i])
            
    print vowels
    print consonants
    print neuters

determineVowls(
    "JRYL UHRLC ZWK UCTCW QCZLU ZIR RYL JZEDCLU MLRYIDE JRLED YVRW EDPU HRWEPWCWE Z WCA WZEPRW, HRWHCPTCK PW FPMCLEQ, ZWK KCKPHZECK ER EDC VLRVRUPEPRW EDZE ZFF SCW ZLC HLCZECK CNYZF. (ZVVFZYUC.) WRA AC ZLC CWIZICK PW Z ILCZE HPTPF AZL, ECUEPWI ADCEDCL EDZE WZE")
