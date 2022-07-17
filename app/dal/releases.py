import typing

from .base import BaseDAL
from sqlalchemy.future import select

from app.models.releases import Releases


class ReleaseDAL(BaseDAL):
    async def get_single_release(self, release_id):
        a = {
            "year": 2022,
            "external_id": 23646134,
            "title": "Spore City Survey",
            "artist_id": 1,
            "link": "https://api.discogs.com/releases/23646134",
            "id": 4,
            "artist_external_id": 3552343,
        }
        return a

        # async with self.session as session:
        #     result = await session.execute(
        #         select(Releases).where(Releases.id == release_id)
        #     )
        #     single_release = await self._get_one_object_from_result(result, "Releases")
        #     return single_release


class ReleaseDataCreator:
    def __init__(self, release_id: int) -> None:
        self.release_id = release_id

    async def _get_single_release_dict(self) -> typing.Dict:
        dal = ReleaseDAL()
        single_release_dict = await dal.get_single_release(self.release_id)
        return single_release_dict

    async def produce_single_release_data(self) -> typing.Dict:
        release = await self._get_single_release_dict()
        return release


async def get_release_context_data(release_id: int) -> typing.Dict:
    release_data_creator = ReleaseDataCreator(release_id)
    single_release = await release_data_creator.produce_single_release_data()
    return single_release
