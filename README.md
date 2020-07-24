 Sentiment-Analysis
==================================================
### Twitter Sentiment Analysis 
Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

### Installation:

* **Tweepy :** tweepy is the python client for the official Twitter API.
      
      Install it using following pip command:
            pip install tweepy
* **TextBlo b:** textblob is the python library for processing textual data.
      
      Install it using following pip command:
            pip install textblob
**Also**, we need to install some NLTK corpora using following command:
      
            python -m textblob.download_corpora
            
### Authentication:
In order to fetch tweets through Twitter API, one needs to register an App through their twitter account.
#### Follow these steps for the same:

- Open this link and click the button: ‘Create New App’
- Fill the application details. You can leave the callback url field empty.
- Once the app is created, you will be redirected to the app page.
- Open the ‘Keys and Access Tokens’ tab.
- Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.            
            
#### These 3 major steps in our program:

- Authorize twitter API client.
- Make a GET request to Twitter API to fetch tweets for a particular query.
- Parse the tweets. Classify each tweet as positive, negative or neutral.            
            
