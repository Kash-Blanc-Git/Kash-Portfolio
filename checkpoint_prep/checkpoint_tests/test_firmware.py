# TODO: Write 2 tests using base_config (no import needed)
# - test that device_id is a non-empty string
def test_device_id_not_empty(base_config):
    assert base_config["device_id"] is not None
    assert len(base_config["device_id"]) > 0
# - test that auth_token contains "test"
def test_auth_token_contents(base_config):
    assert "test" in base_config["auth_token"]