class CambioSugerido:

    PRIORIDADES_VALIDAS = ["alta", "media", "baja"]

    def __init__(self, descripcion, prioridad):
        if not descripcion or descripcion.strip() == "":
            raise ValueError("La descripcion no puede estar vacia.")
        if prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad invalida. Use: alta, media o baja.")
        self.__descripcion = descripcion
        self.__prioridad = prioridad

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def set_prioridad(self, nueva_prioridad):
        if nueva_prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad invalida. Use: alta, media o baja.")
        self.__prioridad = nueva_prioridad