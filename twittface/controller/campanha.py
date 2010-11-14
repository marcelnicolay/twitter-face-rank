# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError
from twittface.models.campanha import Campanha 

import settings

class CampanhaController(BaseController):

    def lista(self, request_handler):
        campanha = Campanha()
        retorno = campanha.listaCandidatas()
        return self.render_to_json({'campanhas':retorno}, request_handler)

    def voto(self, request_handler, id):
        campanha = Campanha()
        retorno = campanha.votar(id)
        request_handler.redirect("/campanha/lista")
        return
