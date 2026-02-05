from sqlalchemy import inspect
from sqlalchemy.orm import Session
from database import Base
from models import User


def test_table_exists():
    engine = Base.metadata.bind
    inspector = inspect(engine)
    assert "users" in inspector.get_table_names()


def test_session_local_insert_and_read(db_session):
    db: Session = db_session

    user = User(username="dbuser", password="pw123")
    db.add(user)
    db.commit()
    db.refresh(user)

    result = db.query(User).filter_by(username="dbuser").first()

    assert result is not None
    assert result.username == "dbuser"
