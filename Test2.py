import models.model as model
import sqlite3
import re
import json
import datetime

import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter

import adapters.book_data_adapter as BookDataAdapter
# connection = sqlite3.connect("Library.db")
# cursor = connection.cursor()
# sql_script = open(file="Library.sql", mode="rt",
#                   encod6ing="utf-8").read()
# cursor.executescript(sql_script)

pr = "insert book ilia 1040 [1,2] Adult 2020-10-07 [4,3] 90 [3] 4 [1] [3,1,2] [1,2] "

# print( ResourcesDataAdapter.ResourcesDataAdapter.delete(51))
r = r"^\[\d+(,\d+)*\]$"

r2 = r"^\d{4}-\d{2}-\d{2}$"
connection = sqlite3.connect("NewLibrary.db")
cursor = connection.cursor()


# while True:
#     model.Category.categories =  CategoryDataAdapter.CategoryDataAdapter.get_all()
#     model.Author.authors =   AuthorDataAdapter.AuthorDataAdapter.get_all()
#     model.Publisher.publishers =  PublisherDataAdapter.PublisherDataAdapter.get_all()
#     model.Language.languages =  LanguageDataAdapter.LanguageDataAdapter.get_all()
#     model.CoverDesigner.cover_designers =  DesignerDataAdapter.DesignerDataAdapter.get_all()
#     model.Translator.translators =  TranslatorDataAdapter.TranslatorDataAdapter.get_all()
#     model.Resources.resources =  ResourcesDataAdapter.ResourcesDataAdapter.get_all()
#     model.Publisher.publishers =  PublisherDataAdapter.PublisherDataAdapter.get_all()
#     model.Book.books =  BookDataAdapter.BookDataAdapter.get_all()
#     print("""help:
# Add Author : insert author [name] [birthdate] [nationality] / Delete : delete author [author_id]
# Add Publisher : insert publisher [name] [address] [website] / Delete : delete publisher [publisher_id]
# Add Language : insert language [name] / Delete : delete language [language_id]
# Add Cover Designer : insert designer [name] [birthdate] [nationality] / Delete : delete designer [designer_id]
# Add Translator : insert translator [name] [language] / Delete : delete translator [translator_id]
# Add Resource : insert resource [name] / Delete  : delete  resource [resource_id]
# Add Category : insert category [name] / Delete  : delete  category [category_id]
# Add book : insert book [title] [product_code] [list[category_id,category_id,...]] [age_group] [release_date] [list[author_id,author_id,...]] [price] [list[language_id,language_id,...]] [publisher_id] [list[designer_id,designer_id,...]] [list[translator_id,translator_id,...]] [list[resourse_id,resourse_id,...]]
# example : insert book hello 1040 [1,2] Adult 2020-10-07 [4,3] 90 [3] 4 [1] [3,1,2] [1,2]
# Delete book : delete book [book_id]
# """)
#     s=input().split()

#     if s[0]=="insert":
#         print(len(s))
#         if s[1]=="author" and len(s)==5:
#             a1=model.Author(None,str(s[2]),str(s[3]),str(s[4]))
#             a2 =   AuthorDataAdapter.AuthorDataAdapter.insert(a1)
#             print("ok")
#         elif s[1]=="publisher"  and len(s)==5:
#             p1 = model.Publisher(None,str(s[2]),str(s[3]),str(s[4]))
#             p2 =  PublisherDataAdapter.PublisherDataAdapter.insert(p1)
#             print("ok")
#         elif s[1]=="language" and len(s)==3:
#             l1=model.Language(None,str(s[2]))
#             l2 =  LanguageDataAdapter.LanguageDataAdapter.insert(l1)
#             print("ok")
#         elif s[1]=="designer" and len(s)==5:
#             d1=model.CoverDesigner(None,str(s[2]),str(s[3]),str(s[4]))
#             d2 =  DesignerDataAdapter.DesignerDataAdapter.insert(d1)
#             print("ok")
#         elif s[1]=="translator" and len(s)==4:
#             t1=model.Translator(None,str(s[2]),str(s[3]))
#             t2 =  TranslatorDataAdapter.TranslatorDataAdapter.insert(t1)
#             print("ok")
#         elif s[1]=="resource" and len(s)==3:
#             r1=model.Resources(None,str(s[2]))
#             r2 =  ResourcesDataAdapter.ResourcesDataAdapter.insert(r1)
#             print("ok")
#         elif s[1]=="category" and len(s)==3:
#             c1=model.Category(None,str(s[2]))
#             c2 =  CategoryDataAdapter.CategoryDataAdapter.insert(c1)
#             print("ok")

#         elif s[1]=="book" and len(s)==14  and re.match( r,s[4]) and re.match(r2,s[6]) and re.match(r,s[7])  and re.match(r,s[9])  and re.match(r,s[11]) and re.match(r,s[12]) and re.match(r,s[13]):
#                 try:
#                     title=s[2]
#                     code=int(s[3])
#                     category=json.loads(s[4])
#                     age_group=s[5]
#                     release_date=datetime.date.fromisoformat(s[6])
#                     author=json.loads(s[7])
#                     price=int(s[8])
#                     language=json.loads(s[9])
#                     publisher=model.Publisher.publishers[model.Publisher.publishers.index(int(s[10]))]
#                     designer=json.loads(s[11])
#                     translator=json.loads(s[12])
#                     resource=json.loads(s[13])

#                     CategoryDataAdapter.CategoryDataAdapter.get_all()
#                     categories=[]
#                     cat_id=[i.id for i in model.Category.categories]
#                     for i in category:
#                         if int(i) in cat_id:
#                             categories.append(model.Category.categories[model.Category.categories.index(int(i))])


#                     authors=[]
#                     author_id=[i.id for i in model.Author.authors]
#                     for i in author:
#                         if int(i) in author_id:
#                             authors.append(model.Author.authors[model.Author.authors.index(int(i))])


#                     language_id=[i.id for i in model.Language.languages]
#                     languages=[]
#                     for i in language:
#                         if int(i) in language_id:
#                             languages.append(model.Language.languages[model.Language.languages.index(int(i))])


#                     designers=[]
#                     designer_id=[i.id for i in model.CoverDesigner.cover_designers]
#                     for i in designer:
#                         if int(i) in designer_id:
#                             designers.append(model.CoverDesigner.cover_designers[model.CoverDesigner.cover_designers.index(int(i))])


#                     translators=[]
#                     translator_id=[i.id for i in model.Translator.translators]
#                     for i in translator:
#                         if int(i) in translator_id:
#                             translators.append(model.Translator.translators[model.Translator.translators.index(int(i))])


#                     resources=[]
#                     resource_id=[i.id for i in model.Translator.translators]
#                     for i in resource:
#                         if int(i) in resource_id:
#                             resources.append(model.Resources.resources[model.Resources.resources.index(int(i))])

#                     # print(categories)

#                     b1=model.Book(None,title,code,categories,age_group,release_date,authors,price,languages,publisher,designers,translators,resources)
#                     b2 =  BookDataAdapter.BookDataAdapter.insert(b1)


#                 except:
#                     print("Error")


#         else:
#             print("Error")
#     elif s[0] == "delete":
#         if len(s)==3:
#             if s[1]=="author":
#                 s=  AuthorDataAdapter.AuthorDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="publisher":
#                 s= PublisherDataAdapter.PublisherDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="language" :
#                 s= LanguageDataAdapter.LanguageDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="designer":
#                 s= DesignerDataAdapter.DesignerDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="translator":
#                 s= TranslatorDataAdapter.TranslatorDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="resource" :
#                 s= ResourcesDataAdapter.ResourcesDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")

#             elif s[1]=="category":
#                 s= CategoryDataAdapter.CategoryDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             elif s[1]=="book":
#                 s= BookDataAdapter.BookDataAdapter.delete(int(s[2]))
#                 if s==True:
#                     print("ok")
#                 else:
#                     print("False")
#             else:
#                 print("Error")

#         else:

#          print("Error")
#     elif s[0]=="exit":
#         break


# cursor.close()
# connection.close()
