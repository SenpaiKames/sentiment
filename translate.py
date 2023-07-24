import pandas as pd 
from deep_translator import GoogleTranslator


# detecting supported languages
# langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# print(langs_dict)

# text = "Ano ginagawa mo?"
# lang = single_detection(text, api_key='e6fe802038a5338e3fee4bcd020df3cb')

translated_tweets = []
csvFile = pd.read_csv('tweets_2.csv')

for tweet in csvFile['Tweet']:

    translated = GoogleTranslator(source='auto', target='english').translate(tweet)
    translated_tweets.append(translated)

    df = pd.DataFrame({'Translated Tweets' : translated_tweets})
    print(df)

    df.to_csv('translated_v2.csv')





