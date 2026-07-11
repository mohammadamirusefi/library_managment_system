from models.translator import Translator
import sqlite3
import datetime
import adapters.language_data_adapter as LanguageDataAdapter


class TranslatorDataAdapter:

    @staticmethod
    def get_all():
        
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        table = list(cursor.execute("SELECT * FROM translators;"))
        languages = LanguageDataAdapter.LanguageDataAdapter.get_all()
        connection.close()
        return [Translator(row[0], row[1], list(filter(lambda lang: lang.name == row[2], languages))) for row in table]

    def insert(translator: Translator):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO translators (`name`,`language`) VALUES ('{}','{}');".format(
            translator.name, translator.languages))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Translator(a, translator.name, translator.languages)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        n = cursor.execute("Select * from translators where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select * from book_translator where translator_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from translators where id=={}".format(id))
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
                return False

    @staticmethod
    def search(name: str):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        s = cursor.execute(
            "Select * from translators where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Translator(i[0], i[1], i[2]))
        connection.close()
        return lis

