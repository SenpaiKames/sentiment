import nltk 
import pandas as pd 

lemm = []
csvFile = pd.read_csv('clean.csv')

## for lemmatization
wnl = nltk.WordNetLemmatizer()

for tweet in csvFile['clean_text']:

    lemm.append(wnl.lemmatize(tweet))

    df = pd.DataFrame({'Lemmatized': lemm})
    print(df)

    df.to_csv('lemma.csv')


