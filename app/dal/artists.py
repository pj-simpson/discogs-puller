from .base import BaseDAL
from sqlalchemy.future import select

from ..models.artists import Artist
from ..models.releases import Releases


class ArtistDAL(BaseDAL):

    async def get_single_artist(self):
        async with self.session as session:
            result = await session.execute(select(Artist).where(Artist.id == 1))
            artist_result = result.mappings().one()
            artist = artist_result["Artist"]

    async def get_artist_release_list(self):
        async with self.session as session:
            result = await session.execute(
                select(Releases).where(Releases.artist_id == 1)
            )
            release_result = result.mappings().all()
            release_list = []
            for item in release_result:
                release = item["Releases"]
                release_list.append(release.resp_for_json())
