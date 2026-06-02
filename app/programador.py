class Programador:

    PRIORIDADES_VALIDAS = ["alta", "media", "baja"]

    def obtener_retroalimentacion(self, seccion_comentarios):
        if not seccion_comentarios.is_activa():
            raise Exception("La seccion de comentarios no esta activa.")
        return seccion_comentarios.get_comentarios()

    def priorizar_cambio(self, cambio_sugerido, nueva_prioridad):
        if nueva_prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("Prioridad invalida. Use: alta, media o baja.")
        cambio_sugerido.set_prioridad(nueva_prioridad)