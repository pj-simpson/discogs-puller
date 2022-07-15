import asyncio
import typing

import aiohttp
import aiosqlite

from db_table_creation import create_artist_table, create_releases_table
from db_table_population import create_artist, create_release
from discogs_api_fetch import get_artist_details, get_artist_releases
from get_env_variables import get_discogs_token, get_discogs_artist_id

async def get_artist_release_uri(band_details: int) -> str:
    """
    Fetches an artist's releases URI from our SQLite DB

    :param artist_id: number representing the artist id in the discogs API
    """
    async with aiosqlite.connect("bands.db") as db:
        async with db.execute(
            f"""
            SELECT releases_uri FROM artist 
            WHERE external_id = {band_details}
            """
        ) as cursor:
            row = await cursor.fetchone()
            releases_uri = row[0]
            return releases_uri

async def main() -> None:
    """
    Fetches the details for the band 'Circuit Breaker' from the Discogs.com API and their releases history.
    Pushes the data into a SQLite DB.
    """
    DISCOGS_ARTIST_ID = get_discogs_artist_id()
    HEADERS = {"Authorization" : f"Discogs token={get_discogs_token()}"}


    await create_artist_table()
    artist_details = await get_artist_details(DISCOGS_ARTIST_ID, headers=HEADERS)
    await create_artist(artist_details)
    await create_releases_table()
    artist_release_uri = await get_artist_release_uri(DISCOGS_ARTIST_ID)
    artist_releases = await get_artist_releases(artist_release_uri, headers=HEADERS)

    # This should be where most of the 'gains' from concurrency happen.
    tasks = []
    for release in artist_releases:
        tasks.append(create_release(release, DISCOGS_ARTIST_ID))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
