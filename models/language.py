import datetime

class Language:
    id: int = 0
    name: str = ""
    languages: list = []

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, int):
            return self.id == other
        elif isinstance(other, Language):
            return self.name == other.name
        else:
            return
