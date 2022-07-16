from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.dal.artists import get_artist_context_data, get_artist_release_list_context_data


class ArtistController(Controller):
    path = "/artist"
    dependencies = {
        "get_artist_context_data": Provide(get_artist_context_data),
        "get_artist_release_list_context_data": Provide(get_artist_release_list_context_data),

    }

    @get(path="/{artist_id:int}")
    async def artist_detail(self, get_artist_context_data: Any, artist_id: int) -> Template:
        artist = get_artist_context_data
        return Template(name="artist/artist.html", context={"artist": artist})

    @get(path="/{artist_id:int}/releases")
    async def artist_release_list(self, get_artist_release_list_context_data: Any, artist_id:int) -> Template:
        releases = get_artist_release_list_context_data
        return Template(name="artist/release_list.html", context={"releases": releases})
