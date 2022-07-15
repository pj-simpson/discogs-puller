from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


# once I hook in a data base, will need to mock the DB layer to keep these meaningful
def test_artist_request_response(test_client):
    with test_client as client:
        response = client.get("/artist/1")
        assert response.status_code == HTTP_200_OK

def test_artist_releases_request_response(test_client):
    with test_client as client:
        response = client.get("/artist/1/releases")
        assert response.status_code == HTTP_200_OK

def test_release_detail_request_response(test_client):
    with test_client as client:
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
