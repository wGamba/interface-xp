import pytest
from app.iteracion import Iteracion
from app.funcionalidad import Funcionalidad
from app.seccion_comentarios import SeccionComentarios

def test_finished_iteration_cannot_receive_more_functionalities():
    iteration = Iteracion()
    iteration.add_functionality(Funcionalidad("User login"))
    section = SeccionComentarios()
    iteration.finish(section)
    with pytest.raises(Exception):
        iteration.add_functionality(Funcionalidad("New functionality"))

def test_iteration_cannot_finish_without_functionalities():
    iteration = Iteracion()
    section = SeccionComentarios()
    with pytest.raises(Exception):
        iteration.finish(section)

def test_iteration_activates_section_when_finished():
    iteration = Iteracion()
    iteration.add_functionality(Funcionalidad("User login"))
    section = SeccionComentarios()
    iteration.finish(section)
    assert section.is_active() == True

def test_iteration_cannot_be_finished_twice():
    iteration = Iteracion()
    iteration.add_functionality(Funcionalidad("User login"))
    section = SeccionComentarios()
    iteration.finish(section)
    with pytest.raises(Exception):
        iteration.finish(section)

def test_iteration_initial_status_is_in_progress():
    iteration = Iteracion()
    assert iteration.get_status() == "in progress"

def test_iteration_status_changes_to_finished():
    iteration = Iteracion()
    iteration.add_functionality(Funcionalidad("User login"))
    section = SeccionComentarios()
    iteration.finish(section)
    assert iteration.get_status() == "finished"

def test_iteration_adds_functionality_correctly():
    iteration = Iteracion()
    functionality = Funcionalidad("User login")
    iteration.add_functionality(functionality)
    assert functionality in iteration.get_functionalities()
