import random
import string
from datetime import datetime


class Sesion:
    def __init__(self, creador_id):
        self.creador_id = creador_id
        self.codigo = self._generar_codigo()
        self.estado = "activa"
        self.inicio = datetime.now()
        self.fin = None

    def _generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def cerrar(self):
        self.estado = "terminada"
        self.fin = datetime.now()

    def esta_activa(self):
        return self.estado == "activa"
