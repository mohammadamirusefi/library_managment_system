# book_database


---

## 📁 Files

| Files | |
|------|-------------|
| model.py : All classes are in this file. |
| LibraryDataAdapter.py : All the work we do in SQL is in this file. |
| main.py : All requests are stated in this file. |
| Library.sql : SQL script to create the database. |
| NewLibrary.db : SQLite database file that saves data.|
| test.py : file for test the main code |



--- 
### 🟥 ` model.py`  code :

##### in this code , all tables and features are constructed and used very frequently .
---

### 🟧 ` libraryDataAdapter.py`  code :

##### this code will do all of the tasks to add and delete and search in the tables .  

---
### 🟪 ` main.py`  code :

##### use this files terminal to add and remove books and authors , etc.
---

### ➕ Add / ➖ Delete Objects

#### ⚠️ note : these text should be written in the main files `terminal`  ( ` main.py ` )
- **Add Author**  
  ``` python
  insert author [name] [birthdate] [nationality]
  ```  
- **Delete Author**  
  ```python
  delete author [author_id]
  ```  

- **Add Publisher**  
  ```python
  insert publisher [name] [address] [website]
  ```  
- **Delete Publisher**  
  ```python
  delete publisher [publisher_id]
  ```  

- **Add Language**  
  ```python
  insert language [name]
  ```  
- **Delete Language**  
  ```python
  delete language [language_id]
  ```  

- **Add Cover Designer**  
  ```python
  insert designer [name] [birthdate] [nationality]
  ```  
- **Delete Cover Designer**  
  ```python
  delete designer [designer_id]
  ```  

- **Add Translator**  
  ```python
  insert translator [name] [language]
  ```  
- **Delete Translator**  
  ```python
  delete translator [translator_id]
  ```  

- **Add Resource**  
  ```python
  insert resource [name]
  ```  
- **Delete Resource**  
  ```python
  delete resource [resource_id]
  ```  

- **Add Category**  
  ```python
  insert category [name]
  ```  
- **Delete Category**  
  ```python
  delete category [category_id]
  ```  
- **Add Book**  
  ```python
  insert book [title] [product_code] [categories] [age_group] [release_date] [authors] [price] [langugaes] [publisher_id] [designers] [translators] [resources]
  ```  
- **Delete book**
  ``` python
  Delete book : delete book [book_id]  
  ``` 
---
### 🔍 Search

  #### ⚠️ note : These codes should be written in the test file (`test.py`)

  ```python
  s = LibraryDataAdapter.("Table name")DataAdapter.search("name")
  ```

  #### for example , search among Authors:

  ```python
  s = LibraryDataAdapter.AuthorDataAdapter.search("Hana")
  ```

  the code will receive the author 's name and on the basis of the name among the same authors .
  #### and also for categories :

  ```python
  s = LibraryDataAdapter.CategoryDataAdapter.search("fiction")
  ```
  tables name for search:

 - `AuthorDataAdapter` 

 - PublisherDataAdapter

 - `CategoryDataAdapter`

 - LanguageDataAdapter

 - `DesignerDataAdapter`

 - TranslatorDataAdapter

 - `ResourcesDataAdapter`

### 📙 Book search (the strengths of the code)

- 🟡 code :

  ```python
  s = LibraryDataAdapter.BookDataAdapter.search([filters])
  ```

  #### filters you can apply :

    | | |
    |------|-------------|
    | name | translator_name |
    | author_name  | resource_name |
    | publisher_name | designer_name|
    | category_name | language_name |
  

- 🟢 example :

  ```python
  s = LibraryDataAdapter.BookDataAdapter.search(
    name="the whis", publisher_name="Press")
  ```
#### and file you can see the objects id , name , age group , etc by this code :
  ```python
  for i in s:
    print("id:", i.id, " , title:", i.title, " , product_code:", i.product_code, " , categories:", [[j.id, j.name] for j in i.categories], " , age_group:", i.age_group, " , authors:", [[j.id, j.name] for j in i.authors], " , publisher:", [
          i.publisher.id, i.publisher.name], " , release_date:", i.release_date, " , price:", i.price, " , languages:", [[j.id, j.name] for j in i.languages], " , cover_designers", [[j.id, j.name] for j in i.cover_designers], " , translators:", [[j.id, j.name] for j in i.translators], " , resources:", [[j.id, j.name] for j in i.resources], "\n")
   ```




##  How to work

1. Run the main script:  
   ```bash
   python main.py
   ```  
2. Enter a command, e.g.:  
   ```
   insert author Jim 2000-01-01 German
   ```   
   ```
   insert book nlbook 1050 [1] Adlut 2000-10-25 [1] 75 [1,2] 3 [1] [2] [4]
   ```  
   ```
   delete book 5
   ```
   ```
   delete author 2
   ```  
3. ⚪ If you want , you can search in the tables with `test.py`  , example :
   ```python
    s = LibraryDataAdapter.TranslatorDataAdapter.search("pedro")
   ```  
---

## ⚙️ Underlying Technology

- Uses Python and the built-in `sqlite3` module to manage a lightweight SQL database. :contentReference[oaicite:0]{index=0}  
- The adapter handles database connection, query execution, insertion, deletion and commit — ensuring persistent storage.  
- `Library.sql` can be used to (re)create database schema from scratch if needed.  

---

## 👍 Why This Project

This project serves as a simple but extensible example of a relational data-based library system. The system can store rich metadata: multiple authors per book, multiple languages, categories, cover designers, translators, sources, publishers, and more - allowing for complex modeling of a book library beyond simple title/author pairs.  

---
  
thanks for reading
