# coding: utf-8
#!/usr/bin/env python

import os, sys, atexit, getopt
import random, tweepy

def usage():
    pass
    
def main():

    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath("%s/.." % project_root))
    
    result = tweepy.API().trends_current()['trends']
    result = result[result.keys()[0]]
    
    random.shuffle(result)
    result = result[:5]
    
    from twittface.models.campanha import Campanha
    
    trends = []
    for trend in result:
        trends.append(trend['name'])
        
    camp = Campanha()
    camp.ativaCampanha(trends)
    
if __name__ == "__main__":
    main()