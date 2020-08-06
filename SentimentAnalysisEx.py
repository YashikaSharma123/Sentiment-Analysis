import tweepy
from textblob import TextBlob #text/tweet parse
from tweepy import OAuthHandler 
import re 
api_key="......................"
api_secret_key="................."

access_token ="..................."
access_token_secret=".............."

auth = OAuthHandler(api_key, api_secret_key)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)

print('login is success')

def get_sentiment(tweet):
    analysis = TextBlob(tweet)

    # set sentiment
    if analysis.sentiment.polarity > 0:
            return 'positive'
    elif analysis.sentiment.polarity == 0:
            return 'neutral'
    else:
            return 'negative'   

def clean_data(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())     


def fetch_data(leader,c=10):
    res = api.search(q=leader,count=c)

    out = []
    #print(res)
    for r in res:
        text = clean_data(r.text)
        #print(text)
        sent = get_sentiment(text)
        out.append(sent)
    return out 


leaders = ["Narendra Modi","Rahul Gandhi","Sonia Gandhi"]
for l in leaders:
    out = fetch_data(l)
    print(l,'-----------------------------')
    print(out)
    

    








