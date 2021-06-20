import tweepy
import twitter_credentials

hash_tag = ''
num_tweets = 100

def getHashtag():
    global hash_tag
    hash_tag = input('Enter hashtag to search : ')

def authenticateTwitterAPI():
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    return auth

def fetchTweets(api):
    tweets = tweepy.Cursor(api.search, q=hash_tag).items(num_tweets)
    for tweet in tweets:
        if 'RT' not in tweet.text:
            print(tweet.text)

def getTweets():
    auth = authenticateTwitterAPI()
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    fetchTweets(api)


def execute():
    getHashtag()
    getTweets()

if __name__ == "__main__":
    execute()