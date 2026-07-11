import datetime
from models.language import Language

class Translator:
    id: int = 0
    name: str = ""
    languages: list[Language] = []
    translators: list = []

    def __init__(self, id: int, name: str, languages: list[Language]):
        self.id = id
        self.name = name
        self.languages = languages

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Translator):
            return self.id == other.id
        else:
            return
