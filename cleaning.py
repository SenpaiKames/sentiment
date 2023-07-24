import pandas as pd
import string
from nltk.corpus import stopwords

df = pd.read_csv('translated_v1.csv')

clean = []

# lower case all words #
df['clean_text'] = df['Translated Tweets'].str.lower()
df.head()

# removal of punctuations #
string.punctuation 

def remove_punctuations(text): 
    punctuations = string.punctuation
    return text.translate(str.maketrans('', '', punctuations))

df['clean_text'] = df['clean_text'].apply(lambda x: remove_punctuations(x))
# df.head()
# print(df)

# removal of stopwords #
", ".join(stopwords.words('english'))

STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in text.split() if word not in STOPWORDS])

df ['clean_text'] = df['clean_text'].apply(lambda x: remove_stopwords(x))
df.head()


# removal of frequent words # 


# removal of special characters # 
import re
def remove_spl_chars(text):
    text = re.sub('[^a-zA-Z0-9]', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text 

df['clean_text'] = df['clean_text'].apply(lambda x: remove_spl_chars(x))
df.head()
print(df)


df.to_csv('clean.csv')