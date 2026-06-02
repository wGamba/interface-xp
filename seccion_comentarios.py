class SeccionComentarios:

    def __init__(self):
        self.__activa = False
        self.__comentarios = []

    def activar(self):
        if self.__activa:
            raise Exception("La seccion de comentarios ya esta activa.")
        self.__activa = True

    def agregar_comentario(self, comentario):
        if not self.__activa:
            raise Exception("La seccion de comentarios no esta activa.")
        if not comentario or comentario.strip() == "":
            raise ValueError("El comentario no puede estar vacio.")
        self.__comentarios.append(comentario)

    def get_comentarios(self):
        if not self.__activa:
            raise Exception("La seccion de comentarios no esta activa.")
        return list(self.__comentarios)

    def is_activa(self):
        return self.__activa