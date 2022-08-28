import pytest

from app.repository.artists import ArtistRepository, artist, artist_release_list
from app.repository.releases import ReleaseDataRepository, release


@pytest.mark.asyncio
async def test_get_artist_context_data(monkeypatch, artist_factory):

    monkeypatch.setattr(ArtistRepository, "get_artist_data", artist_factory)
    artist_context_data = await artist(artist_id=1)
    assert artist_context_data["name"] == "Rock Music Band"


@pytest.mark.asyncio
async def test_get_artist_release_list_context_data(
    monkeypatch, artist_releases_factory
):

    monkeypatch.setattr(
        ArtistRepository,
        "get_artist_release_list_data",
        artist_releases_factory,
    )
    artist_release_list_context_data = await artist_release_list(artist_id=1)
    second_album = {
        "year": 2017,
        "external_id": 11243474,
        "title": "Generic Album",
        "artist_id": 1,
        "id": 2,
        "link": "https://api.discogs.com/masters/11243474",
        "artist_external_id": 3552343,
    }
    assert artist_release_list_context_data[1] == second_album


@pytest.mark.asyncio
async def test_get_release_context_data(monkeypatch, single_release_factory):

    monkeypatch.setattr(
        ReleaseDataRepository, "get_single_release_data", single_release_factory
    )
    single_release_context_data = await release(release_id=1)
    single_release  = {
        "year": 2022,
        "external_id": 5364894,
        "title": "Fantastic Album",
        "artist_id": 1,
        "link": "https://api.discogs.com/releases/5364894",
        "id": 4,
        "artist_external_id": 3552343,
    }
    assert single_release_context_data == single_release
