import pandas as pd
import numpy as np


def createFreqDict():
    data = pd.read_table(
        "bigrams.txt", delimiter=" ", header=None, names=["bigram", "number"])

    numbers = data["number"].values

    bigrams = data["bigram"].values
    total = 0

    bigrams[46] = 'NA'
    for number in numbers:
        total += float(number)

    new = []
    for i in xrange(len(numbers)):
        new.append(numbers[i] / total)

    freqDict = dict(zip(bigrams, new))

    return freqDict


def determineEngBigramFreq():
    freqDict = createFreqDict()

    sortedBigrams = sorted(freqDict.iteritems())

    freqMatrix = np.zeros((26, 26))
    row = 0
    column = 0
    for bigrams, bigramFreqs in sortedBigrams:
        if row < 26:
            freqMatrix[row, column] = bigramFreqs
            row += 1

        else:
            row = 0
            column += 1
            freqMatrix[row, column] = bigramFreqs
            row += 1

    return freqMatrix

determineEngBigramFreq()
