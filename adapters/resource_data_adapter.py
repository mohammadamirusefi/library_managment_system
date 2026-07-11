from models.resource import Resources
import sqlite3
import datetime



class ResourcesDataAdapter:

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        table = list(cursor.execute("SELECT * FROM resources;"))
        connection.close()
        return [Resources(row[0], row[1]) for row in table]

    def insert(resource: Resources):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO resources (`name`) VALUES ('{}');".format(resource.name))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Resources(a, resource.name)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        n = cursor.execute("Select * from resources where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select * from resources_book where resource_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from resources where id=={}".format(id))
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
            "Select * from resources where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Resources(i[0], i[1]))
        connection.close()
        return lis

