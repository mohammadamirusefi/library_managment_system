from models.book import Book
import sqlite3
import datetime
import data

import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter


class BookDataAdapter:

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        sql = "SELECT id,title,product_code,age_group,publisher_id,release_date,price,author_id,category_id,designer_id,language_id,translator_id,resource_id from books LEFT JOIN book_author on book_author.book_id==books.id LEFT JOIN book_category on book_category.book_id==books.id LEFT JOIN book_designer on book_designer.book_id==books.id LEFT JOIN book_language on book_language.book_id==books.id LEFT JOIN book_translator on book_translator.book_id==books.id LEFT JOIN resources_book on resources_book.book_id==books.id "
        table = list(cursor.execute(sql))

        categories = CategoryDataAdapter.CategoryDataAdapter.get_all()
        authors = AuthorDataAdapter.AuthorDataAdapter.get_all()
        publishers = PublisherDataAdapter.PublisherDataAdapter.get_all()
        languages = LanguageDataAdapter.LanguageDataAdapter.get_all()
        cover_designers = DesignerDataAdapter.DesignerDataAdapter.get_all()
        translators = TranslatorDataAdapter.TranslatorDataAdapter.get_all()
        resources = ResourcesDataAdapter.ResourcesDataAdapter.get_all()

        books = []
        for row in table:
            book_id = row[0]
            title = row[1]
            product_code = row[2]
            age_group = row[3]
            publisher = publishers[publishers.index(row[4])]
            release_date = datetime.date.fromisoformat(row[5])
            price = row[6]

            # book_categories = [categories[categories.index(cat)] for cat in [
            #     cat_row[7] for cat_row in table if cat_row[0] == book_id] if cat is not None and not cat in book_categories]
            book_categories = []

            for cat_row in table:

                if cat_row[0] == book_id and cat_row[8] is not None and cat_row[8] not in book_categories:

                    book_categories.append(
                        categories[categories.index(cat_row[8])])

        #     book_authors = [authors[authors.index(author)] for author in [
        #         author_row[8] for author_row in table if author_row[0] == book_id] if author is not None]
            book_authors = []

            for auth_row in table:

                if auth_row[0] == book_id and auth_row[7] is not None and auth_row[7] not in book_authors:

                    book_authors.append(authors[authors.index(auth_row[7])])

        #     book_languages = [languages[languages.index(language)] for language in [
        #         language_row[9] for language_row in table if language_row[0] == book_id] if language is not None]
            book_languages = []
            for lang_row in table:
                if lang_row[0] == book_id and lang_row[10] is not None and lang_row[10] not in book_languages:
                    book_languages.append(
                        languages[languages.index(lang_row[10])])

        #     book_designers = [cover_designers[cover_designers.index(designer)] for designer in [
        #         designer_row[10] for designer_row in table if designer_row[0] == book_id] if designer is not None]
            book_designers = []
            for des_row in table:
                if des_row[0] == book_id and des_row[9] is not None and des_row[9] not in book_designers:
                    book_designers.append(
                        cover_designers[cover_designers.index(des_row[9])])

        #     book_translators = [translators[translators.index(translator)] for translator in [
        #         translator_row[11] for translator_row in table if translator_row[0] == book_id] if translator is not None]
            book_translators = []
            for tran_row in table:
                if tran_row[0] == book_id and tran_row[11] is not None and tran_row[11] not in book_translators:
                    book_translators.append(
                        translators[translators.index(tran_row[11])])

        #     book_resources = [resources[resources.index(resource)] for resource in [
        #         resources_row[12] for resources_row in table if resources_row[0] == book_id] if resource is not None]
            book_resources = []
            for res_row in table:
                if res_row[0] == book_id and res_row[12] is not None and res_row[12] not in book_resources:
                    book_resources.append(
                        resources[resources.index(res_row[12])])

            books.append(Book(
                id=book_id,
                title=title,
                product_code=product_code,
                categories=book_categories,
                age_group=age_group,
                authors=book_authors,
                publisher=publisher,
                release_date=release_date,
                price=price,
                languages=book_languages,
                cover_designers=book_designers,
                translators=book_translators,
                resources=book_resources))
        newbooks = []
        for i in books:
            status = True
            for j in newbooks:
                if j.id == i.id:
                    status = False
            if status:
                newbooks.append(i)
        connection.close()
        return newbooks

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        n = cursor.execute("Select * from books where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            cursor.execute(
                "Delete FROM book_author where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_category where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_language where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_designer where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_translator where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM resources_book where book_id=={};".format(id))
            connection.commit()
            cursor.execute("Delete FROM books where id=={};".format(id))
            connection.commit()
            connection.close()
            return True

    def insert(book: Book):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        title = book.title
        code = book.product_code
        cat = [book.categories[i].id for i in range(len(book.categories))]
        age_group = book.age_group
        release_date = book.release_date

        author = [book.authors[i].id for i in range(len(book.authors))]
        price = book.price

        language = [book.languages[i].id for i in range(len(book.languages))]
        publisher = book.publisher.id

        cover_designer = [book.cover_designers[i].id for i in range(
            len(book.cover_designers))]

        translator = [book.translators[i].id for i in range(
            len(book.translators))]

        resource = [book.resources[i].id for i in range(len(book.resources))]

        cursor.execute("INSERT INTO books (title, product_code,age_group, publisher_id, release_date, price) VALUES('{}', {}, '{}',{},'{}',{});".format(
            title, code, age_group, publisher, release_date, price))
        connection.commit()
        a = cursor.lastrowid
        for i in author:
            cursor.execute(
                "INSERT INTO book_author (`book_id`, `author_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in cat:
            cursor.execute(
                "INSERT INTO book_category (`book_id`, `category_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in cover_designer:
            cursor.execute(
                "INSERT INTO book_designer (`book_id`, `designer_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in language:
            cursor.execute(
                "INSERT INTO book_language (`book_id`, `language_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in translator:
            cursor.execute(
                "INSERT INTO book_translator (book_id, translator_id) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in resource:
            cursor.execute(
                "INSERT INTO resources_book (`book_id`, `resource_id`) VALUES({}, {});".format(a, i))
            connection.commit()

    @staticmethod
    def search(name: str = "", author_name: str = "", publisher_name: str = "", category_name: str = "", language_name: str = "", designer_name: str = "", translator_name: str = "", resource_name: str = ""):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        publishers = PublisherDataAdapter.PublisherDataAdapter.search(
            publisher_name) if publisher_name != "" else PublisherDataAdapter.PublisherDataAdapter.search("")
        publisher_id = [i.id for i in publishers if i != None]
        publishers = str(tuple(publisher_id)).replace(",)", ")")

        authors = AuthorDataAdapter.AuthorDataAdapter.search(
            author_name) if author_name != "" else AuthorDataAdapter.AuthorDataAdapter.search("")
        author_id = [i.id for i in authors if i != None]
        authors = str(tuple(author_id)).replace(",)", ")")

        categories = CategoryDataAdapter.CategoryDataAdapter.search(
            category_name) if category_name != "" else CategoryDataAdapter.CategoryDataAdapter.search("")
        category_id = [i.id for i in categories if i != None]
        categories = str(tuple(category_id)).replace(",)", ")")

        languages = LanguageDataAdapter.LanguageDataAdapter.search(
            language_name) if language_name != "" else LanguageDataAdapter.LanguageDataAdapter.search("")
        language_id = [i.id for i in languages if i != None]
        languages = str(tuple(language_id)).replace(",)", ")")

        designers = DesignerDataAdapter.DesignerDataAdapter.search(
            designer_name) if designer_name != "" else DesignerDataAdapter.DesignerDataAdapter.search("")
        designer_id = [i.id for i in designers if i != None]
        designers = str(tuple(designer_id)).replace(",)", ")")

        translators = TranslatorDataAdapter.TranslatorDataAdapter.search(
            translator_name) if translator_name != "" else TranslatorDataAdapter.TranslatorDataAdapter.search("")
        translator_id = [i.id for i in translators if i != None]
        translators = str(tuple(translator_id)).replace(",)", ")")

        resources = ResourcesDataAdapter.ResourcesDataAdapter.search(
            resource_name) if resource_name != "" else ResourcesDataAdapter.ResourcesDataAdapter.search("")
        resources_id = [i.id for i in resources if i != None]
        resources = str(tuple(resources_id)).replace(",)", ")")

        # print(publishers, authors, categories, languages,
        #       designers, translators, resources)

        s = cursor.execute("""SELECT books.id,books.title,books.product_code,books.age_group
                        ,books.publisher_id,books.release_date,books.price,author_id,category_id
                        ,designer_id,language_id,translator_id,resource_id  from books  
                         LEFT JOIN publishers on books.publisher_id = publishers.id  
                         LEFT JOIN book_author on books.id = book_author.book_id 
                         LEFT JOIN book_category on books.id = book_category.book_id 
                         LEFT JOIN book_language on books.id = book_language.book_id
                         LEFT JOIN book_designer on books.id = book_designer.book_id
                         LEFT JOIN book_translator on books.id = book_translator.book_id
                         LEFT JOIN resources_book on books.id = resources_book.book_id
                         
                         where (books.title like '%{}%') and (author_id in {}) and (publisher_id in {}) 
                         and (category_id in {}) and (designer_id in {}) and (language_id in {}) and 
                         (translator_id in {})  and (resource_id in {}) 
                         """.format(name, authors, publishers, categories, designers,
                                    languages, translators, resources))
        # print(list(s))
        table = list(s)

        categories = CategoryDataAdapter.CategoryDataAdapter.get_all()
        authors = AuthorDataAdapter.AuthorDataAdapter.get_all()
        publishers = PublisherDataAdapter.PublisherDataAdapter.get_all()
        languages = LanguageDataAdapter.LanguageDataAdapter.get_all()
        cover_designers = DesignerDataAdapter.DesignerDataAdapter.get_all()
        translators = TranslatorDataAdapter.TranslatorDataAdapter.get_all()
        resources = ResourcesDataAdapter.ResourcesDataAdapter.get_all()

        books = []
        for row in table:
            book_id = row[0]
            title = row[1]
            product_code = row[2]
            age_group = row[3]
            publisher = publishers[publishers.index(row[4])]
            release_date = datetime.date.fromisoformat(row[5])
            price = row[6]

            # book_categories = [categories[categories.index(cat)] for cat in [
            #     cat_row[7] for cat_row in table if cat_row[0] == book_id] if cat is not None and not cat in book_categories]
            book_categories = []

            for cat_row in table:

                if cat_row[0] == book_id and cat_row[8] is not None and cat_row[8] not in book_categories:

                    book_categories.append(
                        categories[categories.index(cat_row[8])])

        #     book_authors = [authors[authors.index(author)] for author in [
        #         author_row[8] for author_row in table if author_row[0] == book_id] if author is not None]
            book_authors = []

            for auth_row in table:

                if auth_row[0] == book_id and auth_row[7] is not None and auth_row[7] not in book_authors:

                    book_authors.append(authors[authors.index(auth_row[7])])

        #     book_languages = [languages[languages.index(language)] for language in [
        #         language_row[9] for language_row in table if language_row[0] == book_id] if language is not None]
            book_languages = []
            for lang_row in table:
                if lang_row[0] == book_id and lang_row[10] is not None and lang_row[10] not in book_languages:
                    book_languages.append(
                        languages[languages.index(lang_row[10])])

        #     book_designers = [cover_designers[cover_designers.index(designer)] for designer in [
        #         designer_row[10] for designer_row in table if designer_row[0] == book_id] if designer is not None]
            book_designers = []
            for des_row in table:
                if des_row[0] == book_id and des_row[9] is not None and des_row[9] not in book_designers:
                    book_designers.append(
                        cover_designers[cover_designers.index(des_row[9])])

        #     book_translators = [translators[translators.index(translator)] for translator in [
        #         translator_row[11] for translator_row in table if translator_row[0] == book_id] if translator is not None]
            book_translators = []
            for tran_row in table:
                if tran_row[0] == book_id and tran_row[11] is not None and tran_row[11] not in book_translators:
                    book_translators.append(
                        translators[translators.index(tran_row[11])])

        #     book_resources = [resources[resources.index(resource)] for resource in [
        #         resources_row[12] for resources_row in table if resources_row[0] == book_id] if resource is not None]
            book_resources = []
            for res_row in table:
                if res_row[0] == book_id and res_row[12] is not None and res_row[12] not in book_resources:
                    book_resources.append(
                        resources[resources.index(res_row[12])])

            books.append(Book(
                id=book_id,
                title=title,
                product_code=product_code,
                categories=book_categories,
                age_group=age_group,
                authors=book_authors,
                publisher=publisher,
                release_date=release_date,
                price=price,
                languages=book_languages,
                cover_designers=book_designers,
                translators=book_translators,
                resources=book_resources))
        newbooks = []
        for i in books:
            status = True
            for j in newbooks:
                if j.id == i.id:
                    status = False
            if status:
                newbooks.append(i)
        connection.close()
        return newbooks
