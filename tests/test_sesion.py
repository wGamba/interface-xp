import pytest
from app.models.sesion import Sesion


def test_crear_sesion():
    sesion = Sesion(creador_id=1)
    assert sesion.creador_id == 1
    assert sesion.estado == "activa"


def test_generar_codigo_unico():
    s1 = Sesion(creador_id=1)
    s2 = Sesion(creador_id=2)
    assert s1.codigo != s2.codigo
    assert len(s1.codigo) == 6


def test_sesion_registra_inicio():
    sesion = Sesion(creador_id=1)
    assert sesion.inicio is not None


def test_cerrar_sesion():
    sesion = Sesion(creador_id=1)
    sesion.cerrar()
    assert sesion.estado == "terminada"
    assert sesion.fin is not None


def test_sesion_activa_por_defecto():
    sesion = Sesion(creador_id=1)
    assert sesion.esta_activa() is True


def test_sesion_inactiva_tras_cerrar():
    sesion = Sesion(creador_id=1)
    sesion.cerrar()
    assert sesion.esta_activa() is False
