# twitter-lib
A simple lib to post and research

#Exemple
from twitter import Twitter
```python
consumerKey = 'yourConsumerKey'
consumerSecret = 'yourConsumerSecrey'

tokenKey = 'yourTokenkey'
tokenSecret = 'youtTokenScret'

twitter = Twitter(consumerKey, consumerSecret, tokenKey, tokenSecret)

twitter.tweet('My tweet')

search = twitter.search('#mysearch, 'us')

for result in search:
    print(result['text'])
    print(result['user']['screen_name'])
```
