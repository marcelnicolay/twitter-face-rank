# coding: utf-8
#!/usr/bin/env python

import tweepy
import random

class TwitterAPI(object):
    
    api = None
    
    def __init__(self):
        self.api = tweepy.API()
        
    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def getRandon(self, search):
        result = self.api.search(q=search, page=1, rrd=100, show_user=True)
        random.shuffle(result)
        
        return result
        