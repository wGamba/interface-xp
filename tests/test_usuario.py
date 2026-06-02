import pytest
from app.models.usuario import Usuario


def test_create_user():
    user = Usuario(name="Franco", email="franco@test.com")
    assert user.name == "Franco"
    assert user.email == "franco@test.com"


def test_authenticate_correct_password():
    user = Usuario(name="Franco", email="franco@test.com", password="1234")
    assert user.authenticate("1234") is True
    assert user.authenticated is True


def test_authenticate_wrong_password():
    user = Usuario(name="Franco", email="franco@test.com", password="1234")
    assert user.authenticate("wrong") is False
    assert user.authenticated is False


def test_join_session():
    user = Usuario(name="Franco", email="franco@test.com")
    user.join_session("ABC123")
    assert user.session_id == "ABC123"


def test_leave_session():
    user = Usuario(name="Franco", email="franco@test.com")
    user.join_session("ABC123")
    user.leave_session()
    assert user.session_id is None


def test_assign_role():
    user = Usuario(name="Franco", email="franco@test.com")
    user.assign_role("Driver")
    assert user.role == "Driver"
