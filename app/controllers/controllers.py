from starlite.controller import Controller
from starlite.handlers import get



class ArtistController(Controller):
    path = "/artist"

    @get(path="/{artist_id:int}")
    async def retrieve_user_order(self, artist_id: int) -> str:
        return {'echo':f'{artist_id}'}
