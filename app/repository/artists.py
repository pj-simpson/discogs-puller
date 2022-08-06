from app.database.artists import ArtistDAL

import typing

class ArtistRepository:
    def __init__(self) -> None:
        self.dal = ArtistDAL()

    async def get_artist_data(self, artist_id: int) -> typing.Dict:
        artist = await self.dal.get_single_artist(artist_id)
        images = await self.dal.get_artist_images(artist_id)
        artist["images"] = images
        return artist

    async def get_artist_release_list_data(self, artist_id:int) -> typing.List:
        release_list = await self.dal.get_artist_release_list(artist_id)
        return release_list


async def artist(artist_id: int) -> typing.Dict:
    """
    Dependancy function for the controller to provide the context data upwards.
    """
    artist_data_creator = ArtistRepository()
    artist_data = await artist_data_creator.get_artist_data(artist_id)
    return artist_data


async def artist_release_list(artist_id: int) -> typing.List:
    """
    Dependancy function for the controller to provide the context data upwards.
    """
    artist_data_creator = ArtistRepository()
    artist_release_list = await artist_data_creator.get_artist_release_list_data(artist_id)
    return artist_release_list
