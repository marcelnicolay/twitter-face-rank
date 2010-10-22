# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError
import tweepy

import math
import settings

class LoginController(BaseController):
    
    def index(self, request_handler):
        
        auth = tweepy.OAuthHandler("5dMcC3yYelEVwQykbsitcA","63g7kzmNdJX25qVuz51RMUFXCwiJ7DKaeoMn3fLmlQ", "http://twittface.local:8080/login/oauth_callback")        
        redirect_url = auth.get_authorization_url()
        
        self.request_token = (auth.request_token.key, auth.request_token.secret)
        
        request_handler.redirect(redirect_url)
        return
        
    def oauth_callback(self, request_handler, **kw):
        
        auth = tweepy.OAuthHandler("5dMcC3yYelEVwQykbsitcA","63g7kzmNdJX25qVuz51RMUFXCwiJ7DKaeoMn3fLmlQ")
        auth.set_request_token(self.request_token[0], self.request_token[1])
        auth.get_access_token(kw.get('oauth_verifier'))
        
        import pdb;pdb.set_trace()
