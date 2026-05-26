import pytest
import os
SAMPLE_LOG = """
2025-05-18 09:01:02 INFO Service started: rfid-reader-daemon
2025-05-18 09:01:03 INFO Device ID: reader_01 registered
2025-05-18 09:01:04 INFO Firmware version: 2.1.4 loaded
2025-05-18 09:01:05 WARN Signal strength low: 34dBm
2025-05-18 09:01:06 INFO Provisioning complete: reader_01
2025-05-18 09:01:07 ERROR Network timeout on port 8883
"""
@pytest.fixture
def log_file(tmp_path):
    """Creates a temp log file — tmp_path is a built-in pytest fixture."""
    log = tmp_path / "device.log"
    log.write_text(SAMPLE_LOG)
    yield str(log)
# tmp_path auto-cleans up after test session
# Asserts the log contains a successful provisioning entry
def test_provisioning_success_logged(log_file):
    with open(log_file) as f:
      content = f.read()
      assert "Provisioning complete" in content

# Counts ERROR lines — assert there is exactly 1
def test_single_error_in_log(log_file):
    with open(log_file) as f:
       lines = f.readlines()
       error_lines = [line for line in lines if "ERROR" in line]   
       assert  len(error_lines) == 1

# Asserts no CRITICAL entries exist
def test_no_critical_errors(log_file):
    with open(log_file) as f:
        lines = f.readlines()
        critical_lines = [line for line in lines if "CRITICAL" in line]
        assert len(critical_lines) == 0
        
# Extracts the firmware version from the log and assert it's "2.1.4"
def test_firmware_version_logged_correctly(log_file):
    with open(log_file) as f:
        lines = f.readlines()
        firmware_line = [line for line in lines if "Firmware version" in line][0]
        assert firmware_line.split()[5] == "2.1.4"
    