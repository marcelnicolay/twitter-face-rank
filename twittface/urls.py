from torneira.core.dispatcher import url
from twittface.controller.home import HomeController
from twittface.controller.login import LoginController

urls = (
    url("/", HomeController, action="", name="home"),    
    url("/login", LoginController, action="index", name="login_index"),    
    url("/login/oauth_callback", LoginController, action="oauth_callback", name="login_oauth_callback"),    
    
)
