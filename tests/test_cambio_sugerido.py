import pytest
from app.cambio_sugerido import CambioSugerido

def test_cambio_sugerido_rechaza_prioridad_invalida():
    with pytest.raises(ValueError):
        CambioSugerido("Mejorar interfaz", "urgente")

def test_cambio_sugerido_no_puede_crearse_sin_descripcion():
    with pytest.raises(ValueError):
        CambioSugerido("", "alta")

def test_cambio_sugerido_actualiza_su_prioridad():
    cambio = CambioSugerido("Mejorar interfaz", "baja")
    cambio.set_prioridad("alta")
    assert cambio.get_prioridad() == "alta"

def test_cambio_sugerido_almacena_descripcion_correctamente():
    cambio = CambioSugerido("Agregar modo oscuro", "media")
    assert cambio.get_descripcion() == "Agregar modo oscuro"

def test_cambio_sugerido_conoce_su_prioridad():
    cambio = CambioSugerido("Agregar modo oscuro", "alta")
    assert cambio.get_prioridad() == "alta"

def test_cambio_sugerido_no_acepta_actualizacion_con_prioridad_invalida():
    cambio = CambioSugerido("Mejorar interfaz", "media")
    with pytest.raises(ValueError):
        cambio.set_prioridad("urgentisimo")