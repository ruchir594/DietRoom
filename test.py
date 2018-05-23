from streamuser import get_all_tweets, get_all_followers
from analyze import publish_cmd

user = 'ruchir94'

from classifiers import MakeProfile

obj = MakeProfile('./cdata/'+user+'_tweets.csv', user)
obj.judge()
