import requests
from twython import Twython
from blog.auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
class tweet_joke:
    def tweet_fn():
        twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
        #message = "Hello world!"
        url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        joke_msg = requests.get(url, headers=headers).json().get('joke')
        print(joke_msg)
        twitter.update_status(status=joke_msg)
        print("Tweeted: %s" % joke_msg)
