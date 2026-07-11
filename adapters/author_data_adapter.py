from models.author import Author
import sqlite3
import datetime



class AuthorDataAdapter:

    @staticmethod
    def update(id:int,name:str,birthdate: datetime.date,nationality:str):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        s = cursor.execute("""Update authors
                                   SET name='{}',birthdate='{}',nationality='{}'
                                   where id={};""".format(name,str(birthdate),nationality,id))
        connection.commit()
        connection.close()
        return 
        
    @staticmethod
    def get_one(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        s = cursor.execute("Select * from authors where id=={}".format(id))
        lis = []
        for i in s:
            lis.append(Author(i[0], i[1], i[2], i[3]))
        connection.close()
        return lis

    @staticmethod
    def get_all():
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        table = list(cursor.execute("SELECT * FROM authors;"))
        connection.close()
        return [Author(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in table]

    @staticmethod
    def delete(id: int):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        s = cursor.execute("Select * from authors where id=={}".format(id))
        if len(list(s)) == 0:
            connection.close()
            return False
        else:
            s = cursor.execute(
                "Select author_id from book_author where author_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from authors where id=={}".format(id))
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
                return False

    def insert(author: Author):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (`name`,`birthdate`,`nationality`) VALUES ('{}','{}','{}');".format(
            author.name, author.birthdate, author.nationality))
        connection.commit()
        a = cursor.lastrowid
        connection.close()
        return Author(a, author.name, author.birthdate, author.nationality)

    @staticmethod
    def search(name: str):
        connection = sqlite3.connect("../data/NewLibrary.db")
        cursor = connection.cursor()
        s = cursor.execute(
            "Select * from authors where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(Author(i[0], i[1], i[2], i[3]))
        connection.close()
        return lis

