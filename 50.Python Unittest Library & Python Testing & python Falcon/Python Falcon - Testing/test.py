# test_myapp.py

from falcon import testing
import pytest
import myapp


@pytest.fixture()
def test_client():
    return testing.TestClient(myapp.create_app())


def test_get_message(test_client):
    expected_response = {'message': 'Hello, World!'}
    result = test_client.simulate_get('/')
    assert result.json == expected_response
