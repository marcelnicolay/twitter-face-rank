# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError
from twittface.controller import authenticated

import math
import settings

class HomeController(BaseController):
    
    @authenticated
    def index(self, request_handler):
        
        return self.render_to_template("home.html")