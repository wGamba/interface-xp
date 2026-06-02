from cambio_sugerido import CambioSugerido

class Cliente:

    def aprobar(self, funcionalidad, justificacion):
        if not justificacion or justificacion.strip() == "":
            raise ValueError("La justificacion no puede estar vacia.")
        if funcionalidad.get_estado() != "pendiente":
            raise Exception("La funcionalidad ya fue evaluada.")
        funcionalidad.set_estado("aprobada", justificacion)

    def desaprobar(self, funcionalidad, justificacion):
        if not justificacion or justificacion.strip() == "":
            raise ValueError("La justificacion no puede estar vacia.")
        if funcionalidad.get_estado() != "pendiente":
            raise Exception("La funcionalidad ya fue evaluada.")
        funcionalidad.set_estado("rechazada", justificacion)

    def proponer_cambio(self, descripcion, prioridad):
        if not descripcion or descripcion.strip() == "":
            raise ValueError("La descripcion del cambio no puede estar vacia.")
        return CambioSugerido(descripcion, prioridad)