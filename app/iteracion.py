from app.funcionalidad import Funcionalidad
from app.seccion_comentarios import SeccionComentarios

class Iteracion:

    def __init__(self):
        self.__estado = "en curso"
        self.__funcionalidades = []

    def agregar_funcionalidad(self, funcionalidad):
        if self.__estado == "finalizada":
            raise Exception("No se pueden agregar funcionalidades a una iteracion finalizada.")
        self.__funcionalidades.append(funcionalidad)

    def finalizar(self, seccion_comentarios):
        if self.__estado == "finalizada":
            raise Exception("La iteracion ya fue finalizada.")
        if len(self.__funcionalidades) == 0:
            raise Exception("No se puede finalizar una iteracion sin funcionalidades.")
        self.__estado = "finalizada"
        seccion_comentarios.activar()

    def get_estado(self):
        return self.__estado

    def get_funcionalidades(self):
        return list(self.__funcionalidades)