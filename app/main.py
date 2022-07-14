from starlite import Starlite, MediaType, TemplateConfig
from .controllers.artists import ArtistController
from .controllers.home import HomeController
from .controllers.releases import ReleasesController
from .health_check import health_check
from starlite.template.jinja import JinjaTemplateEngine
import os

app = Starlite(
    route_handlers=[
        health_check,
        HomeController,
        ArtistController,
        ReleasesController,
    ],
    template_config=TemplateConfig(
        directory="app/templates", engine=JinjaTemplateEngine
    ),
    debug=os.environ.get("DEBUG", False),
)
