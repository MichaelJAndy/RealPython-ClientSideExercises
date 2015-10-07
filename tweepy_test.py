# Consumer Key (API Key) seLtRPmpcnCpbGtOzRMkXJz3d
# Consumer Secret (API Secret) Hlee0nP1W5CwteG6uEHjzcyvLDL833Dvb3H5d8r6SHxaO5kwhW
# Access Level Read and write (modify app permissions)
# Owner Michael_J_Andy
# Owner ID 851859229
# Access Token 851859229-SNsRCZoCzAaCvu43k7hk094M6wjKm4VsJBjU3TZw
# Access Token Secret eUboOm2u5cMoWbeVsZkGL6Cy7JN6OsKS1Vr7cmuOgUuqs

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
