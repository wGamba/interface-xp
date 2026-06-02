class ArchivoCompartido:
    def __init__(self, name, content=""):
        self.name = name
        self.__content = content
        self.version = 0

    def update_content(self, content):
        if content is None:
            raise ValueError("Content cannot be None.")
        self.__content = content
        self.version += 1

    def get_content(self):
        return self.__content
