from models.publisher import Publisher
import sqlite3
import datetime



class PublisherDataAdapter:

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        table = list(cursor.execute("SELECT * FROM publishers;"))
        connection.close()
        return [Publisher(row[0], row[1], row[2], row[3]) for row in table]

    def insert(publisher: Publisher):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO publishers (`name`,`address`,`website`) VALUES ('{}','{}','{}');".format(
            publisher.name, publisher.address, publisher.website))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Publisher(a, publisher.name, publisher.address, publisher.website)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        n = cursor.execute("Select * from publishers where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select publisher_id from books where publisher_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from publishers where id=={}".format(id))
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
            "Select * from publishers where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Publisher(i[0], i[1], i[2], i[3]))
        connection.close()
        return lis
