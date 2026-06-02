import pytest
from app.models.cambio_sugerido import CambioSugerido

def test_suggested_change_rejects_invalid_priority():
    with pytest.raises(ValueError):
        CambioSugerido("Improve interface", "urgent")

def test_suggested_change_cannot_be_created_without_description():
    with pytest.raises(ValueError):
        CambioSugerido("", "high")

def test_suggested_change_updates_its_priority():
    change = CambioSugerido("Improve interface", "low")
    change.set_priority("high")
    assert change.get_priority() == "high"

def test_suggested_change_stores_description_correctly():
    change = CambioSugerido("Add dark mode", "medium")
    assert change.get_description() == "Add dark mode"

def test_suggested_change_knows_its_priority():
    change = CambioSugerido("Add dark mode", "high")
    assert change.get_priority() == "high"

def test_suggested_change_rejects_invalid_priority_on_update():
    change = CambioSugerido("Improve interface", "medium")
    with pytest.raises(ValueError):
        change.set_priority("super urgent")
