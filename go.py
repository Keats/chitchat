from twython import Twython

APP_KEY = 'vSnRygPTqdXrpeNnvhSGifz4A'
APP_SECRET = 'QTSoWPlEunVxZtybOEdX7Bq22RBFBTst9waj62yZrIyjqr7peH'

twitter = Twython(APP_KEY, APP_SECRET)


def search_twitter(query):
  result = ""
  highest_retweet = 0

  twitter_results = twitter.search(q="worldcup")['statuses']

  for result in twitter_results:
    if result['retweet_count'] > highest_retweet:
      result = result['text']

  return result

print search_twitter("worldcup")
