import pytest
@pytest.fixture(scope="function") # re-runs for every test
def function_scoped_db():
    print("\n[SETUP] function-scoped DB connection")
    db = {"connection": "active", "records": 42}
    yield db
    print("[TEARDOWN] function-scoped DB closed")

@pytest.fixture(scope="module") # runs once for the whole file
def module_scoped_db():
    print("\n[SETUP] module-scoped DB connection")
    db = {"connection": "active", "records": 42}
    yield db
    print("[TEARDOWN] module-scoped DB closed")

def test_function_connection_active(function_scoped_db):
    assert function_scoped_db["connection"] == "active"

def test_function_records_greater_than_40(function_scoped_db):
    assert function_scoped_db["records"] >= 40

def test_db_has_required_keys(function_scoped_db):
    assert "connection" in function_scoped_db
    assert "records" in function_scoped_db

def test_module_connection_active(module_scoped_db):
    assert module_scoped_db["connection"] == "active"

def test_module_records_greater_than_41(module_scoped_db):
    assert module_scoped_db["records"] >= 41

def test_module_state_persists(module_scoped_db):
    module_scoped_db["records"] = 999
    assert module_scoped_db["records"] == 999