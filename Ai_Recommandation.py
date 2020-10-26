# Import Pandas
import pandas as pd

# Load Good Data
goodData = pd.read_csv('resultat.csv')
goodData.head()

# Load Bad Data
badData = pd.read_csv('bad_words.csv')
badData.head()

#merger des de fichier
data = pd.merge(goodData, badData, on='dataid')
data.head()

data.groupby('id')['body_text_nostop'].mean().head()
data.groupby('id')['body_text_nostop'].mean().sort_values(ascending=False).head()
