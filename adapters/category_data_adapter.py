from models.category import Category
import sqlite3
import datetime


class CategoryDataAdapter:

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        table = list(cursor.execute("SELECT * FROM categories;"))
        connection.close()
        return [Category(row[0], row[1]) for row in table]

    def insert(category: Category):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO categories (`name`) VALUES ('{}');".format(category.name))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Category(a, category.name)

    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()

        n = cursor.execute("Select * from categories where id=={}".format(id))
        if len(list(n)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select * from book_category where category_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from categories where id=={}".format(id))
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
            "Select * from categories where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Category(i[0], i[1]))
        connection.close()
        return lis

