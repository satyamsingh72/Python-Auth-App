import pytest
from sqlalchemy.orm import Session
from models import User
from database import Base
from sqlalchemy import inspect

# NOTE:
# We no longer create a separate engine or SQLite file.
# conftest.py already provides:
# - in-memory DB
# - TestingSessionLocal
# - reset_tables() before each test


@pytest.fixture
def db(override_get_db):
    """Get a fresh DB session from the overridden dependency."""
    return next(override_get_db())


def test_user_model_create(db: Session):
    user = User(username="testuser", password="hashedpw123")
    db.add(user)
    db.commit()
    db.refresh(user)

    assert user.id is not None
    assert user.username == "testuser"
    assert user.password == "hashedpw123"


def test_user_model_unique_username(db: Session):
    user1 = User(username="alex", password="pass1")
    db.add(user1)
    db.commit()

    user2 = User(username="alex", password="pass2")

    with pytest.raises(Exception):
        db.add(user2)
        db.commit()


def test_user_query(db: Session):
    user = User(username="queryuser", password="pw")
    db.add(user)
    db.commit()

    fetched = db.query(User).filter_by(username="queryuser").first()

    assert fetched is not None
    assert fetched.username == "queryuser"