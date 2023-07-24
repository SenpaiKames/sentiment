from nltk import sent_tokenize, word_tokenize
import pandas as pd 

# text = "@kaixcpa yes, you can attend f2f classes and online classes, the hybrid. ðŸ’™ðŸ’›"

# word_tokens = word_tokenize(text)
# print(word_tokens)

tok = []
csvFile = pd.read_csv('lemma.csv')

## for tokenization


for tweet in csvFile['Lemmatized']:

    tok.append(word_tokenize(tweet))

    df = pd.DataFrame({'Tokenized': tok})
    print(df)

    df.to_csv('token.csv')
