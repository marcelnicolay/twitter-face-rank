# coding: utf-8
#!/usr/bin/env python

from torneira.controller import BaseController, render_to_extension
from tornado.web import HTTPError

import math
import settings

class HomeController(BaseController):
    
    def index(self, request_handler):
        
        return self.render_to_template("home.html")
