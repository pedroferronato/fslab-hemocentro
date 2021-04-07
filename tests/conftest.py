from app import flaskApp
import pytest

@pytest.fixture
def client():
    return flaskApp