import sys, csv
import pandas as pd
import re
import pymongo

class MakeProfile(object):
    def __init__(self, filepath, screen_name):
        self.m = []
        self.filepath = filepath
        self.all_text = []
        self.all_words = []
        self.feature_vector = ['neg', 'pos', 'neu', 'health', 'news', 'politics',
                                'inspire']
        self.feature_dictionary = {}
        self.feature_dictionary['screen_name'] = screen_name


    def judge(self):
        df = pd.read_csv(self.filepath)
        all_text = df.text
        print len(all_text)
        self.all_text = all_text
        for line in all_text:
            self.all_words.extend(re.sub("[^\w]", " ",  line).split())
        self.sentiment()
        for feature in self.feature_vector[3:]:
            descriptor = self.add_bow_features('./cdata/'+feature+'.txt')
            self.feature_dictionary[feature] = descriptor

        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client.store1
        collection = db.latent_profile
        post_id = collection.insert_one(self.feature_dictionary).inserted_id


    def sentiment(self):
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()
        neg = 0
        pos = 0
        neu = 0
        for e in self.all_text:
            ss = sid.polarity_scores(e)
            if ss['neg'] > 0.2:
                neg += 1
            elif ss['pos'] > 0.5:
                pos += 1
            else:
                neu += 1

        self.feature_dictionary['neg'] = neg
        self.feature_dictionary['pos'] = pos
        self.feature_dictionary['neu'] = neu

    def add_bow_features(self, f_path):
        with open(f_path) as f:
            read_data = f.readlines()
        read_data = set([e[:-1] for e in read_data])
        cnt = 0
        for e in self.all_words:
            if e in read_data:
                cnt += 1
        return cnt
