from models.language import Language
import sqlite3
import datetime

class LanguageDataAdapter:
    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        table = list(cursor.execute("SELECT * FROM languages;"))
        connection.close()
        return [Language(row[0], row[1]) for row in table]

    def insert(language: Language):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO languages (`name`) VALUES ('{}');".format(language.name,))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Language(a, language.name)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        n = cursor.execute("Select * from languages where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select * from book_language where language_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from languages where id=={}".format(id))
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
            "Select * from languages where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Language(i[0], i[1]))
        connection.close()
        return lis

