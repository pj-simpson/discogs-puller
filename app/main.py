from starlite import Starlite, MediaType,TemplateConfig
from .controllers.artists import ArtistController
from .controllers.releases import ReleasesController
from .health_check import health_check
from starlite.template.jinja import JinjaTemplateEngine


app = Starlite(
    route_handlers=[
        health_check,
        ArtistController,
        ReleasesController,
    ],
    template_config=TemplateConfig(directory='app/templates',engine=JinjaTemplateEngine),
    debug=True)
