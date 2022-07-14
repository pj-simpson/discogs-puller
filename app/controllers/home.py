from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template


class HomeController(Controller):
    path = "/"

    @get(path="/")
    async def home_page(self) -> Template:
        return Template(name="home.html")
