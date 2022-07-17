import typing

import pytest

from app.dal.artists import (
    get_artist_context_data,
    get_artist_release_list_context_data,
    ArtistDAL,
)
from app.dal.artists import ArtistDataCreator

## test the functions

# artists
from app.dal.releases import ReleaseDataCreator, get_release_context_data, ReleaseDAL


@pytest.mark.asyncio
async def test_get_artist_context_data(monkeypatch, produce_artist_json):

    monkeypatch.setattr(ArtistDataCreator, "produce_artist_data", produce_artist_json)
    artist_context_data = await get_artist_context_data(artist_id=1)
    assert artist_context_data["name"] == "Circuit Breaker (8)"


@pytest.mark.asyncio
async def test_get_artist_release_list_context_data(
    monkeypatch, produce_artist_release_list, single_release_detail
):

    monkeypatch.setattr(
        ArtistDataCreator,
        "produce_artist_release_list_data",
        produce_artist_release_list,
    )
    artist_release_list_context_data = await get_artist_release_list_context_data(
        artist_id=1
    )
    assert artist_release_list_context_data[3] == single_release_detail


#  releases


@pytest.mark.asyncio
async def test_get_release_context_data(
    monkeypatch, produce_single_release_detail, single_release_detail
):

    monkeypatch.setattr(
        ReleaseDataCreator, "produce_single_release_data", produce_single_release_detail
    )
    single_release_context_data = await get_release_context_data(release_id=1)
    assert single_release_context_data == single_release_detail


## test the data creators

#  artists
def test_artist_data_creator_init():
    artist_data_creator = ArtistDataCreator(artist_id=1)
    assert artist_data_creator.artist_id == 1


@pytest.mark.asyncio
async def test_artist_data_creator_produce_artist_data(
    monkeypatch, produce_artist_json
):

    monkeypatch.setattr(ArtistDataCreator, "produce_artist_data", produce_artist_json)
    artist_data_creator = ArtistDataCreator(artist_id=1)
    artist_data = await artist_data_creator.produce_artist_data()
    assert artist_data["name"] == "Circuit Breaker (8)"


@pytest.mark.asyncio
async def test_artist_data_creator_produce_artist_release_list_data(
    monkeypatch, produce_artist_release_list, single_release_detail
):

    monkeypatch.setattr(
        ArtistDataCreator,
        "produce_artist_release_list_data",
        produce_artist_release_list,
    )
    artist_data_creator = ArtistDataCreator(artist_id=1)
    artist_release_list_data = (
        await artist_data_creator.produce_artist_release_list_data()
    )
    assert artist_release_list_data[3] == single_release_detail


@pytest.mark.asyncio
async def test_artist_data_creator__get_artist_dict(monkeypatch, produce_artist_json):
    monkeypatch.setattr(ArtistDAL, "get_single_artist", produce_artist_json)
    artist_data_creator = ArtistDataCreator(artist_id=1)
    single_artist = await artist_data_creator._get_artist_dict()
    assert single_artist["name"] == "Circuit Breaker (8)"


@pytest.mark.asyncio
async def test_artist_data_creator__get_artist_images_list(
    monkeypatch, produce_artist_image_list
):
    monkeypatch.setattr(ArtistDAL, "get_artist_images", produce_artist_image_list)
    artist_data_creator = ArtistDataCreator(artist_id=1)
    artist_image_list = await artist_data_creator._get_artist_images_list()
    assert artist_image_list[0]["height"] == "286"


@pytest.mark.asyncio
async def test_artist_data_creator__get_artist_release_list(
    monkeypatch, produce_artist_release_list, single_release_detail
):
    monkeypatch.setattr(
        ArtistDAL, "get_artist_release_list", produce_artist_release_list
    )
    artist_data_creator = ArtistDataCreator(artist_id=1)
    artist_release_list = await artist_data_creator._get_artist_release_list()
    assert artist_release_list[3] == single_release_detail


#  releases


def test_release_data_creator_init():
    release_data_creator = ReleaseDataCreator(release_id=1)
    assert release_data_creator.release_id == 1


@pytest.mark.asyncio
async def test_release_data_creator_produce_single_release_data(
    monkeypatch, produce_single_release_detail, single_release_detail
):

    monkeypatch.setattr(
        ReleaseDataCreator, "_get_single_release_dict", produce_single_release_detail
    )
    release_data_creator = ReleaseDataCreator(release_id=1)
    single_release_data = await release_data_creator.produce_single_release_data()
    assert single_release_data == single_release_data


@pytest.mark.asyncio
async def test_release_data_creator__get_single_release_dict(
    monkeypatch, produce_single_release_detail, single_release_detail
):
    monkeypatch.setattr(ReleaseDAL, "get_single_release", produce_single_release_detail)
    release_data_creator = ReleaseDataCreator(release_id=1)
    single_release_dict = await release_data_creator._get_single_release_dict()
    assert single_release_dict == single_release_detail
