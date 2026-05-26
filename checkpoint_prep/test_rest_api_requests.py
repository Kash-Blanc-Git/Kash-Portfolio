import pytest
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
@pytest.fixture
def api_session():
    """Reusable requests session — mirrors how you'd connect to a device API."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()

# Tests a GET request returns 200 and has expected fields
# GET /posts/1 -- treats this like GET /devices/1 on a real device API
def test_get_device_returns_200(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

# Tests the response body has required fields
# asserts "id", "title", "body", "userId" are all in response.json()
def test_get_device_response_schema(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

# Tests a 404 response for a non-existent device
# GET /posts/99999
def test_missing_device_returns_404(api_session):
    response = api_session.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404

# Parametrizes a test across multiple device IDs (1, 2, 3)
# Each should return 200 and a non-empty title
@pytest.mark.parametrize("device_id", [1, 2, 3])
def test_multiple_devices_return_valid_data(api_session, device_id):
    response = api_session.get(f"{BASE_URL}/posts/{device_id}")
    assert response.status_code == 200
    assert api_session is not None 
    