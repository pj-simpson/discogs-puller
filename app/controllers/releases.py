from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.dal.releases import get_release_context_data


class ReleasesController(Controller):
    path = "/releases"
    dependencies = {"get_release_context_data": Provide(get_release_context_data)}

    @get(path="/{release_id:int}")
    async def release_detail(
        self, get_release_context_data: Any, release_id: int
    ) -> Template:
        release = get_release_context_data
        return Template(
            name="releases/release_detail.html", context={"release": release}
        )
