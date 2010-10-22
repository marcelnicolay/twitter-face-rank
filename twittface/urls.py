from torneira.core.dispatcher import url
from twittface.controller.home import HomeController

urls = (
    url("/", HomeController, action="", name="home"),    
)
