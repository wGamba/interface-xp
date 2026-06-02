import pytest
from app.programador import Programador
from app.seccion_comentarios import SeccionComentarios
from app.cambio_sugerido import CambioSugerido

def test_programador_no_puede_obtener_retroalimentacion_si_seccion_no_esta_activa():
    programador = Programador()
    seccion = SeccionComentarios()
    with pytest.raises(Exception):
        programador.obtener_retroalimentacion(seccion)

def test_programador_no_puede_priorizar_con_valor_invalido():
    programador = Programador()
    cambio = CambioSugerido("Mejorar interfaz", "media")
    with pytest.raises(ValueError):
        programador.priorizar_cambio(cambio, "urgentisimo")

def test_programador_puede_cambiar_prioridad_de_cambio_sugerido():
    programador = Programador()
    cambio = CambioSugerido("Mejorar interfaz", "baja")
    programador.priorizar_cambio(cambio, "alta")
    assert cambio.get_prioridad() == "alta"

def test_programador_obtiene_retroalimentacion_correctamente():
    programador = Programador()
    seccion = SeccionComentarios()
    seccion.activar()
    seccion.agregar_comentario("El diseno no es intuitivo")
    comentarios = programador.obtener_retroalimentacion(seccion)
    assert "El diseno no es intuitivo" in comentarios

def test_programador_obtiene_lista_vacia_si_no_hay_comentarios():
    programador = Programador()
    seccion = SeccionComentarios()
    seccion.activar()
    comentarios = programador.obtener_retroalimentacion(seccion)
    assert comentarios == []