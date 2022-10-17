import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():

    access_key = "5FXOdlbvJv0KH85QiQCEXLkbg" 
    access_secret = "g3YW5ss4XlNwskGf8XiIhILXX6bjqJrEtrthb34jFFjIFth9u0" 
    consumer_key = "442467583-MCVgyRJGaKhSwSMLuIiTUm5MRDZEkG9bFuME7p7n"
    consumer_secret = "YnZPh63OK75MivZJxvdYE0YisBZqjA5KHFybH6Agi9gys"


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    print(tweets)