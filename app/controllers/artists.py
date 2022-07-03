from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template



class ArtistController(Controller):
    path = "/artist"

    @get(path="/{artist_id:int}")
    async def artist_detail(self, artist_id: int) -> Template:
        return Template(name="artist/artist.html",context={'artist_id':artist_id})

    @get(path="/{artist_id:int}/releases")
    async def artist_release_list(self, artist_id: int) -> Template:
        return Template(name="artist/release_list.html", context={'artist_id': artist_id})
