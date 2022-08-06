from app.database.base import BaseDAL


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