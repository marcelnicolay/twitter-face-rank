# coding: utf-8
#!/usr/bin/env python

from twittface.models.usuario import Usuario
from tornado.web import HTTPError
from torneira.core.meta import TorneiraSession

import logging

def authenticated(fn):
    def authenticated_fn(self, *args, **kwargs):
        
        request_handler = kwargs.get('request_handler')
        usuario_id = request_handler.get_secure_cookie("TWITTFACE_ID")
        usuario = None
        
        if usuario_id:
            usuario = Usuario().get(int(usuario_id))
        
        if usuario:
            return fn(self, usuario, *args, **kwargs)
        else:
            request_handler.redirect("/login")
            return
            
    return authenticated_fn
