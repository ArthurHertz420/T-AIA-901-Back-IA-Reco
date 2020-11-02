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
inputGoodWords = pd.read_csv("resultat.csv").head(5)
inputBadWords = pd.read_csv("badwords.csv")

goodWords = word_list(inputGoodWords['body_text_nostop'])

badWords = word_list(inputBadWords['body_text_nostop'])

uniqueWords = set(goodWords).union(set(badWords))

#classifier les good words depuis l'union entre les deux fichiers (resultat et badwords)
numOfGoodWords = dict.fromkeys(uniqueWords, 0)
for word in goodWords:
    numOfGoodWords[word] = 1

#classifier les bad words depuis l'union entre les deux fichiers (resultat et badwords)
numOfBadWords = dict.fromkeys(uniqueWords, 0)
for word in badWords:
    numOfBadWords[word] = 1

print(numOfBadWords)

