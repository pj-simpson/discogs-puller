from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.repository.releases import release


class ReleasesController(Controller):
    path = "/releases"
    dependencies = {"release_context_data": Provide(release)}

    @get(path="/{release_id:int}")
    async def release_detail(
        self, release_context_data: Any, release_id: int
    ) -> Template:
        release = release_context_data
        return Template(
            name="releases/release_detail.html", context={"release": release}
        )
