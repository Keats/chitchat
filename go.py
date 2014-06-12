from twython import Twython

APP_KEY = 'vSnRygPTqdXrpeNnvhSGifz4A'
APP_SECRET = 'QTSoWPlEunVxZtybOEdX7Bq22RBFBTst9waj62yZrIyjqr7peH'

twitter = Twython(APP_KEY, APP_SECRET)


def search_twitter(query):
  results = {}

  twitter_results = twitter.search(q="worldcup")

search_twitter("worldcup")
