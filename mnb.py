import nltk
import pandas as pd


from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# data_1 = ["Piford Technologies Piford is in Mohali."]

# vectorizer = CountVectorizer()

# vectorizer.fit(data_1)

# print(vectorizer.vocabulary_)

# vector = vectorizer.transform(data_1)
# print(vector)


df = pd.read_csv('token.csv')
# print(df.head())


bow_transformer = CountVectorizer().fit(df['Tokenized'])
# print(bow_transformer.vocabulary_)

tweet_bow = bow_transformer.transform(df['Tokenized'])
# print(tweet_bow)
tfidf_trans = TfidfTransformer().fit(tweet_bow)
print(tfidf_trans)

tweet_tfidf = tfidf_trans.transform(tweet_bow)
print(tweet_tfidf)
print(tweet_tfidf.shape)

## Opinion Lexicon Corpus
# Get the list of positive words
# from nltk.corpus import opinion_lexicon
# positive_words = opinion_lexicon.positive()

# # Get the list of negative words
# negative_words = opinion_lexicon.negative()

# # Print some examples of positive and negative words
# print("Positive Words:", positive_words[:5])
# print("Negative Words:", negative_words[:5])





