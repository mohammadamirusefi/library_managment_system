from models.designer import CoverDesigner
import sqlite3
import datetime

class DesignerDataAdapter:

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        table = list(cursor.execute("SELECT * FROM cover_designers;"))
        connection.close()
        return [CoverDesigner(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in table]

    def insert(designer: CoverDesigner):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cover_designers (`name`,`birthdate`,`nationality`) VALUES ('{}','{}','{}');".format(
            designer.name, designer.birthdate, designer.nationality))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return CoverDesigner(a, designer.name, designer.birthdate, designer.nationality)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        n = cursor.execute(
            "Select * from cover_designers where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select * from book_designer where designer_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from cover_designers where id=={}".format(id))
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
            "Select * from cover_designers where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(CoverDesigner(i[0], i[1], i[2], i[3]))
        connection.close()
        return lis

