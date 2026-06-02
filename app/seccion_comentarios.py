class SeccionComentarios:

    def __init__(self):
        self.__active = False
        self.__comments = []

    def activate(self):
        if self.__active:
            raise Exception("Comments section is already active.")
        self.__active = True

    def add_comment(self, comment):
        if not self.__active:
            raise Exception("Comments section is not active.")
        if not comment or comment.strip() == "":
            raise ValueError("Comment cannot be empty.")
        self.__comments.append(comment)

    def get_comments(self):
        if not self.__active:
            raise Exception("Comments section is not active.")
        return list(self.__comments)

    def is_active(self):
        return self.__active
