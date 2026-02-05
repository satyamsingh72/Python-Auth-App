import pytest
from schemas import UserCreate, UserLogin


def test_user_create_valid():
    data = {"username": "john", "password": "123456"}
    user = UserCreate(**data)
    assert user.username == "john"
    assert user.password == "123456"


def test_user_create_missing_username():
    with pytest.raises(Exception):
        UserCreate(password="123456")


def test_user_login_valid():
    data = {"username": "alice", "password": "mypassword"}
    user = UserLogin(**data)
    assert user.username == "alice"
    assert user.password == "mypassword"


def test_user_login_missing_password():
    with pytest.raises(Exception):
        UserLogin(username="bob")
