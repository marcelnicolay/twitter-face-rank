from torneira.core.dispatcher import url
from twittface.controller.home import HomeController
from twittface.controller.voto import VotoController

urls = (
    url("/", HomeController, action="", name="home"),    
    url("/voto", VotoController, action="", name=""),
)
