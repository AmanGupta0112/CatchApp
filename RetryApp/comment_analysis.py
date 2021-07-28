import play_scraper as ps
from google_play_scraper import app as gapp
import numpy as np
from textblob import TextBlob

class CommentAnalyser():

    def analyse_sentiment(self,comment):
        analysis = TextBlob(comment)

        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

class Sentiment_Analysis :

    def Analysis(ans):
        comment_analyser = CommentAnalyser()
        app = ans
        result = ps.search(app, page=1)
        id = result[0]['app_id']

        appdetail = gapp(id)

        comments = appdetail['comments']

        size = len(comments)
        sentiments = np.array([comment_analyser.analyse_sentiment(comment) for comment in comments])
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
