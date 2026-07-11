import datetime


class Category:
    id: int = 0
    name: str = ""
    categories: list = []

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, int):
            return self.id == other
        elif isinstance(other, Category):
            return self.name == other.name
        else:
            return
