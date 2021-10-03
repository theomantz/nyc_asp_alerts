import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("twitter_api_key")
API_SECRET = os.getenv("twitter_api_secret")
ACCESS_TOKEN = os.getenv("twitter_access_token")
TOKEN_SECRET = os.getenv("twitter_access_token_secret")

twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

twitter_api = tweepy.API(twitter_oauth)

try:
  print(twitter_api.verify_credentials())
  print("Successfully logged in")
except tweepy.TweepError as e:
  print(e)
except Exception as e:
  print(e)
