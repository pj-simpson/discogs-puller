import typing

from app.database.base import BaseDAL

class ArtistDAL(BaseDAL):
    async def get_single_artist(self, artist_id: int) -> typing.Dict:
        a = {
            "name": "Circuit Breaker (7)",
            "biog": "Circuit Breaker are an Industrial band, consisting of London based brothers Peter and Edward Simpson. ",
            "external_id": 3552343,
            "id": 1,
            "releases_uri": "https://api.discogs.com/artists/3552343/releases",
        }
        return a

    # async with self.session as session:
    #     result = await session.execute(select(Artist).where(Artist.id == artist_id))
    #     single_artist = await self._get_one_object_from_result(result, "Artist")
    #     return single_artist

    async def get_artist_release_list(self, artist_id: int) -> typing.List:
        a = [
            {
                "year": 2013,
                "external_id": 5099743,
                "title": "Grid",
                "artist_id": 1,
                "id": 1,
                "link": "https://api.discogs.com/releases/5099743",
                "artist_external_id": 3552343,
            },
            {
                "year": 2017,
                "external_id": 1177776,
                "title": "Live Life",
                "artist_id": 1,
                "id": 2,
                "link": "https://api.discogs.com/masters/1177776",
                "artist_external_id": 3552343,
            },
            {
                "year": 2018,
                "external_id": 11243074,
                "title": "Hands Return To Shake",
                "artist_id": 1,
                "id": 3,
                "link": "https://api.discogs.com/releases/11243074",
                "artist_external_id": 3552343,
            },
            {
                "year": 2022,
                "external_id": 23646134,
                "title": "Spore City Survey",
                "artist_id": 1,
                "id": 4,
                "link": "https://api.discogs.com/releases/23646134",
                "artist_external_id": 3552343,
            },
            {
                "year": 2014,
                "external_id": 6109393,
                "title": "TV12 ",
                "artist_id": 1,
                "id": 5,
                "link": "https://api.discogs.com/releases/6109393",
                "artist_external_id": 3552343,
            },
            {
                "year": 2017,
                "external_id": 1155379,
                "title": "The Harbinger Sound Sampler",
                "artist_id": 1,
                "id": 6,
                "link": "https://api.discogs.com/masters/1155379",
                "artist_external_id": 3552343,
            },
            {
                "year": 2015,
                "external_id": 884186,
                "title": "My Descent Into Capital",
                "artist_id": 1,
                "id": 7,
                "link": "https://api.discogs.com/masters/884186",
                "artist_external_id": 3552343,
            },
            {
                "year": 2013,
                "external_id": 19910101,
                "title": "Cairn",
                "artist_id": 1,
                "id": 8,
                "link": "https://api.discogs.com/releases/19910101",
                "artist_external_id": 3552343,
            },
        ]
        return a
        # async with self.session as session:
        #     result = await session.execute(
        #         select(Releases).where(Releases.artist_id == artist_id)
        #     )
        #     release_list = await self._build_object_list_from_result(result, "Releases")
        #     return release_list

    async def get_artist_images(self, artist_id: int) -> typing.List:
        a = [
            {
                "id": 1,
                "height": "296",
                "artist_external_id": 3552343,
                "uri": "https://i.discogs.com/fylHsufHKr6xQEMXJQnAvRnsJEMOI6fPUVBwdnLbd14/rs:fit/g:sm/q:90/h:296/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTA3/Mi02NDQyLmpwZWc.jpeg",
                "width": "500",
                "artist_id": 1,
            },
            {
                "id": 2,
                "height": "521",
                "artist_external_id": 3552343,
                "uri": "https://i.discogs.com/_wMMxjb4YJCURqAEUzAbFetptf2GpN5ntbtAGZ4Dgho/rs:fit/g:sm/q:90/h:521/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTE0/NS0yODA0LmpwZWc.jpeg",
                "width": "600",
                "artist_id": 1,
            },
        ]
        return a
        # async with self.session as session:
        #     result = await session.execute(
        #         select(ArtistImage).where(ArtistImage.artist_id == artist_id)
        #     )
        #     artist_images_list = await self._build_object_list_from_result(result, "ArtistImage")
        #     return artist_images_list