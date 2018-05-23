from streamuser import get_all_tweets, get_all_followers
from analyze import publish_cmd

user = 'RichardDawkins'

get_all_tweets(user)
#get_all_followers(user)
#publish_cmd(user)

#from classifiers import MakeProfile

#obj = MakeProfile('./'+user+'_tweets.csv')
#obj.judge()
