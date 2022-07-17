import typing

import aiohttp


async def get_artist_details(artist_id: int, headers) -> str:
    """
    Fetches an artists information from the discogs API

    :param artist_id: number representing the artist id in the discogs API
    :return: discogs API json representing a single artist
    """
    print(headers)
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.discogs.com/artists/{artist_id}", headers=headers
        ) as resp:
            result = await resp.json(content_type=None)
            return result


async def get_artist_releases(releases_uri: str, headers: typing.Dict) -> str:
    """
    Fetches an artist's releases information from the discogs API

    :param releases_uri: url of the resource at the Discogs end.
    :return: discogs API json representing a single artist
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(releases_uri, headers=headers) as resp:
            result = await resp.json(content_type=None)
            return result["releases"]
