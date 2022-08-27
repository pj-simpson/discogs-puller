import pytest
import os
from sqlalchemy.engine import ChunkedIteratorResult

from starlite.testing import TestClient

from app.main import app


@pytest.fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture(name="artist_factory", scope="session")
def artist_json_factory(*args, **kwargs):
    async def _produce_artist_json(*args, **kwargs):
        artist_json = {
            "name": "Rock Music Band",
            "biog": "Rock Music Band are, quite simply, THE greatest Rock Music band.",
            "external_id": 3552343,
            "id": 1,
            "releases_uri": "https://api.discogs.com/artists/3552343/releases",
            "images": [
                {
                    "id": 1,
                    "height": "296",
                    "artist_external_id": 3552343,
                    "uri": "https://i.discogs.com/fylHsufHKr6xQEMXJQnAvRnsJEMOI6fPUVBwdnLbd14/rs:fit/g:sm/q:90/h:296/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTA3/Mi02NDQyLmpwZWc.jpeg",
                    "width": "500",
                    "artist_id": 1,
                },
                {
                    "id": 2,
                    "height": "521",
                    "artist_external_id": 3552343,
                    "uri": "https://i.discogs.com/_wMMxjb4YJCURqAEUzAbFetptf2GpN5ntbtAGZ4Dgho/rs:fit/g:sm/q:90/h:521/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTE0/NS0yODA0LmpwZWc.jpeg",
                    "width": "600",
                    "artist_id": 1,
                },
            ],
        }
        return artist_json

    return _produce_artist_json


@pytest.fixture(name="artist_releases_factory", scope="session")
def artist_release_list_factory(*args, **kwargs):
    async def _produce_artist_release_list(*args, **kwargs):
        artist_release_list = [
            {
                "year": 2015,
                "external_id": 5096743,
                "title": "Album 1",
                "artist_id": 1,
                "id": 1,
                "link": "https://api.discogs.com/releases/5096743",
                "artist_external_id": 3552343,
            },
            {
                "year": 2017,
                "external_id": 11243474,
                "title": "Generic Album",
                "artist_id": 1,
                "id": 2,
                "link": "https://api.discogs.com/masters/11243474",
                "artist_external_id": 3552343,
            },
            {
                "year": 2018,
                "external_id": 11243474,
                "title": "Album after the Album",
                "artist_id": 1,
                "id": 3,
                "link": "https://api.discogs.com/releases/11243474",
                "artist_external_id": 3552343,
            },
        ]
        return artist_release_list

    return _produce_artist_release_list


@pytest.fixture(name="single_release_factory", scope="session")
def single_release_detail_factory(*args, **kwargs):
    async def _produce_single_release_detail(*args, **kwargs):
        single_release_detail = {
            "year": 2022,
            "external_id": 5364894,
            "title": "Fantastic Album",
            "artist_id": 1,
            "link": "https://api.discogs.com/releases/5364894",
            "id": 4,
            "artist_external_id": 3552343,
        }

        return single_release_detail

    return _produce_single_release_detail


@pytest.fixture(name="artist_images_factory", scope="session")
def artist_image_list_factory(*args, **kwargs):
    async def _produce_artist_image_list(*args, **kwargs):
        artist_image_list = [
            {
                "id": 1,
                "height": "286",
                "artist_external_id": 3552343,
                "uri": "https://i.discogs.com/fylHsufHKr6xQEMXJQnAvRnsJEMOI6fPUVBwdnLbd14/rs:fit/g:sm/q:90/h:296/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTA3/Mi02NDQyLmpwZWc.jpeg",
                "width": "500",
                "artist_id": 1,
            },
            {
                "id": 2,
                "height": "521",
                "artist_external_id": 3552343,
                "uri": "https://i.discogs.com/_wMMxjb4YJCURqAEUzAbFetptf2GpN5ntbtAGZ4Dgho/rs:fit/g:sm/q:90/h:521/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTE0/NS0yODA0LmpwZWc.jpeg",
                "width": "600",
                "artist_id": 1,
            },
        ]
        return artist_image_list

    return _produce_artist_image_list


@pytest.fixture(name="arbitrary_sqlalchemy_result_factory", scope="session")
def arbitrary_sqlalchemy_result_factory(*args, **kwargs):
    async def _produce_arbitrary_sqlalchemy_result_factory(*args, **kwargs):
        release = type("ArbitraryResult", (), dict())
        return release

    return _produce_arbitrary_sqlalchemy_result_factory


@pytest.fixture()
def set_up_temporary_database(tmp_path):
    os.system("cat tests/test_data_layer/backup.sql | sqlite3 test.db")
    os.system(f"mv test.db {tmp_path}")
    return tmp_path / "test.db"


@pytest.fixture()
def get_temporary_db_path_string(set_up_temporary_database):
    full_path_to_test_file = set_up_temporary_database
    return str(full_path_to_test_file)
