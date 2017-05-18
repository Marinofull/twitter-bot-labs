import tweepy
#import requests
from configs import *
from helpers import *

class BotStreamer(tweepy.StreamListener):

    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        if not isinside(username, 'username-blacklist.txt'):
            tweet_echo(username, status_id)
        else:
            print('abusive username')



def tweet_echo(username, status_id):
    #request = requests.get(url, stream=True)
    #if request.status_code == 200:
    api.update_status(status='hi @{0}'.format(username) , in_reply_to_status_id=status_id)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth) # create an API object

myStreamListener = BotStreamer()
stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=[appname])


#user = api.get_user('tname')
#for friend in user.friends():
#    print(friend.screen_name)
