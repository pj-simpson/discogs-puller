import aiosqlite


async def create_artist(band_details: str) -> None:
    """
    Checks whether or not an artist record already exists in our SQLite DB
    If it doesnt, it creates the relevant record.

    :param band_details: json of single artist details from the discogs API
    """
    band_name = band_details["name"]
    band_biography = band_details["profile"]
    discogs_external_band_id = band_details["id"]
    releases_uri = band_details["releases_url"]

    # this will enforce connection only if the file exists
    async with aiosqlite.connect("file:bands.db?mode=rw", uri=True) as db:
        check = await db.execute(
            f"""
            SELECT count(*) FROM artist 
            WHERE external_id={discogs_external_band_id}
            """
        )
        table_exists = await check.fetchone()
        if table_exists[0] == 0:
            await db.execute(
                """
                INSERT INTO artist (name, biog, external_id,releases_uri)
                VALUES(?,?,?,?);
                """,
                (band_name, band_biography, discogs_external_band_id, releases_uri),
            )
            await db.commit()
            await create_artist_images(band_details)

async def create_artist_images(band_details: str) -> None:
    """
    Creates the relevant records for artist images
    :param band_details: json of single artist details from the discogs API
    """
    band_images = band_details["images"]

    # TODO an asyncio.gather here?
    for image in band_images:

        # this will enforce connection only if the file exists
        async with aiosqlite.connect("file:bands.db?mode=rw", uri=True) as db:

            await db.execute(
                """
                INSERT INTO artist_images (width, height, uri,artist_id,artist_external_id)
                VALUES(?,?,?,?,?);
                """,
                # TODO bad hard coding artist unique identifier
                (image['width'],image['height'],image['uri'],1,band_details["id"]),
            )
            await db.commit()

async def create_release(release: str, artist_external_id: int) -> str:
    """
    Checks whether or not asingle releases has record already existing in our SQLite DB
    If it doesnt, it creates the relevant record.

    :param release: json of single artist's releases details from the discogs API
    """
    print(release)
    title = release["title"]
    year = release["year"]
    link = release["resource_url"]
    external_id = release["id"]

    # this will enforce connection only if the file exists
    async with aiosqlite.connect("file:bands.db?mode=rw", uri=True) as db:
        check = await db.execute(
            f"""
            SELECT count(*) FROM releases 
            WHERE external_id={external_id} AND artist_external_id= {artist_external_id}
            """
        )
        release_exists = await check.fetchone()
        if release_exists[0] == 0:
            # get our internal unique identifier for the artist
            get_internal_artist_id = await db.execute(
                f"""
                        SELECT id FROM artist 
                        WHERE external_id={artist_external_id}
                        """
            )
            artist_internal_id = await get_internal_artist_id.fetchone()
            # crete the record for the releases
            await db.execute(
                """
                INSERT INTO releases (title,year,link,external_id,artist_external_id,artist_id)
                VALUES(?,?,?,?,?,?);
                """,
                (
                    title,
                    year,
                    link,
                    external_id,
                    artist_external_id,
                    artist_internal_id[0],
                ),
            )
            await db.commit()
            # await create_release_images(release,artist_external_id)

async def create_release_images(release: str, artist_external_id: int) -> None:
    """
    Creates the relevant records for a releases images
    :param band_details: json of single artist details from the discogs API
    """
    release_images = release["images"]

    # TODO an asyncio.gather here?
    for image in release_images:

        # this will enforce connection only if the file exists
        async with aiosqlite.connect("file:bands.db?mode=rw", uri=True) as db:

            await db.execute(
                """
                INSERT INTO release_images (width, height, uri,artist_id,artist_external_id)
                VALUES(?,?,?,?,?);
                """,
                # TODO bad hard coding artist unique identifier
                (image['width'],image['height'],image['uri'],1,artist_external_id),
            )
            await db.commit()
