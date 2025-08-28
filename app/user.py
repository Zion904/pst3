class User:
    """A base class for all users in the system."""
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        """Serialize object to a JSON-friendly dict."""
        return {"user_id": self.user_id, "name": self.name}

    @staticmethod
    def from_dict(data_dict):
        """create a user from a dictionary"""
        return User(
            user_id = data_dict.get("user_id", data_dict.get("id")),
            name = data_dict.get("name", ""),
        )

