import pytest
from app.funcionalidad import Funcionalidad

def test_functionality_cannot_be_created_without_description():
    with pytest.raises(ValueError):
        Funcionalidad("")

def test_functionality_initial_status_is_pending():
    functionality = Funcionalidad("Payment module")
    assert functionality.get_status() == "pending"

def test_approved_functionality_cannot_be_reevaluated():
    functionality = Funcionalidad("Payment module")
    functionality.set_status("approved", "Works well")
    with pytest.raises(Exception):
        functionality.set_status("rejected", "Changed my mind")

def test_functionality_cannot_be_approved_without_justification():
    functionality = Funcionalidad("Payment module")
    with pytest.raises(ValueError):
        functionality.set_status("approved", "")

def test_functionality_stores_description_correctly():
    functionality = Funcionalidad("Payment module")
    assert functionality.get_description() == "Payment module"

def test_functionality_stores_justification_correctly():
    functionality = Funcionalidad("Payment module")
    functionality.set_status("approved", "Works perfectly")
    assert functionality.get_justification() == "Works perfectly"

def test_functionality_stores_rejected_status_correctly():
    functionality = Funcionalidad("Payment module")
    functionality.set_status("rejected", "Does not meet requirements")
    assert functionality.get_status() == "rejected"
