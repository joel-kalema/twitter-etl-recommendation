import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://username:password@localhost/dbname')

def load_data(json_file):
    with open(json_file, 'r') as file:
        data = [json.loads(line) for line in file]

    users = []
    tweets = []
    hashtags = []
    interactions = []

    for tweet in data:
        user = tweet['user']
        users.append({
            'user_id': user['id'],
            'screen_name': user['screen_name'],
            'description': user['description'],
            'created_at': tweet['created_at']
        })

        tweets.append({
            'tweet_id': tweet['id'],
            'user_id': tweet['user']['id'],
            'text': tweet['text'],
            'in_reply_to_user_id': tweet.get('in_reply_to_user_id'),
            'retweeted_status_id': tweet.get('retweeted_status', {}).get('id'),
            'created_at': tweet['created_at'],
            'lang': tweet['lang']
        })

        for tag in tweet['entities']['hashtags']:
            hashtags.append({
                'tweet_id': tweet['id'],
                'tag': tag['text']
            })

        if tweet.get('in_reply_to_user_id'):
            interactions.append({
                'tweet_id': tweet['id'],
                'user_id': tweet['user']['id'],
                'contact_user_id': tweet['in_reply_to_user_id'],
                'type': 'reply'
            })
        elif tweet.get('retweeted_status'):
            interactions.append({
                'tweet_id': tweet['id'],
                'user_id': tweet['user']['id'],
                'contact_user_id': tweet['retweeted_status']['user']['id'],
                'type': 'retweet'
            })

    pd.DataFrame(users).drop_duplicates().to_sql('users', engine, if_exists='append', index=False)
    pd.DataFrame(tweets).drop_duplicates().to_sql('tweets', engine, if_exists='append', index=False)
    pd.DataFrame(hashtags).drop_duplicates().to_sql('hashtags', engine, if_exists='append', index=False)
    pd.DataFrame(interactions).drop_duplicates().to_sql('interactions', engine, if_exists='append', index=False)