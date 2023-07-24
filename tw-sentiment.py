from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# tweet = "@MehranShakarami today's cold @ home 😒 https://mehranshakarami.com"
tweet = 'lowkey missing online classes'

# precprocess tweet
tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    
    elif word.startswith('http'):
        word = "http"
    tweet_words.append(word)

tweet_proc = " ".join(tweet_words)

# load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
# output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()
scores = softmax(scores)

tweet_categ = []

# for i in range(len(scores)):
    
#     l = labels[i]
#     s = scores[i]
#     print(l,s)

print(scores)

large_val = max(scores[0], scores[1], scores[2])
if large_val == scores[0]:
    category = labels[0]
elif large_val == scores[1]:
    category = labels[1]
elif large_val == scores[2]:
    category = labels[2]

print(category)

