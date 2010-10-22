# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError
from twittface.models.voto import Voto 

import math
import settings
import datetime

class VotoController(BaseController):
    CONTEXT = ""
    
    def index(self, request_handler, **kw):
        resuSet = (None, "success", "error")
        retorno = {"result": resuSet[0], "message":"Nenhuma alteração efetuada"}
        
        if kw and kw['eleitor'] and kw['candidato'] and kw['nota']:
            if kw['nota'].isdigit() and int(float(kw['nota'])) > 0 and int(float(kw['nota'])) <=5:
                v = Voto()
                v.user = kw['eleitor']
                v.target = kw['candidato']
                v.rating = kw['nota']
                v.context = self.CONTEXT
                v.data = datetime.datetime.now()

                try:
                    v.save()
                    retorno = {"result": resuSet[1], "message":None}
                except Exception, e:
                    print "*"*80
                    print "Erro: %s" % e
                    print "*"*80
                    retorno = {"result": resuSet[2], "message":"Erro ao salvar o voto"}
            else:
                retorno = {"result": resuSet[2], "message":"Nota inválida"}
        else:
            retorno = {"result": resuSet[2], "message":"Dados incompletos"}
        
        return self.render_to_json(retorno, request_handler)






    def create(self, request_handler, **kw):
        return self.render_to_json({}, request_handler)
