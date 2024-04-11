from ntscraper import Nitter
import pandas as pd

def create_twiter_dataset(username, no_of_tweets):
    scraper = Nitter(log_level=1, skip_instance_check=False)
    tweets = scraper.get_tweets(username, mode="user", number=no_of_tweets)
    data = {
    'link':[],
    'text':[],
    'user':[],
    'likes':[],
    'quotes':[],
    'retweets':[],
    'comments':[]
    }

    for tweet in tweets['tweets']:
        data['link'].append(tweet['link'])
        data['text'].append(tweet['text'])
        data['user'].append(tweet['user']['name'])
        data['likes'].append(tweet['stats']['likes'])
        data['quotes'].append(tweet['stats']['quotes'])
        data['retweets'].append(tweet['stats']['retweets'])
        data['comments'].append(tweet['stats']['comments'])

    df = pd.DataFrame(data)
    name = '{}.csv'.format(username)
    df.to_csv(name)
    return df.head()

