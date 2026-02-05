from auth import create_token

def test_create_token():
    token = create_token("testuser")
    assert isinstance(token, str)
    assert len(token) > 10  # token should not be empty