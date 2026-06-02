import pytest
from app.seccion_comentarios import SeccionComentarios
from app.programador import Programador

def test_seccion_no_puede_recibir_comentarios_si_no_esta_activa():
    seccion = SeccionComentarios()
    with pytest.raises(Exception):
        seccion.agregar_comentario("Buen incremento")

def test_seccion_no_puede_activarse_dos_veces():
    seccion = SeccionComentarios()
    seccion.activar()
    with pytest.raises(Exception):
        seccion.activar()

def test_seccion_retorna_lista_vacia_si_no_hay_comentarios():
    seccion = SeccionComentarios()
    seccion.activar()
    assert seccion.get_comentarios() == []

def test_seccion_no_acepta_comentario_vacio():
    seccion = SeccionComentarios()
    seccion.activar()
    with pytest.raises(ValueError):
        seccion.agregar_comentario("")

def test_seccion_agrega_comentario_correctamente():
    seccion = SeccionComentarios()
    seccion.activar()
    seccion.agregar_comentario("Falta validacion de campos")
    assert seccion.get_comentarios()[0] == "Falta validacion de campos"

def test_seccion_no_esta_activa_por_defecto():
    seccion = SeccionComentarios()
    assert seccion.is_activa() == False

def test_seccion_esta_activa_despues_de_activar():
    seccion = SeccionComentarios()
    seccion.activar()
    assert seccion.is_activa() == True