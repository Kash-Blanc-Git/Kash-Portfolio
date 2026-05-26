import pytest
import sys

# Skips this test unconditionally with reason
@pytest.mark.skip(reason="Reader provisioning API not yet implemented")
def test_device_provisioning():
    assert False # would fail anyway

# Marks as expected to fail (xfail) with reason
@pytest.mark.xfail(reason="Bug CHK-442: signal drops to -1 on firmware 2.0.x")
def test_signal_never_negative():
    signal = -1 # simulating the known bug
    assert signal >= 0

# Applies a custom marker @pytest.mark.hardware
# to this test, then run: pytest -v -m hardware
# (only this test should run)
@pytest.mark.hardware
def test_rfid_read_range():
# simulates a test that needs physical hardware
    assert True

# Conditionally skips based on OS
# Skip if not running on Linux (embedded devices run Linux)
@pytest.mark.skipif(sys.platform != "linux", reason="Not Linux system")
def test_systemd_service_active():
    assert sys.platform == "linux"
