import typing

import pytest

from app.dal.artists import ArtistDAL, ArtistDataCreator
from app.dal.releases import ReleaseDataCreator, ReleaseDAL


class TestArtistDataCreators:
    def test_artist_data_creator_init(self):
        artist_data_creator = ArtistDataCreator(artist_id=1)
        assert artist_data_creator.artist_id == 1

    @pytest.mark.asyncio
    async def test_artist_data_creator_produce_artist_data(
        self, monkeypatch, artist_factory
    ):

        monkeypatch.setattr(ArtistDataCreator, "produce_artist_data", artist_factory)
        artist_data_creator = ArtistDataCreator(artist_id=1)
        artist_data = await artist_data_creator.produce_artist_data()
        assert artist_data["name"] == "Rock Music Band"

    @pytest.mark.asyncio
    async def test_artist_data_creator_produce_artist_release_list_data(
        self, monkeypatch, artist_releases_factory
    ):

        monkeypatch.setattr(
            ArtistDataCreator,
            "produce_artist_release_list_data",
            artist_releases_factory,
        )
        artist_data_creator = ArtistDataCreator(artist_id=1)
        artist_release_list_data = (
            await artist_data_creator.produce_artist_release_list_data()
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

    @pytest.mark.asyncio
    async def test_artist_data_creator__get_artist_dict(
        self, monkeypatch, artist_factory
    ):
        monkeypatch.setattr(ArtistDAL, "get_single_artist", artist_factory)
        artist_data_creator = ArtistDataCreator(artist_id=1)
        single_artist = await artist_data_creator._get_artist_dict()
        assert single_artist["name"] == "Rock Music Band"

    @pytest.mark.asyncio
    async def test_artist_data_creator__get_artist_images_list(
        self, monkeypatch, artist_images_factory
    ):
        monkeypatch.setattr(ArtistDAL, "get_artist_images", artist_images_factory)
        artist_data_creator = ArtistDataCreator(artist_id=1)
        artist_image_list = await artist_data_creator._get_artist_images_list()
        assert artist_image_list[0]["height"] == "286"

    @pytest.mark.asyncio
    async def test_artist_data_creator__get_artist_release_list(
        self, monkeypatch, artist_releases_factory
    ):
        monkeypatch.setattr(
            ArtistDAL, "get_artist_release_list", artist_releases_factory
        )
        artist_data_creator = ArtistDataCreator(artist_id=1)
        artist_release_list = await artist_data_creator._get_artist_release_list()
        second_album = {
            "year": 2017,
            "external_id": 11243474,
            "title": "Generic Album",
            "artist_id": 1,
            "id": 2,
            "link": "https://api.discogs.com/masters/11243474",
            "artist_external_id": 3552343,
        }
        assert artist_release_list[1] == second_album


class TestReleaseDataCreators:
    def test_release_data_creator_init(self):
        release_data_creator = ReleaseDataCreator(release_id=1)
        assert release_data_creator.release_id == 1

    @pytest.mark.asyncio
    async def test_release_data_creator_produce_single_release_data(
        self, monkeypatch, single_release_factory
    ):

        monkeypatch.setattr(
            ReleaseDataCreator, "_get_single_release_dict", single_release_factory
        )
        release_data_creator = ReleaseDataCreator(release_id=1)
        single_release_data = await release_data_creator.produce_single_release_data()
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

    @pytest.mark.asyncio
    async def test_release_data_creator__get_single_release_dict(
        self, monkeypatch, single_release_factory
    ):
        monkeypatch.setattr(ReleaseDAL, "get_single_release", single_release_factory)
        release_data_creator = ReleaseDataCreator(release_id=1)
        single_release_dict = await release_data_creator._get_single_release_dict()
        single_release = {
            "year": 2022,
            "external_id": 5364894,
            "title": "Fantastic Album",
            "artist_id": 1,
            "link": "https://api.discogs.com/releases/5364894",
            "id": 4,
            "artist_external_id": 3552343,
        }
        assert single_release_dict == single_release
