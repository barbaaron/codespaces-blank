import pytest

@pytest.fixture
def fix():
    yield 'test'