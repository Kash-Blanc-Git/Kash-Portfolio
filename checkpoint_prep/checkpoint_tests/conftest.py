import pytest

@pytest.fixture
def base_config():
  return {
    "api_base_url": "http://device-mgmt.local/api/v1",
    "auth_token": "test-token-abc123",
    "timeout": 10,
    "device_id": "reader_01"
}
