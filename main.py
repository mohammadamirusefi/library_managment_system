import models.model as model
import sqlite3
import re
import json
import datetime

from models.category import Category
from models.author import Author
from models.publisher import Publisher
from models.language import Language
from models.designer import CoverDesigner
from models.translator import Translator
from models.resource import Resources
from models.book import Book


import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter
import adapters.book_data_adapter as  BookDataAdapter

publisher = Publisher(1, "ali", "alsas", "wfmwf")
category = Category(1, "fiction")
author = Author(1, "ali", datetime.datetime.today(), "british")
language = Language(1, "engrghr")
designer = CoverDesigner(1, "ali", datetime.datetime.today(), "scsd")
trans = Translator(1, "ali", [language])
resource = Resources(1, "als")
book = Book(1, "tkjgb", 1001, [category], "adult", [
            author], publisher, datetime.datetime.today(), 50, [language], [designer], [trans], [resource])
s=BookDataAdapter.BookDataAdapter.search(name="the")
for i in s:
    print("id:", i.id, " , title:", i.title, " , product_code:", i.product_code, " , categories:", [[j.id, j.name] for j in i.categories], " , age_group:", i.age_group, " , authors:", [[j.id, j.name] for j in i.authors], " , publisher:", [
          i.publisher.id, i.publisher.name], " , release_date:", i.release_date, " , price:", i.price, " , languages:", [[j.id, j.name] for j in i.languages], " , cover_designers", [[j.id, j.name] for j in i.cover_designers], " , translators:", [[j.id, j.name] for j in i.translators], " , resources:", [[j.id, j.name] for j in i.resources], "\n")
