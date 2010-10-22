# coding: utf-8
#!/usr/bin/env python

from twittface.util import signature 
from twittface.models.usuario import Usuario
from tornado.web import HTTPError
from torneira.core.meta import TorneiraSession

import logging

def authenticated(fn):
    def authenticated_fn(self, *args, **kwargs):
        
        request_handler = kwargs.get('request_handler')
        auth = request_handler.get_secure_cookie("TWITTFACE_ID")
        usuario = None
        
        if auth:
            usuario_id = signature.get_secure_value(auth)
            if usuario_id:
                usuario = Usuario().get(int(usuario_id))
        
        if usuario:
            return fn(self, usuario, *args, **kwargs)
        else:
            raise HTTPError(401)
    return authenticated_fn
