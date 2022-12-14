import json
import pandas as pd
import tweepy
import csv
from datetime import datetime
from pprint import pprint

# consumer_key = 'pXH0AbgYOXlPGfB5cUPp4tORj'
# consumer_secret = '2fAXh1UEWqBACX5ejOMWlGzm5FH6MsHcWUaEwl1EjAKnpUmUT2'
# access_token = '1042095274842316806-EOhE0hsnpSDQa1SxFRXicq7acZKaS9'
# access_token_secret = '6p2TY9hkgbk5CIpOFg8hOc5v2MCUPskYSfVfwUBRxxfuR'
academic_bearer = "AAAAAAAAAAAAAAAAAAAAAIdpIgEAAAAAr6AixckPLuyYWLgvmJr%2FhYJkq4s%3DQCeCj6DRyOu0iIxXZzLX5ggNjcXj6tHAQc5Lk0KFRhAlvBdnXj"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
auth = tweepy.OAuth2BearerHandler(academic_bearer)
api = tweepy.API(auth,wait_on_rate_limit=True)

def collect_data(hashtag):
    data_list = []

    # hashtag = "#HijabBan"
    print(hashtag)

    # count = 0
    for tweet in tweepy.Cursor(api.search_tweets,q=hashtag,
                            lang="en",
                            tweet_mode='extended',
                            # since="2022-01-01",
                            until="2022-12-10"
                            ).items():
        twt_data = tweet._json
        created_at_date = datetime.strptime(twt_data['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime("%Y-%m-%d")
        print(created_at_date)
        if created_at_date>='2022-07-05':
            print('saved', created_at_date)
            # pprint(twt_data)
            data_list.append(twt_data)
            # count +- 1

        # if len(data_list)>=10:
        #     break
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    with open('data/'+hashtag+'.json', 'w') as fout:
        json.dump(data_list, fout, indent=4)

with open('search_hashtags.txt', 'r') as fin:
    search_hashtags = [h.strip() for h in fin.readlines()]
    for h in search_hashtags:
        collect_data(h)