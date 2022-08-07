import typing

from sqlalchemy.future import select

from app.database.base import BaseDAL
from app.models.artists import Artist, ArtistImage
from app.models.releases import Releases


class ArtistDAL(BaseDAL):
    async def get_single_artist(self, artist_id: int) -> typing.Dict:

        async with self.session as session:
            result = await session.execute(select(Artist).where(Artist.id == artist_id))
            single_artist = await self._get_one_object_from_result(result, "Artist")
            return single_artist

    async def get_artist_release_list(self, artist_id: int) -> typing.List:

        async with self.session as session:
            result = await session.execute(
                select(Releases).where(Releases.artist_id == artist_id)
            )
            release_list = await self._build_object_list_from_result(result, "Releases")
            return release_list

    async def get_artist_images(self, artist_id: int) -> typing.List:

        async with self.session as session:
            result = await session.execute(
                select(ArtistImage).where(ArtistImage.artist_id == artist_id)
            )
            artist_images_list = await self._build_object_list_from_result(
                result, "ArtistImage"
            )
            return artist_images_list
