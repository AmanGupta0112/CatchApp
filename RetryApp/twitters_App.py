from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from textblob import TextBlob
# import .Cred
import numpy as np
import re
from decouple import config

ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRET = config('CONSUMER_SECRET')

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        return auth

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

class TweetAnalyzer():

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

class Sentiment_Analysis:

    def Analysis(ans):
        twitter_client = TwitterClient()
        tweet_analyzer = TweetAnalyzer()

        api = twitter_client.get_twitter_client_api()

        query = ans

        tweets = api.search(q=query, result_type = "mixed", count=20)
        size = len(tweets)
        sentiments = np.array([tweet_analyzer.analyze_sentiment(tweet.text) for tweet in tweets])
        pos,neu,neg = 0,0,0
        for sentiment in sentiments:
            if sentiment == 1:
                pos += 1
            elif sentiment == 0 :
                neu += 1
            else:
                neg += 1

        pos = (pos/size)*100
        neu = (neu/size)*100
        neg = (neg/size)*100

        sa_dt = { "pos" : pos , "neu" : neu, "neg" : neg}
        print(sa_dt)

        return sa_dt
