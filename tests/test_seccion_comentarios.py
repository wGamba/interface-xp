import pytest
from app.models.seccion_comentarios import SeccionComentarios

def test_comments_section_cannot_receive_comments_if_not_active():
    section = SeccionComentarios()
    with pytest.raises(Exception):
        section.add_comment("Great increment")

def test_comments_section_cannot_be_activated_twice():
    section = SeccionComentarios()
    section.activate()
    with pytest.raises(Exception):
        section.activate()

def test_comments_section_returns_empty_list_if_no_comments():
    section = SeccionComentarios()
    section.activate()
    assert section.get_comments() == []

def test_comments_section_does_not_accept_empty_comment():
    section = SeccionComentarios()
    section.activate()
    with pytest.raises(ValueError):
        section.add_comment("")

def test_comments_section_adds_comment_correctly():
    section = SeccionComentarios()
    section.activate()
    section.add_comment("Missing field validation")
    assert section.get_comments()[0] == "Missing field validation"

def test_comments_section_is_not_active_by_default():
    section = SeccionComentarios()
    assert section.is_active() == False

def test_comments_section_is_active_after_activation():
    section = SeccionComentarios()
    section.activate()
    assert section.is_active() == True
