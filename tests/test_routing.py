from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
import pytest

from app.dal import releases
from app.dal import artists


def test_artist_request_response(test_client,monkeypatch,artist_json):
    with test_client as client:
        monkeypatch.setattr(artists, 'get_artist_context_data', artist_json)
        response = client.get("/artist/1")
        assert response.status_code == HTTP_200_OK

def test_artist_releases_request_response(test_client,monkeypatch,artist_release_list):
    with test_client as client:
        monkeypatch.setattr(artists, 'get_artist_release_list_context_data', artist_release_list)
        response = client.get("/artist/1/releases")
        assert response.status_code == HTTP_200_OK

def test_release_detail_request_response(test_client,monkeypatch,single_release_detail):
    with test_client as client:
        monkeypatch.setattr(releases,'get_release_context_data',single_release_detail)
        response = client.get("/releases/1")
        assert response.status_code == HTTP_200_OK


def test_home_page(test_client):
    with test_client as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK

def test_non_existent_endpoint(test_client):
    with test_client as client:
        response = client.get("/something")
        assert response.status_code == HTTP_404_NOT_FOUND
