from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.dal.artists import (
    artist,
    artist_release_list,
)


class ArtistController(Controller):
    path = "/artist"
    dependencies = {
        "artist_context_data": Provide(artist),
        "artist_release_list_context_data": Provide(artist_release_list),
    }

    @get(path="/{artist_id:int}")
    async def artist_detail(self, artist_context_data: Any, artist_id: int) -> Template:
        artist = artist_context_data
        return Template(name="artist/artist.html", context={"artist": artist})

    @get(path="/{artist_id:int}/releases")
    async def artist_release_list(
        self, artist_release_list_context_data: Any, artist_id: int
    ) -> Template:
        releases = artist_release_list_context_data
        return Template(name="artist/release_list.html", context={"releases": releases})
