from tweepy import OAuthHandler

from app import keys

class TwitterAuthenticator:

    def authenticate_twitter_app(self):
        auth = OAuthHandler(keys.API_KEY, keys.API_KEY_SECRET)
        auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
        return auth
