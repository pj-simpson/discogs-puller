from starlette.status import HTTP_200_OK


def test_health_check(test_client):
    with test_client as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert response.text == "healthy"

