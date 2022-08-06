from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
import pytest

from app.repository import releases
from app.repository import artists


class TestHttpRouting:
    def test_artist_request_response(self, test_client, monkeypatch, artist_factory):
        with test_client as client:
            monkeypatch.setattr(artists, "artist", artist_factory)
            response = client.get("/artist/1")
            assert response.status_code == HTTP_200_OK

    def test_artist_releases_request_response(
        self, test_client, monkeypatch, artist_releases_factory
    ):
        with test_client as client:
            monkeypatch.setattr(artists, "artist_release_list", artist_releases_factory)
            response = client.get("/artist/1/releases")
            assert response.status_code == HTTP_200_OK

    def test_release_detail_request_response(
        self, test_client, monkeypatch, single_release_factory
    ):
        with test_client as client:
            monkeypatch.setattr(releases, "release", single_release_factory)
            response = client.get("/releases/1")
            assert response.status_code == HTTP_200_OK

    def test_home_page(self, test_client):
        with test_client as client:
            response = client.get("/")
            assert response.status_code == HTTP_200_OK

    def test_non_existent_endpoint(self, test_client):
        with test_client as client:
            response = client.get("/something")
            assert response.status_code == HTTP_404_NOT_FOUND
