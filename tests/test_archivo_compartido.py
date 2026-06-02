import pytest
from app.models.archivo_compartido import ArchivoCompartido


def test_create_file_empty_by_default():
    file = ArchivoCompartido(name="main.py")
    assert file.name == "main.py"
    assert file.get_content() == ""


def test_create_file_with_initial_content():
    file = ArchivoCompartido(name="main.py", content="print('hi')")
    assert file.get_content() == "print('hi')"


def test_update_content():
    file = ArchivoCompartido(name="main.py")
    file.update_content("x = 1")
    assert file.get_content() == "x = 1"


def test_version_starts_at_zero():
    file = ArchivoCompartido(name="main.py")
    assert file.version == 0


def test_version_increments_on_update():
    file = ArchivoCompartido(name="main.py")
    file.update_content("x = 1")
    file.update_content("x = 2")
    assert file.version == 2


def test_update_with_none_raises_error():
    file = ArchivoCompartido(name="main.py")
    with pytest.raises(ValueError):
        file.update_content(None)
