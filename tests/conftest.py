# tests/conftest.py
import pytest
from tinydb import TinyDB, Storage
from tinydb.storages import MemoryStorage
from app.main import app, db_file
from fastapi.testclient import TestClient

@pytest.fixture(scope="function")
def test_app():
    # Use in-memory DB
    app.dependency_overrides[db_file] = lambda: TinyDB(storage=MemoryStorage)
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}
