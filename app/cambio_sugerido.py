class CambioSugerido:

    VALID_PRIORITIES = ["high", "medium", "low"]

    def __init__(self, description, priority):
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty.")
        if priority not in self.VALID_PRIORITIES:
            raise ValueError("Invalid priority. Use: high, medium or low.")
        self.__description = description
        self.__priority = priority

    def get_description(self):
        return self.__description

    def get_priority(self):
        return self.__priority

    def set_priority(self, new_priority):
        if new_priority not in self.VALID_PRIORITIES:
            raise ValueError("Invalid priority. Use: high, medium or low.")
        self.__priority = new_priority
