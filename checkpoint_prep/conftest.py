import pytest
def pytest_configure(config):
    config.addinivalue_line(
    "markers", "hardware: marks tests requiring physical device"
)