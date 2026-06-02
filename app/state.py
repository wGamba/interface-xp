"""In-memory state for the demo interface.

US-01 (Pair Programming) keeps one entry per active session, keyed by code.
US-02 (Client Feedback) keeps a single shared iteration for the demo.
No database: the goal is to showcase the domain models, not to persist data.
"""
from app.models.sesion import Sesion
from app.models.archivo_compartido import ArchivoCompartido
from app.models.registro_cambios import RegistroCambios
from app.models.iteracion import Iteracion
from app.models.seccion_comentarios import SeccionComentarios
from app.models.cliente import Cliente
from app.models.programador import Programador

# --- US-01: Pair Programming ---------------------------------------------
# code -> {"sesion", "archivo", "registro", "users": {sid: {name, role}}}
sessions = {}


def create_session(creator_name):
    sesion = Sesion(creador_id=creator_name)
    sessions[sesion.codigo] = {
        "sesion": sesion,
        "archivo": ArchivoCompartido(name="shared.py", content=""),
        "registro": RegistroCambios(),
        "users": {},
    }
    return sesion.codigo


def get_session(code):
    return sessions.get(code)


# --- US-02: Client Feedback ----------------------------------------------
feedback = {}


def reset_feedback():
    feedback.clear()
    feedback.update({
        "iteracion": Iteracion(),
        "comentarios": SeccionComentarios(),
        "cambios": [],          # list[CambioSugerido]
        "cliente": Cliente(),
        "programador": Programador(),
    })


reset_feedback()
