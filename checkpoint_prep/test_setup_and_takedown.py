import pytest
CLIENT_CONFIG = {
"host": "192.168.1.100", #actual data wouldn't be hardcoded
"port": 8080,
"timeout": 30,
"connected": True
}

@pytest.fixture
def device_client():
    client = CLIENT_CONFIG
    yield client
# teardown
print("Teardown: client closed")

def test_client_host(device_client):
    assert device_client["host"] == "192.168.1.100" #actual data wouldn't be hardcoded

def test_client_is_connected(device_client):
    assert device_client["connected"] == True