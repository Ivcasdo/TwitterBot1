import tweepy
import datetime

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

print("just a few more steps to finish this bot")
twitter_API = tweepy.API(auth)
def publictweet():
    tweettopublish = 'Prueba del bot hola chavales como estamos todo bien #España'
    twitter_API.update_status(tweettopublish)
    print(tweettopublish)

publictweet()
