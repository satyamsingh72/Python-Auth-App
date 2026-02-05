from auth import create_token, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import datetime, timedelta

def test_token_creation():
    token = create_token("john")

    # Should return a string
    assert isinstance(token, str)
    assert len(token) > 20  # basic sanity check


def test_token_decoding():
    username = "john"
    token = create_token(username)

    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # Verify token payload contains username
    assert decoded["sub"] == username


def test_token_expiry_is_set():
    token = create_token("john")
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    # exp should exist and be in future
    assert "exp" in decoded
    exp_time = datetime.utcfromtimestamp(decoded["exp"])
    assert exp_time > datetime.utcnow()


def test_token_expiry_2_hours():
    token = create_token("john")
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    exp_time = datetime.utcfromtimestamp(decoded["exp"])
    now = datetime.utcnow()

    # Difference should be close to 2 hours
    diff = exp_time - now
    # Allow ± few seconds since tests run fast
    assert timedelta(hours=1, minutes=59) < diff < timedelta(hours=2, minutes=1)
