class Funcionalidad:

    def __init__(self, description):
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty.")
        self.__description = description
        self.__status = "pending"
        self.__justification = ""

    def set_status(self, status, justification):
        if self.__status != "pending":
            raise Exception("Functionality has already been evaluated.")
        if not justification or justification.strip() == "":
            raise ValueError("Justification cannot be empty.")
        self.__status = status
        self.__justification = justification

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def get_justification(self):
        return self.__justification
