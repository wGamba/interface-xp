import pytest
from funcionalidad import Funcionalidad

def test_funcionalidad_no_puede_crearse_sin_descripcion():
    with pytest.raises(ValueError):
        Funcionalidad("")

def test_funcionalidad_estado_inicial_es_pendiente():
    funcionalidad = Funcionalidad("Modulo de pagos")
    assert funcionalidad.get_estado() == "pendiente"

def test_funcionalidad_aprobada_no_puede_reevaluarse():
    funcionalidad = Funcionalidad("Modulo de pagos")
    funcionalidad.set_estado("aprobada", "Funciona bien")
    with pytest.raises(Exception):
        funcionalidad.set_estado("rechazada", "Cambie de opinion")

def test_funcionalidad_no_puede_aprobarse_sin_justificacion():
    funcionalidad = Funcionalidad("Modulo de pagos")
    with pytest.raises(ValueError):
        funcionalidad.set_estado("aprobada", "")

def test_funcionalidad_almacena_descripcion_correctamente():
    funcionalidad = Funcionalidad("Modulo de pagos")
    assert funcionalidad.get_descripcion() == "Modulo de pagos"

def test_funcionalidad_registra_justificacion_correctamente():
    funcionalidad = Funcionalidad("Modulo de pagos")
    funcionalidad.set_estado("aprobada", "Funciona perfectamente")
    assert funcionalidad.get_justificacion() == "Funciona perfectamente"

def test_funcionalidad_registra_estado_rechazada_correctamente():
    funcionalidad = Funcionalidad("Modulo de pagos")
    funcionalidad.set_estado("rechazada", "No cumple los requisitos")
    assert funcionalidad.get_estado() == "rechazada"    