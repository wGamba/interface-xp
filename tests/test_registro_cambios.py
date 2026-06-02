import pytest
from app.models.registro_cambios import RegistroCambios


def test_history_empty_by_default():
    log = RegistroCambios()
    assert log.get_history() == []


def test_register_change_adds_entry():
    log = RegistroCambios()
    log.register("Franco", "added function foo")
    assert len(log.get_history()) == 1


def test_entry_stores_author_and_description():
    log = RegistroCambios()
    log.register("Franco", "added function foo")
    entry = log.get_history()[0]
    assert entry["author"] == "Franco"
    assert entry["description"] == "added function foo"


def test_entry_has_timestamp():
    log = RegistroCambios()
    log.register("Franco", "added function foo")
    entry = log.get_history()[0]
    assert entry["timestamp"] is not None


def test_register_without_author_raises_error():
    log = RegistroCambios()
    with pytest.raises(ValueError):
        log.register("", "some change")


def test_register_without_description_raises_error():
    log = RegistroCambios()
    with pytest.raises(ValueError):
        log.register("Franco", "")


def test_history_keeps_order():
    log = RegistroCambios()
    log.register("Franco", "first")
    log.register("Ariel", "second")
    history = log.get_history()
    assert history[0]["description"] == "first"
    assert history[1]["description"] == "second"
