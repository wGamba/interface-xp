class Iteracion:

    def __init__(self):
        self.__status = "in progress"
        self.__functionalities = []

    def add_functionality(self, functionality):
        if self.__status == "finished":
            raise Exception("Cannot add functionalities to a finished iteration.")
        self.__functionalities.append(functionality)

    def finish(self, comments_section):
        if self.__status == "finished":
            raise Exception("Iteration has already been finished.")
        if len(self.__functionalities) == 0:
            raise Exception("Cannot finish an iteration without functionalities.")
        self.__status = "finished"
        comments_section.activate()

    def get_status(self):
        return self.__status

    def get_functionalities(self):
        return list(self.__functionalities)
