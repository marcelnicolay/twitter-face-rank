# coding: utf-8
#!/usr/bin/env python

import os, sys, atexit, getopt

def usage():
    pass
    
def main():

    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath("%s/.." % project_root))
    
    tweepy.API().trends_current()
    
    
if __name__ == "__main__":
    main()