# coding: utf-8
#!/usr/bin/env python

from twittface.controller import authenticated
from torneira.controller import BaseController, render_to_extension
import tweepy
import random

class SearchController(BaseController):
    
    @authenticated
    def result(self, usuario, request_handler, **kw):
        
        itens =  kw.get('itens') or 50
        page = kw.get('page') or 1
        palavra = kw.get('palavra')
        
        api = tweepy.API()
        
        result = api.search(q=palavra, page=page, rrd=itens, show_user=True)
        random.shuffle(result)
        
        response = {'tweets':[]}
        
        for t in result:
            response['tweets'].append({'id_twitter':t.from_user_id, 
                                        'image_url':t.profile_image_url,
                                        'name': t.from_user,
                                        'last_tweet': t.text})
            
        return self.render_to_json(response, request_handler)
        