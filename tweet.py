import re # regular expression 
import tweepy #access to tweet app
from tweepy import OAuthHandler #authenication 
from textblob import TextBlob #text/tweet parse
 
# keys and tokens from the Twitter Dev Console
#2 key used because one for sign one for data
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
# attempt authentication
try:
            # create OAuthHandler object
            auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            api = tweepy.API(auth)
            print('auth. success')
            
            
except:
            print("Error: Authentication Failed")
 
def clean_tweet( tweet):

        s =' '        
        return s.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
        
 
def get_tweet_sentiment( tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
def get_tweets( query, c=10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = api.search(q = query, count = c)
 
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
            
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)
                #print('text',parsed_tweet)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def get_tweet_result(leader):    

   
    # calling function to get tweets
    tweets = get_tweets(query = leader, c = 200)
    #print(tweets)

    #conventional list
    a =[111,222,4444]
    #b = [x*2 for x in a]
    #b=[]
    #for x in a:
    #    b.append(x*2)
        
        
    
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    
    result=[];
    
    # percentage of positive tweets
    #print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    result.append(format(100*len(ptweets)/len(tweets)))
    
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    #print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    result.append(format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    #print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
    result.append(format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

    return result

    
def gettweet():
    leaders=['Narendra Modi','Rahul Gandhi','Donald Trump']
    res=[]
    # calling main function
    for l in leaders:
        res.append(get_tweet_result(l))
        
    print(res)
    
    
gettweet()



