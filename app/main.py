from starlite import Starlite, MediaType
from .controllers.controllers import ArtistController
from starlite.handlers import get


@get(path="/",media_type=MediaType.TEXT)
def health_check() -> str:
    return "healthy"

app = Starlite(route_handlers=[health_check,ArtistController],debug=True)
