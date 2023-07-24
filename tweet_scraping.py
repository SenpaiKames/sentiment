import snscrape.modules.twitter as sntwitter
import pandas as pd

filters = [ 'online classes since:2021-01-01 near:"Caloocan"', 'online classes since:2021-01-01 near:"Quezon"', 'online classes since:2021-01-01 near:"Manila"', 
            'online classes since:2021-01-01 near:"Cebu"', 'online classes since:2021-01-01 near:"Davao"',
           
            'asynchronous since:2021-01-01 near:"Davao"', 'asynchronous since:2021-01-01 near:"Caloocan"', 
            'asynchronous since:2021-01-01 near:"Quezon"', 'asynchronous since:2021-01-01 near:"Cebu"', 'asynchronous since:2021-01-01 near:"Manila"',
            
            'synchronous since:2021-01-01 near:"Davao"', 'synchronous since:2021-01-01 near:"Caloocan"', 'synchronous since:2021-01-01 near:"Quezon"',
            'synchronous since:2021-01-01 near:"Cebu"', 'synchronous since:2021-01-01 near:"Manila"', 
            
            'distance learning since:2021-01-01 near:"Davao"', 'distance learning since:2021-01-01 near:"Caloocan"', 'distance learning since:2021-01-01 near:"Quezon"',
            'distance learning since:2021-01-01 near:"Cebu"', 'distance learning since:2021-01-01 near:"Manila"',
            
            'modular learning since:2021-01-01 near:"Davao"', 'modular learning since:2021-01-01 near:"Caloocan"', 'modular learning since:2021-01-01 near:"Quezon"',
            'modular learning since:2021-01-01 near:"Cebu"', 'modular learning since:2021-01-01 near:"Manila"',
            
            'blended learning since:2021-01-01 near:"Davao"', 'blended learning since:2021-01-01 near:"Caloocan"', 'blended learning since:2021-01-01 near:"Quezon"',
            'blended learning since:2021-01-01 near:"Cebu"', 'blended learning since:2021-01-01 near:"Manila"',
            
            'online mag-aral since:2021-01-01', 'online mag-aral since:2021-01-01 near:"Davao"', 'online mag-aral since:2021-01-01 near:"Caloocan"', 'online mag-aral since:2021-01-01 near:"Quezon"',
            'online mag-aral since:2021-01-01 near:"Cebu"', 'online mag-aral since:2021-01-01 near:"Manila"',
            
            'hybrid classes since:2021-01-01 near:"Davao"', 'hybrid classes since:2021-01-01 near:"Caloocan"', 'hybrid classes since:2021-01-01 near:"Quezon"',
            'hybrid classes since:2021-01-01 near:"Cebu"', 'hybrid classes since:2021-01-01 near:"Manila"',
            
            'online klase since:2021-01-01', 'online klase since:2021-01-01 near:"Davao"', 'online klase since:2021-01-01 near:"Caloocan"', 'online klase since:2021-01-01 near:"Quezon"',
            'online klase since:2021-01-01 near:"Cebu"', 'online klase since:2021-01-01 near:"Manila"'
            
            ]

tweets = []
limit = 20000

for filter in filters:

    for tweet in sntwitter.TwitterSearchScraper(filter).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    print(df)

    df.to_csv('tweets_2.csv')


