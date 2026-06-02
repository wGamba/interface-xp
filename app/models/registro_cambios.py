from datetime import datetime


class RegistroCambios:
    def __init__(self):
        self.__history = []

    def register(self, author, description):
        if not author or author.strip() == "":
            raise ValueError("Author cannot be empty.")
        if not description or description.strip() == "":
            raise ValueError("Description cannot be empty.")
        self.__history.append({
            "author": author,
            "description": description,
            "timestamp": datetime.now(),
        })

    def get_history(self):
        return list(self.__history)
