from starlite import Starlite, TemplateConfig, StaticFilesConfig
from app.controllers.artists import ArtistController
from app.controllers.home import HomeController
from app.controllers.releases import ReleasesController
from app.health_check import health_check
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
    # static_files_config=[
    #     StaticFilesConfig(directories=["static"], path="/static"),
    # ],
    debug=os.environ.get("DEBUG", False),
)
