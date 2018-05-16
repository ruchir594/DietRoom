import csv

#user = 'ruchir94'

def publish_cmd(user):
    with open(user+'_tweets.csv') as f:
        read = f.readlines()
        for row in read:
            print row
