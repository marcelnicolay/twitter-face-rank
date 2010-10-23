from torneira.core.dispatcher import url
from twittface.controller.home import HomeController
from twittface.controller.voto import VotoController
from twittface.controller.login import LoginController
from twittface.controller.search import SearchController

urls = (
    url("/", HomeController, action="", name="home"),    
    url("/voto", VotoController, action="", name=""),
    url("/login", LoginController, action="index", name="login_index"),    
    url("/logout", LoginController, action="logout", name="login_logout"),    
    url("/login/oauth", LoginController, action="oauth", name="login_oauth"),    
    url("/login/oauth_callback", LoginController, action="oauth_callback", name="login_oauth_callback"),    
    
    
    url("/search/result.json", SearchController, action="result", name=""),
)
