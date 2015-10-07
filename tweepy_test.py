import tweepy
# I've deleted the Twitter App but just in case
consumer_key = "XXXXXX"
consumer_secret = "XXXXXX"
access_token = "XXXXXX"
access_secret = "XXXXXX"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='#python')

# display results to screen
for t in tweets:
    print(t.created_at, t.text)
