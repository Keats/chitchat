 # -*- coding: utf-8 -*-
from twython import Twython
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 200)


APP_KEY = 'vSnRygPTqdXrpeNnvhSGifz4A'
APP_SECRET = 'QTSoWPlEunVxZtybOEdX7Bq22RBFBTst9waj62yZrIyjqr7peH'

twitter = Twython(APP_KEY, APP_SECRET)


def help_me(query, lang="pt"):
  result = ""
  highest_retweet = 0

  twitter_results = twitter.search(q=query, lang=lang)['statuses']

  for twitter_result in twitter_results:
    if twitter_result['retweet_count'] >= highest_retweet:
      result = twitter_result['text']
      highest_retweet = twitter_result['retweet_count']

  print "%d retweets" % highest_retweet
  print result
  voice = engine.getProperty('voices')[0]
  engine.setProperty('voice', voice.id) 
  engine.say(result)



help_me("copa da mundo")
engine.runAndWait()
