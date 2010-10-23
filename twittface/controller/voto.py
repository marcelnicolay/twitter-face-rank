# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError
from twittface.models.voto import Voto 
import tweepy

import math
import settings
import datetime

class VotoController(BaseController):
    CONTEXT = ""
    
    def create(self, request_handler, **kw):
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
                    retorno = {"result": resuSet[1], "message":"Voto efetuado com sucesso!"}
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
    
    
    def random_target(self, request_handler):
        
        retorno = [
                   {"id_twitter":234L, "image_url":"http://www.blogbrasil.com.br/wp-content/uploads/2009/05/andressa-soares-a-mulher-melancia-do-brasil.jpg", "last_tweet":"qqre porra"},
                    {"id_twitter":234L, "image_url":"http://www.blogbrasil.com.br/wp-content/uploads/2009/03/regina-krilow-ganhadora-do-concurso-menina-fantastica.jpg", "last_tweet":"qqre porra"},
                    {"id_twitter":234L, "image_url":"http://www.maisacao.net/blog/wp-content/uploads/2009/05/menina_maisa_cai_no_choro_durante_programa_deste_domingo_blog.jpg", "last_tweet":"qqre porra"},
                    {"id_twitter":234L, "image_url":"http://peganaminhaebalanca.files.wordpress.com/2007/08/200_mulher_samambaia2.jpg", "last_tweet":"qqre porra"},
                    {"id_twitter":234L, "image_url":"http://arquidiocesedecampogrande.org.br/arq/images/stories/mulher5.jpg", "last_tweet":"qqre porra"}
                ]

        
        return self.render_to_json(retorno, request_handler)
    



