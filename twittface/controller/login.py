# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from twittface.models.usuario import Usuario
from torneira.core.meta import TorneiraSession
from sqlalchemy.orm.exc import NoResultFound
from tornado.web import HTTPError
import tweepy

import math
import settings

class LoginController(BaseController):
    
    request_token = None
    def index(self, request_handler):
        return self.render_to_template("login.html")
        
        
    def oauth(self, request_handler):
        
        auth = tweepy.OAuthHandler("5dMcC3yYelEVwQykbsitcA","63g7kzmNdJX25qVuz51RMUFXCwiJ7DKaeoMn3fLmlQ", "http://twittface.local:8080/login/oauth_callback")        
        redirect_url = auth.get_authorization_url()

        self.request_token = (auth.request_token.key, auth.request_token.secret)
        
        request_handler.redirect(redirect_url)
        return
        
    def oauth_callback(self, request_handler, **kw):
        
        auth = tweepy.OAuthHandler("5dMcC3yYelEVwQykbsitcA","63g7kzmNdJX25qVuz51RMUFXCwiJ7DKaeoMn3fLmlQ")
        auth.set_request_token(self.request_token[0], self.request_token[1])
        auth.get_access_token(kw.get('oauth_verifier'))
        
        api = tweepy.API(auth)
        user_twitter = api.me()
        
        session = TorneiraSession()
        try:
            usuario = session.query(Usuario).filter(Usuario.id_twitter==int(user_twitter.id)).one()
        except NoResultFound:
            usuario = Usuario()
            usuario.id_twitter = user_twitter.id
            usuario.image_url = user_twitter.profile_image_url
            usuario.save()
            
        request_handler.set_secure_cookie(name="TWITTFACE_ID", value=str(usuario.id), path="/", expires_days=None)        
        request_handler.redirect("/")
        return