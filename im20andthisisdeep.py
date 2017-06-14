'''
A reddit bot which just reposts links from /r/LateStageCapitalism to /r/im20andthisisdeep

I am not the creator of /r/im20andthisisdeep (although I wish I was).

Author: James Alexander Hughes

'''

import praw
import time

reddit = praw.Reddit('bot1')

# Get the 5 *hot* posts
lsc = reddit.subreddit('LateStageCapitalism')
hot_subs = []
for sub in lsc.hot(limit=10):
    hot_subs.append(sub)


# Post the submissions. Once every minute. 
i20 = reddit.subreddit('im20andthisisdeep')
startTime = time.time()
for sub in hot_subs:
    # only submit if it doesn't have self text 
    if sub.selftext == '':
    # only submit if it's a link to imgur
    #if sub.url.find('imgur') != -1 or sub.url.find('i.redd.it') != -1:
        print sub.title
        print sub.url
        #i20.submit(sub.title, url=sub.url)
        time.sleep(600 - ((time.time() - startTime) % 600.0))

