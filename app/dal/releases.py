from .base import BaseDAL
from sqlalchemy.future import select

from app.models.releases import Releases


class ReleaseDAL(BaseDAL):
    async def get_single_release(self, release_id):
        async with self.session as session:
            result = await session.execute(
                select(Releases).where(Releases.id == release_id)
            )
            single_release = await self._get_one_object_from_result(result, "Releases")
            return single_release
