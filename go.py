 # -*- coding: utf-8 -*-
from twython import Twython

APP_KEY = 'vSnRygPTqdXrpeNnvhSGifz4A'
APP_SECRET = 'QTSoWPlEunVxZtybOEdX7Bq22RBFBTst9waj62yZrIyjqr7peH'

twitter = Twython(APP_KEY, APP_SECRET)


def search_twitter(query):
  result = ""
  highest_retweet = 0

  twitter_results = twitter.search(q=query)['statuses']

  for twitter_result in twitter_results:
    if twitter_result['retweet_count'] >= highest_retweet:
      result = twitter_result['text']
      highest_retweet = twitter_result['retweet_count']

  return result

print search_twitter("football")
