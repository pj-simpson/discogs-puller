from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.dal.artists import ArtistDAL


class ArtistController(Controller):
    path = "/artist"
    dependencies = {"artist_dal": Provide(ArtistDAL)}

    @get(path="/{artist_id:int}")
    async def artist_detail(self, artist_dal: Any, artist_id: int) -> Template:
        artist = await artist_dal.get_single_artist(artist_id)
        images = await artist_dal.get_artist_images(artist_id)
        return Template(name="artist/artist.html", context={"artist": artist,"images":images})

    @get(path="/{artist_id:int}/releases")
    async def artist_release_list(self, artist_dal: Any, artist_id: int=1) -> Template:
        releases = await artist_dal.get_artist_release_list(artist_id)
        return Template(name="artist/release_list.html", context={"releases": releases})
