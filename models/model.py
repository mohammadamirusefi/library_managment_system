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


class CoverDesigner:
    id: int = 0
    name: str = ""
    birthdate: datetime.date = datetime.date.today()
    nationality: str = ""
    cover_designers: list = []

    def __init__(self, id: int, name: str, birthdate: datetime.date, nationality: str):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.nationality = nationality

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, CoverDesigner):
            return self.id == other.id
        else:
            return


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


class Book:
    id: int = 0
    title: str = ""
    product_code: int = 0
    categories: list[Category] = []
    age_group: str = ""
    authors: list[Author] = []
    publisher: Publisher
    release_date: datetime.date = datetime.date.today()
    price: int = 0
    languages: list[Language] = []
    cover_designers: list[CoverDesigner] = []
    translators: list[Translator] = []
    resources: list[Resources] = []
    books: list = []

    def __init__(self, id: int, title: str, product_code: int, categories: list[Category], age_group: str, release_date: datetime.datetime, authors: list[Author], price: int, languages: list[Language], publisher: Publisher, cover_designers: list[CoverDesigner], translators: list[Translator], resources: list[Resources]):
        self.id = id
        self.title = title
        self.product_code = product_code
        self.categories = categories
        self.age_group = age_group
        self.release_date = release_date
        self.authors = authors
        self.price = price
        self.languages = languages
        self.publisher = publisher
        self.cover_designers = cover_designers
        self.translators = translators
        self.resources = resources

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Book):
            return self.id == other.id
        else:
            return

