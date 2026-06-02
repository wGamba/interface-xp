import pytest
from app.iteracion import Iteracion
from app.funcionalidad import Funcionalidad
from app.seccion_comentarios import SeccionComentarios

def test_iteracion_finalizada_no_puede_recibir_mas_funcionalidades():
    iteracion = Iteracion()
    iteracion.agregar_funcionalidad(Funcionalidad("Login de usuario"))
    seccion = SeccionComentarios()
    iteracion.finalizar(seccion)
    with pytest.raises(Exception):
        iteracion.agregar_funcionalidad(Funcionalidad("Nueva funcionalidad"))

def test_iteracion_no_puede_finalizar_sin_funcionalidades():
    iteracion = Iteracion()
    seccion = SeccionComentarios()
    with pytest.raises(Exception):
        iteracion.finalizar(seccion)

def test_iteracion_activa_seccion_al_finalizar():
    iteracion = Iteracion()
    iteracion.agregar_funcionalidad(Funcionalidad("Login de usuario"))
    seccion = SeccionComentarios()
    iteracion.finalizar(seccion)
    assert seccion.is_activa() == True

def test_iteracion_no_puede_finalizarse_dos_veces():
    iteracion = Iteracion()
    iteracion.agregar_funcionalidad(Funcionalidad("Login de usuario"))
    seccion = SeccionComentarios()
    iteracion.finalizar(seccion)
    with pytest.raises(Exception):
        iteracion.finalizar(seccion)

def test_iteracion_estado_inicial_es_en_curso():
    iteracion = Iteracion()
    assert iteracion.get_estado() == "en curso"

def test_iteracion_estado_cambia_a_finalizada():
    iteracion = Iteracion()
    iteracion.agregar_funcionalidad(Funcionalidad("Login de usuario"))
    seccion = SeccionComentarios()
    iteracion.finalizar(seccion)
    assert iteracion.get_estado() == "finalizada"

def test_iteracion_agrega_funcionalidad_correctamente():
    iteracion = Iteracion()
    funcionalidad = Funcionalidad("Login de usuario")
    iteracion.agregar_funcionalidad(funcionalidad)
    assert funcionalidad in iteracion.get_funcionalidades()