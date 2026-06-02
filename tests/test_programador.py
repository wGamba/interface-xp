import pytest
from app.programador import Programador
from app.seccion_comentarios import SeccionComentarios
from app.cambio_sugerido import CambioSugerido

def test_developer_cannot_get_feedback_if_section_not_active():
    developer = Programador()
    section = SeccionComentarios()
    with pytest.raises(Exception):
        developer.get_feedback(section)

def test_developer_cannot_prioritize_with_invalid_value():
    developer = Programador()
    change = CambioSugerido("Improve interface", "medium")
    with pytest.raises(ValueError):
        developer.prioritize_change(change, "super urgent")

def test_developer_can_change_priority_of_suggested_change():
    developer = Programador()
    change = CambioSugerido("Improve interface", "low")
    developer.prioritize_change(change, "high")
    assert change.get_priority() == "high"

def test_developer_gets_feedback_correctly():
    developer = Programador()
    section = SeccionComentarios()
    section.activate()
    section.add_comment("The design is not intuitive")
    comments = developer.get_feedback(section)
    assert "The design is not intuitive" in comments

def test_developer_gets_empty_list_if_no_comments():
    developer = Programador()
    section = SeccionComentarios()
    section.activate()
    comments = developer.get_feedback(section)
    assert comments == []
