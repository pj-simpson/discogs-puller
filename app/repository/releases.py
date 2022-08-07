import typing

from app.database.releases import ReleaseDAL


class ReleaseDataRepository:
    def __init__(self) -> None:
        self.dal = ReleaseDAL()

    async def get_single_release_data(self, release_id: int) -> typing.Dict:
        release = await self.dal.get_single_release(release_id)
        return release


async def release(release_id: int) -> typing.Dict:
    release_data_creator = ReleaseDataRepository()
    single_release = await release_data_creator.get_single_release_data(release_id)
    return single_release
