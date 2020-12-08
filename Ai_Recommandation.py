import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import string

# Function pour formater le text csv
def word_list(textWords):
    df = pd.DataFrame(textWords, columns=['body_text_nostop'])
    wordList = df.stack().values.tolist()
    wordList = str(wordList).replace("[", "")
    wordList = str(wordList).replace("]", "")
    wordList = str(wordList).replace(" ", "")
    wordList = str(wordList).replace("'", "")
    wordList = str(wordList).replace("\"", "")
    wordList = wordList.split(',')
    return wordList

# Lire les données depuis le fichier CSV
inputGoodWords = pd.read_csv("resultat.csv")
inputBadWords = pd.read_csv("badwords.csv")

goodWords = word_list(inputGoodWords['body_text_nostop'])

badWords = word_list(inputBadWords['body_text_nostop'])

uniqueWords = set(goodWords).union(set(badWords))

#classifier les bad words depuis l'union entre les deux fichiers (resultat et badwords)
numOfBadWords = dict.fromkeys(uniqueWords, 0)
for word in badWords:
    numOfBadWords[word] = 1

#classifier les good words depuis l'union entre les deux fichiers (resultat et badwords)
numOfGoodWords = dict.fromkeys(uniqueWords, 0)
for word in goodWords:
    numOfGoodWords[word] = 1

#afficher la classification
print(numOfGoodWords)

#Le code suivant implémente la fréquence des termes en python.
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

#Les lignes suivantes calculent le terme fréquence pour chacun de nos documents.
tfA = computeTF(numOfBadWords, goodWords)
tfB = computeTF(numOfGoodWords, badWords)

#Le code suivant implémente la fréquence inverse des données en python.
def computeIDF(documents):
    import math
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] = 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

#L'IDF est calculé une fois pour tous les documents.
idfs = computeIDF([numOfBadWords, numOfGoodWords])

#Enfin, le TF-IDF est simplement le TF multiplié par l'IDF.
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
df = pd.DataFrame([tfidfA, tfidfB])

print(df)
df.to_csv('newresfinal.csv')