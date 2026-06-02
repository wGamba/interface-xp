class Usuario:
    def __init__(self, name, email, password=None):
        self.name = name
        self.email = email
        self._password = password
        self.authenticated = False
        self.session_id = None
        self.role = None

    def authenticate(self, password):
        if self._password == password:
            self.authenticated = True
            return True
        return False

    def join_session(self, code):
        self.session_id = code

    def leave_session(self):
        self.session_id = None

    def assign_role(self, role):
        self.role = role
