import aiosqlite


async def create_artist_table() -> None:
    """
    Checks to see whether or not the Artist table exists in the SQLiteDB.
    Creates if it doesn't
    """
    async with aiosqlite.connect("bands.db") as db:
        check = await db.execute(
            """
            SELECT count(name) FROM sqlite_master 
            WHERE type='table' 
            AND name='artist'
            """
        )
        table_exists = await check.fetchone()
        if table_exists[0] == 0:
            await db.execute(
                """
                CREATE TABLE artist (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                biog TEXT NOT NULL,
                releases_uri TEXT NOT NULL,
                external_id INTEGER NOT NULL
            );
            """
            )
            await db.commit()
            # nasty way to deal with a dependancy... TODO refactor!
            await create_artist_image_table()


async def create_artist_image_table() -> None:
    """
    Checks to see whether or not the Artist image table exists in the SQLiteDB.
    Creates if it doesn't
    """
    async with aiosqlite.connect("bands.db") as db:
        check = await db.execute(
            """
            SELECT count(name) FROM sqlite_master 
            WHERE type='table' 
            AND name='artist_images'
            """
        )
        table_exists = await check.fetchone()
        if table_exists[0] == 0:
            await db.execute(
                """
                CREATE TABLE artist_images (
                id INTEGER PRIMARY KEY,
                width TEXT NOT NULL,
                height TEXT NOT NULL,
                uri TEXT NOT NULL,
                artist_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,

                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
            """
            )
            await db.commit()


async def create_releases_table():
    """
    Checks to see whether or not the Releases table exists in the SQLiteDB.
    Creates if it doesn't
    """
    async with aiosqlite.connect("bands.db") as db:
        check = await db.execute(
            """
            SELECT count(name) FROM sqlite_master 
            WHERE type='table' 
            AND name='releases'
            """
        )
        table_exists = await check.fetchone()
        if table_exists[0] == 0:
            await db.execute(
                """
                CREATE TABLE releases (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                year INTEGER NOT NULL,
                link TEXT NOT NULL , 
                external_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,
                artist_id INTEGER NOT NULL,

                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
            """
            )
            await db.commit()
            # nasty way to deal with a dependancy... TODO refactor!
            await create_releases_image_table()


async def create_releases_image_table() -> None:
    """
    Checks to see whether or not the Release image table exists in the SQLiteDB.
    Creates if it doesn't
    """
    async with aiosqlite.connect("bands.db") as db:
        check = await db.execute(
            """
            SELECT count(name) FROM sqlite_master 
            WHERE type='table' 
            AND name='release_images'
            """
        )
        table_exists = await check.fetchone()
        if table_exists[0] == 0:
            await db.execute(
                """
                CREATE TABLE release_images (
                id INTEGER PRIMARY KEY,
                width TEXT NOT NULL,
                height TEXT NOT NULL,
                uri TEXT NOT NULL,
                release_id INTEGER NOT NULL,
                artist_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,

                FOREIGN KEY (release_id) REFERENCES release (id),
                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
            """
            )
            await db.commit()
