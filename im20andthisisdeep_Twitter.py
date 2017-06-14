'''
A Twitter bot which just tweets links from /r/LateStageCapitalism 

Author: James Alexander Hughes

'''

import os
import praw
import requests
import time
import tweepy
import twitterCreds


def tweet_image(api, url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


# Twitter Details
CONSUMER_KEY = twitterCreds.CONSUMER_KEY
CONSUMER_SECRET = twitterCreds.CONSUMER_SECRET
ACCESS_KEY = twitterCreds.ACCESS_KEY
ACCESS_SECRET = twitterCreds.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# Get the X *hot* posts
X = 15
reddit = praw.Reddit('bot1')
lsc = reddit.subreddit('LateStageCapitalism')
hot_subs = []
for sub in lsc.hot(limit=X):
    if sub.selftext == '':
        hot_subs.append(sub)

# Tweet the hot posts
startTime = time.time()
for sub in hot_subs:
    # only submit if it doesn't have self text 
    if sub.selftext == '':
        #print sub.title
        #print sub.url
        if len(sub.title) <= 100:
            tweet=sub.title + " " + sub.shortlink + " #LateStageCapitalism"
        else:
            tweet=sub.shortlink + " #LateStageCapitalism"

        tweet_image(api, url=sub.url, message=tweet)  
        #print
        time.sleep(3600 - ((time.time() - startTime) % 3600.0))

