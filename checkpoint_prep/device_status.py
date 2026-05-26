def get_device_status(device_id):
    """Simulates a device status response."""
    devices = {
        "reader_01": {"online": True, "firmware": "2.1.4", "signal": 87},
        "reader_02": {"online": False, "firmware": "2.0.1", "signal": 0},
        "reader_03": {"online": True, "firmware": "2.1.4", "signal": 43},
    }
    return devices.get(device_id)
def get_active_devices(devices):
    return [d for d in devices if devices[d]["online"]]

import pytest
from device_status import get_device_status, get_active_devices
def test_online_device_returns_status():
    assert get_device_status("reader_01") is not None
def test_offline_device_signal_is_zero():
    assert get_device_status("reader_02")["signal"] == 0
def test_firmware_version_format():
    assert "." in get_device_status("reader_03")["firmware"]
def test_active_device_count():
    devices = {
        "reader_01": {"online": True, "firmware": "2.1.4", "signal": 87},
        "reader_02": {"online": False, "firmware": "2.0.1", "signal": 0},
    }
    assert len(get_active_devices(devices)) == 1
