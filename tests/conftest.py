import pytest
from utilities.api_client import PoetryDBClient

@pytest.fixture
def api_client():
    """Fixture to provide a PoetryDB API client."""
    return PoetryDBClient()

@pytest.fixture
def expected_title():
    """Fixture for a known poem title to test with."""
    return "Ozymandias"

@pytest.fixture
def expected_author():
    """Fixture for a known poem author to test with."""
    return "William Shakespeare"

@pytest.fixture
def expected_winter_poems():
    """Fixture for expected Winter poem titles by Shakespeare."""
    return [
        "Winter",
        "Spring and Winter i",
        "Spring and Winter ii",
        "Blow, Blow, Thou Winter Wind",
        "Sonnet 2: When forty winters shall besiege thy brow"
    ] 