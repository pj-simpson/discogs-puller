import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.artists import ArtistDAL
from app.database.releases import ReleaseDAL


class TestReleasesDal:
    @pytest.mark.asyncio
    async def test_get_single_release(
        self, monkeypatch, arbitrary_sqlalchemy_result_factory, single_release_factory
    ):

        monkeypatch.setattr(
            AsyncSession, "execute", arbitrary_sqlalchemy_result_factory
        )
        monkeypatch.setattr(
            ReleaseDAL, "_get_one_object_from_result", single_release_factory
        )

        release_dal = ReleaseDAL()
        single_release = await release_dal.get_single_release(1)

        assert single_release == {
            "year": 2022,
            "external_id": 5364894,
            "title": "Fantastic Album",
            "artist_id": 1,
            "link": "https://api.discogs.com/releases/5364894",
            "id": 4,
            "artist_external_id": 3552343,
        }


class TestArtistDal:
    @pytest.mark.asyncio
    async def test_get_single_artist(
        self, monkeypatch, arbitrary_sqlalchemy_result_factory, artist_factory
    ):

        monkeypatch.setattr(
            AsyncSession, "execute", arbitrary_sqlalchemy_result_factory
        )
        monkeypatch.setattr(ArtistDAL, "_get_one_object_from_result", artist_factory)

        artist_dal = ArtistDAL()
        single_artist = await artist_dal.get_single_artist(1)

        assert single_artist["name"] == "Rock Music Band"

    @pytest.mark.asyncio
    async def test_get_artist_release_list(
        self, monkeypatch, arbitrary_sqlalchemy_result_factory, artist_releases_factory
    ):

        monkeypatch.setattr(
            AsyncSession, "execute", arbitrary_sqlalchemy_result_factory
        )
        monkeypatch.setattr(
            ArtistDAL, "_build_object_list_from_result", artist_releases_factory
        )

        artist_dal = ArtistDAL()
        release_list = await artist_dal.get_artist_release_list(1)

        assert len(release_list) == 3

    @pytest.mark.asyncio
    async def test_get_artist_images(
        self, monkeypatch, arbitrary_sqlalchemy_result_factory, artist_images_factory
    ):

        monkeypatch.setattr(
            AsyncSession, "execute", arbitrary_sqlalchemy_result_factory
        )
        monkeypatch.setattr(
            ArtistDAL, "_build_object_list_from_result", artist_images_factory
        )

        artist_dal = ArtistDAL()
        artist_images_list = await artist_dal.get_artist_images(1)

        assert len(artist_images_list) == 2
