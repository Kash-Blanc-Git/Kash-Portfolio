import pytest
import re
def is_valid_firmware(version):
    """Returns True if firmware matches format: digits.digits.digits"""
    pattern = r"^\d+\.\d+\.\d+$"
    return bool(re.match(pattern, version))

@pytest.mark.parametrize("version, expected", [
    ("2.1.14", True),
    ("10.0.1", True),
    ("1.0.0", True),
    ("abc", False),
    ("2.1", False),
    ("2.1.4.5", False),
])
def test_firmware_format(version, expected):
    assert is_valid_firmware(version) == expected