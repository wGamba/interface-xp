import pytest
from app.models.cliente import Cliente
from app.models.funcionalidad import Funcionalidad
from app.models.cambio_sugerido import CambioSugerido

def test_client_cannot_approve_without_justification():
    client = Cliente()
    functionality = Funcionalidad("User login")
    with pytest.raises(ValueError):
        client.approve(functionality, "")

def test_client_cannot_reject_without_justification():
    client = Cliente()
    functionality = Funcionalidad("User login")
    with pytest.raises(ValueError):
        client.reject(functionality, "")

def test_client_cannot_evaluate_already_evaluated_functionality():
    client = Cliente()
    functionality = Funcionalidad("User login")
    client.approve(functionality, "Meets expectations")
    with pytest.raises(Exception):
        client.reject(functionality, "Changed my mind")

def test_client_cannot_propose_change_without_description():
    client = Cliente()
    with pytest.raises(ValueError):
        client.propose_change("", "high")

def test_client_approves_functionality_correctly():
    client = Cliente()
    functionality = Funcionalidad("User login")
    client.approve(functionality, "Meets expectations")
    assert functionality.get_status() == "approved"
    assert functionality.get_justification() == "Meets expectations"

def test_client_rejects_functionality_correctly():
    client = Cliente()
    functionality = Funcionalidad("User login")
    client.reject(functionality, "Does not work correctly")
    assert functionality.get_status() == "rejected"
    assert functionality.get_justification() == "Does not work correctly"

def test_client_proposes_change_correctly():
    client = Cliente()
    change = client.propose_change("Improve interface", "high")
    assert change.get_description() == "Improve interface"
    assert change.get_priority() == "high"
