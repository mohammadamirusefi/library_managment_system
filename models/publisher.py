import datetime


class Publisher:
    id: int = 0
    name: str = ""
    address: str = ""
    website: str = ""
    publishers: list = []

    def __init__(self, id: int, name: str, address: str, website: str):
        self.id = id
        self.name = name
        self.address = address
        self.website = website

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Publisher):
            return self.id == other.id
        else:
            return
