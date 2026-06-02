class Rol:

    VALID_ROLES = ["Driver", "Navigator"]

    def __init__(self, name):
        if name not in self.VALID_ROLES:
            raise ValueError("Invalid role. Use: Driver or Navigator.")
        self.name = name

    def can_edit(self):
        return self.name == "Driver"

    def swap(self):
        self.name = "Navigator" if self.name == "Driver" else "Driver"
