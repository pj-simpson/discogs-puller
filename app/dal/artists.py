from .base import BaseDAL
from sqlalchemy.future import select

from ..models.artists import Artist
from ..models.releases import Releases

import typing


class ArtistDAL(BaseDAL):
    async def get_single_artist(self) -> typing.Dict:
        async with self.session as session:
            result = await session.execute(select(Artist).where(Artist.id == 1))
            single_artist = await self._get_one_object_from_result(result, "Artist")
            return single_artist

    async def get_artist_release_list(self) -> typing.Dict:
        async with self.session as session:
            result = await session.execute(
                select(Releases).where(Releases.artist_id == 1)
            )
            release_list = await self._build_object_list_from_result(result, "Releases")
            return release_list
