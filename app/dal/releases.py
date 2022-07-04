from .base import BaseDAL
from sqlalchemy.future import select

from ..models.releases import Releases


class ReleaseDAL(BaseDAL):

    async def get_single_release(self,release_id):
        async with self.session as session:
            result = await session.execute(
                select(Releases).where(Releases.id == release_id)
            )
            release_result = result.mappings().one()
            release = release_result["Releases"]
