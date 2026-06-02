import pytest
from app.cliente import Cliente
from app.funcionalidad import Funcionalidad
from app.cambio_sugerido import CambioSugerido

def test_cliente_no_puede_aprobar_sin_justificacion():
    cliente = Cliente()
    funcionalidad = Funcionalidad("Login de usuario")
    with pytest.raises(ValueError):
        cliente.aprobar(funcionalidad, "")

def test_cliente_no_puede_desaprobar_sin_justificacion():
    cliente = Cliente()
    funcionalidad = Funcionalidad("Login de usuario")
    with pytest.raises(ValueError):
        cliente.desaprobar(funcionalidad, "")

def test_cliente_no_puede_evaluar_funcionalidad_ya_evaluada():
    cliente = Cliente()
    funcionalidad = Funcionalidad("Login de usuario")
    cliente.aprobar(funcionalidad, "Cumple con lo esperado")
    with pytest.raises(Exception):
        cliente.desaprobar(funcionalidad, "Cambie de opinion")

def test_cliente_no_puede_proponer_cambio_sin_descripcion():
    cliente = Cliente()
    with pytest.raises(ValueError):
        cliente.proponer_cambio("", "alta")

def test_cliente_aprueba_funcionalidad_correctamente():
    cliente = Cliente()
    funcionalidad = Funcionalidad("Login de usuario")
    cliente.aprobar(funcionalidad, "Cumple con lo esperado")
    assert funcionalidad.get_estado() == "aprobada"
    assert funcionalidad.get_justificacion() == "Cumple con lo esperado"

def test_cliente_desaprueba_funcionalidad_correctamente():
    cliente = Cliente()
    funcionalidad = Funcionalidad("Login de usuario")
    cliente.desaprobar(funcionalidad, "No funciona correctamente")
    assert funcionalidad.get_estado() == "rechazada"
    assert funcionalidad.get_justificacion() == "No funciona correctamente"

def test_cliente_propone_cambio_correctamente():
    cliente = Cliente()
    cambio = cliente.proponer_cambio("Mejorar interfaz", "alta")
    assert cambio.get_descripcion() == "Mejorar interfaz"
    assert cambio.get_prioridad() == "alta"