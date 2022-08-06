import typing

import pytest

from app.repository.artists import ArtistDAL, ArtistRepository
from app.repository.releases import ReleaseDataRepository, ReleaseDAL


class TestArtistDataCreators:

    @pytest.mark.asyncio
    async def test_artist_repository_init(self):
        artist_data_creator = ArtistRepository()
        assert type(artist_data_creator.dal) == ArtistDAL

    @pytest.mark.asyncio
    async def test_artist_repository_get_artist_data(
        self, monkeypatch, artist_factory
    ):

        monkeypatch.setattr(ArtistRepository, "get_artist_data", artist_factory)
        artist_data_creator = ArtistRepository()
        artist_data = await artist_data_creator.get_artist_data(artist_id=1)
        assert artist_data["name"] == "Rock Music Band"

    @pytest.mark.asyncio
    async def test_artist_repository_get_artist_release_list_data(
        self, monkeypatch, artist_releases_factory
    ):

        monkeypatch.setattr(
            ArtistRepository,
            "get_artist_release_list_data",
            artist_releases_factory,
        )
        artist_data_creator = ArtistRepository()
        artist_release_list_data = (
            await artist_data_creator.get_artist_release_list_data(artist_id=1)
        )
        second_album = {
            "year": 2017,
            "external_id": 11243474,
            "title": "Generic Album",
            "artist_id": 1,
            "id": 2,
            "link": "https://api.discogs.com/masters/11243474",
            "artist_external_id": 3552343,
        }
        assert artist_release_list_data[1] == second_album



class TestReleaseDataCreators:

    @pytest.mark.asyncio
    async def test_release_data_repository_init(self):
        release_data_creator = ReleaseDataRepository()
        assert type(release_data_creator.dal) == ReleaseDAL

    @pytest.mark.asyncio
    async def test_release_data_repository_get_single_release_data(
        self, monkeypatch, single_release_factory
    ):

        monkeypatch.setattr(
            ReleaseDataRepository, "get_single_release_data", single_release_factory
        )
        release_data_creator = ReleaseDataRepository()
        single_release_data = await release_data_creator.get_single_release_data(release_id=1)
        single_release = {
            "year": 2022,
            "external_id": 5364894,
            "title": "Fantastic Album",
            "artist_id": 1,
            "link": "https://api.discogs.com/releases/5364894",
            "id": 4,
            "artist_external_id": 3552343,
        }
        assert single_release_data == single_release