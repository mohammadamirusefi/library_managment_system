import datetime

class Author:
    id: int = 0
    name: str = ""
    birthdate: datetime.date = datetime.date.today()
    nationality: str = ""
    authors: list = []

    def __init__(self, id: int, name: str, birthdate: datetime.date, nationality: str):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.nationality = nationality

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Author):
            return self.id == other.id
        else:
            return
