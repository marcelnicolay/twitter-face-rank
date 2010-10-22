from torneira.core.dispatcher import url

urls = (
    url("/", HomeController, action="", name="home"),
    
)
