import sys, os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Allow Jenkins to import main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app, get_db
from database import Base

# --------------------------
# Test DB
# --------------------------
TEST_DB_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DB_URL, connect_args={"check_same_thread": False}
)

Base.metadata.bind = engine
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fresh tables for every test run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# --------------------------
# 1️⃣ OVERRIDE DB FOR FASTAPI
# --------------------------
@pytest.fixture
def override_get_db():
    def _override():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    return _override


@pytest.fixture
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


# --------------------------
# 2️⃣ A RAW DB SESSION FIXTURE FOR DB TESTS
# --------------------------
@pytest.fixture
def db_session():
    """Return an actual session for database-only tests."""
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
