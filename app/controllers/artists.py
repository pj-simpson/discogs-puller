from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from ..dal.artists import ArtistDAL


class ArtistController(Controller):
    path = "/artist"
    dependencies = {"artist_dal": Provide(ArtistDAL)}

    @get(path="/{artist_id:int}")
    async def artist_detail(self,artist_dal:Any, artist_id: int) -> Template:
        await artist_dal.get_single_artist()
        return Template(name="artist/artist.html",context={'artist_id':artist_id})

    @get(path="/{artist_id:int}/releases")
    async def artist_release_list(self,artist_dal:Any, artist_id: int) -> Template:
        await artist_dal.get_artist_release_list()
        return Template(name="artist/release_list.html", context={'artist_id': artist_id})
