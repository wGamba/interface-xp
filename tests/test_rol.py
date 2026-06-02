import pytest
from app.models.rol import Rol


def test_create_driver_role():
    role = Rol("Driver")
    assert role.name == "Driver"


def test_create_navigator_role():
    role = Rol("Navigator")
    assert role.name == "Navigator"


def test_invalid_role_raises_error():
    with pytest.raises(ValueError):
        Rol("Manager")


def test_driver_can_edit():
    role = Rol("Driver")
    assert role.can_edit() is True


def test_navigator_cannot_edit():
    role = Rol("Navigator")
    assert role.can_edit() is False


def test_driver_swaps_to_navigator():
    role = Rol("Driver")
    role.swap()
    assert role.name == "Navigator"


def test_navigator_swaps_to_driver():
    role = Rol("Navigator")
    role.swap()
    assert role.name == "Driver"


def test_swap_changes_edit_permission():
    role = Rol("Driver")
    role.swap()
    assert role.can_edit() is False
