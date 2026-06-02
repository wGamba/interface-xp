class Funcionalidad:

    def __init__(self, descripcion):
        if not descripcion or descripcion.strip() == "":
            raise ValueError("La descripcion no puede estar vacia.")
        self.__descripcion = descripcion
        self.__estado = "pendiente"
        self.__justificacion = ""

    def set_estado(self, estado, justificacion):
        if self.__estado != "pendiente":
            raise Exception("La funcionalidad ya fue evaluada.")
        if not justificacion or justificacion.strip() == "":
            raise ValueError("La justificacion no puede estar vacia.")
        self.__estado = estado
        self.__justificacion = justificacion

    def get_descripcion(self):
        return self.__descripcion

    def get_estado(self):
        return self.__estado

    def get_justificacion(self):
        return self.__justificacion