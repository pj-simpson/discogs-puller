from typing import Any

from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template, Provide

from app.dal.releases import ReleaseDAL


class ReleasesController(Controller):
    path = "/releases"
    dependencies = {"release_dal": Provide(ReleaseDAL)}

    @get(path="/{release_id:int}")
    async def release_detail(self, release_dal: Any, release_id: int) -> Template:
        release = await release_dal.get_single_release(release_id)
        return Template(
            name="releases/release_detail.html", context={"release": release}
        )
