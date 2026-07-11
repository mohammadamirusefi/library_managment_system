import models.model as model
import sqlite3

import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter

import adapters.book_data_adapter as BookDataAdapter
#
# connection = sqlite3.connect("data/NewLibrary.db")
# cursor = connection.cursor()

s =  BookDataAdapter.BookDataAdapter.get_all()
print(s)
# print("all books:")
# for i in (model.Book.books):
#     print("id:", i.id, " , title:", i.title, " , product_code:", i.product_code, " , categories:", [[j.id, j.name] for j in i.categories], " , age_group:", i.age_group, " , authors:", [[j.id, j.name] for j in i.authors], " , publisher:", [
#           i.publisher.id, i.publisher.name], " , release_date:", i.release_date, " , price:", i.price, " , languages:", [[j.id, j.name] for j in i.languages], " , cover_designers", [[j.id, j.name] for j in i.cover_designers], " , translators:", [[j.id, j.name] for j in i.translators], " , resources:", [[j.id, j.name] for j in i.resources], "\n")
# print("authors:")
# s =  AuthorDataAdapter.AuthorDataAdapter.search("")
# for i in s:
#     print("id:", i.id, " , name :", i.name, " , birthdate:",
#           i.birthdate, " , nationality:", i.nationality)
# print("///")
# print("publishers:")
# m =  PublisherDataAdapter.PublisherDataAdapter.search("a")
# for i in m:
#     print("id:", i.id, " , name :", i.name, " , address:",
#           i.address, " , website:", i.website)
# print("///")
# print("categories:")
# m =  CategoryDataAdapter.CategoryDataAdapter.search("fiction")
# for i in m:
#     print("id:", i.id, " , name :", i.name)
# print("///")
# print("languages:")
# m =  LanguageDataAdapter.LanguageDataAdapter.search("english")
# for i in m:
#     print("id:", i.id, " , name :", i.name)
# print("///")
# print("cover_designers:")
# s =  DesignerDataAdapter.DesignerDataAdapter.search("clara")
# for i in s:
#     print("id:", i.id, " , name :", i.name, " , birthdate:",
#           i.birthdate, " , nationality:", i.nationality)
# print("///")
# print("translators:")
# s =  TranslatorDataAdapter.TranslatorDataAdapter.search("pedro")
# for i in s:
#     print("id:", i.id, " , name :", i.name, " , languages:",
#           i.languages,)
# print("///")
# print("resources:")
# s =  ResourcesDataAdapter.ResourcesDataAdapter.search("maney")
# for i in s:
#     print("id:", i.id, " , name :", i.name,)
# print("///")
# print("search results:")
# result =  BookDataAdapter.BookDataAdapter.search(
#     name="the")
# for i in result:
#     print("id:", i.id, " , title:", i.6title, " , product_code:", i.product_code, " , categories:", [[j.id, j.name] for j in i.categories], " , age_group:", i.age_group, " , authors:", [[j.id, j.name] for j in i.authors], " , publisher:", [
#           i.publisher.id, i.publisher.name], " , release_date:", i.release_date, " , price:", i.price, " , languages:", [[j.id, j.name] for j in i.languages], " , cover_designers", [[j.id, j.name] for j in i.cover_designers], " , translators:", [[j.id, j.name] for j in i.translators], " , resources:", [[j.id, j.name] for j in i.resources], "\n")
print("serach results:")
s =  BookDataAdapter.BookDataAdapter.search(
    name="the whis", publisher_name="Press")
for i in s:
    print("id:", i.id, " , title:", i.title, " , product_code:", i.product_code, " , categories:", [[j.id, j.name] for j in i.categories], " , age_group:", i.age_group, " , authors:", [[j.id, j.name] for j in i.authors], " , publisher:", [
          i.publisher.id, i.publisher.name], " , release_date:", i.release_date, " , price:", i.price, " , languages:", [[j.id, j.name] for j in i.languages], " , cover_designers", [[j.id, j.name] for j in i.cover_designers], " , translators:", [[j.id, j.name] for j in i.translators], " , resources:", [[j.id, j.name] for j in i.resources], "\n")
