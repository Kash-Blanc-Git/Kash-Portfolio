# 2 tests using base_config (no import needed)
# - tests that api_base_url starts with "http"

def test_api_base_url_type(base_config):
    assert "http://" in base_config["api_base_url"]
    
# - tests that timeout is greater than 0
def test_timeout_greater_than_0(base_config):
    assert base_config["timeout"] > 0