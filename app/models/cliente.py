from app.models.cambio_sugerido import CambioSugerido

class Cliente:

    def approve(self, functionality, justification):
        if not justification or justification.strip() == "":
            raise ValueError("Justification cannot be empty.")
        if functionality.get_status() != "pending":
            raise Exception("Functionality has already been evaluated.")
        functionality.set_status("approved", justification)

    def reject(self, functionality, justification):
        if not justification or justification.strip() == "":
            raise ValueError("Justification cannot be empty.")
        if functionality.get_status() != "pending":
            raise Exception("Functionality has already been evaluated.")
        functionality.set_status("rejected", justification)

    def propose_change(self, description, priority):
        if not description or description.strip() == "":
            raise ValueError("Change description cannot be empty.")
        return CambioSugerido(description, priority)
