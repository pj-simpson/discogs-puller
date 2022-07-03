from starlite.controller import Controller
from starlite.handlers import get
from starlite import Template

class ReleasesController(Controller):
    path = "/releases"

    @get(path="/{release_id:int}")
    async def release_detail(self, release_id: int) -> Template:
        return Template(name="releases/release_detail.html",context={'release_id':release_id})
