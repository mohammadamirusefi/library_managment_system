import datetime

from models.category import Category
from models.author import Author
from models.publisher import Publisher
from models.language import Language
from models.designer import CoverDesigner
from models.translator import Translator
from models.resource import Resources

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
