class Programador:

    VALID_PRIORITIES = ["high", "medium", "low"]

    def get_feedback(self, comments_section):
        if not comments_section.is_active():
            raise Exception("The comments section is not active.")
        return comments_section.get_comments()

    def prioritize_change(self, suggested_change, new_priority):
        if new_priority not in self.VALID_PRIORITIES:
            raise ValueError("Invalid priority. Use: high, medium or low.")
        suggested_change.set_priority(new_priority)
