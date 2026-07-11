import datetime


class Resources:
    id: int = 0
    name: str = ""
    resources: list = []

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, int):
            return self.id == other
        elif isinstance(other, Resources):
            return self.name == other.name
        else:
            return