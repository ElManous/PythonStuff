import tweepy
from keys import keys
import json


# import player data 
# open file with JSON and dump data into output file
with open('playerData.txt') as outfile:
    livdata=json.load(outfile)


# Get access keys from API page
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_SECRET = keys['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# tweet out the stats
for p in livdata['players']: 
    api.update_status(status=p)
    


