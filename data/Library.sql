DROP TABLE IF EXISTS books;
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
product_code INTEGER,
age_group VARCHAR(30),
publisher_id INTEGER,
release_date VARCHAR(30),
price INTEGER
);

INSERT INTO books (`title`, `product_code`, `age_group`, `publisher_id`, `release_date`, `price`) VALUES
('The Whispering Code', 1001, 'Adult', 1, '2021-01-15', 25),
('Shadows of Eternity', 1002, 'Adult', 2, '2019-06-12', 30),
('Beyond the Horizon', 1003, 'Young Adult', 1, '2020-09-20', 22),
('The Last Algorithm', 1004, 'Adult', 3, '2022-03-10', 28),
('Silent Oceans', 1005, 'Adult', 2, '2018-11-08', 26),
('Memory of Fireflies', 1006, 'Adult', 4, '2021-07-05', 27),
('Broken Compass', 1007, 'Adult', 5, '2017-04-14', 24),
('The Crystal Path', 1008, 'Young Adult', 1, '2023-02-01', 29),
('Echoes of Tomorrow', 1009, 'Adult', 3, '2020-10-10', 31),
('River of Forgotten Dreams', 1010, 'Adult', 2, '2016-08-22', 23),
('A Thousand Lanterns', 1011, 'Young Adult', 1, '2021-09-30', 26),
('The Iron Labyrinth', 1012, 'Adult', 2, '2019-12-17', 27),
('Digital Mirage', 1013, 'Adult', 3, '2022-04-28', 32),
('Ashes and Rain', 1014, 'Adult', 4, '2018-05-19', 21),
('Clockwork Garden', 1015, 'Young Adult', 5, '2017-02-25', 28),
('Threads of Infinity', 1016, 'Adult', 1, '2021-06-11', 29),
('The Hidden Atlas', 1017, 'Adult', 2, '2019-09-07', 27),
('Stormsong', 1018, 'Young Adult', 3, '2020-01-20', 30),
('Luminous Fragments', 1019, 'Adult', 4, '2022-11-15', 19),
('The Glass Orchard', 1020, 'Adult', 5, '2018-07-13', 26);


DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100)
);

INSERT INTO categories (`name`) VALUES
('Adventure'),
('Fiction'),
('Science'),
('Fantasy'),
('Technology'),
('Poetry'),
('History');


DROP TABLE IF EXISTS authors;
CREATE TABLE IF NOT EXISTS authors (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(200),
birthdate VARCHAR(30),
nationality VARCHAR(100)
);

INSERT INTO authors (`name`, `birthdate`, `nationality`) VALUES
('Aria Collins', '1985-03-12', 'British'),
('Daniel Hartwell', '1979-07-22', 'American'),
('Sofia Marquez', '1990-02-10', 'Spanish'),
('Elias Thompson', '1982-11-15', 'Irish'),
('Hana Kobayashi', '1988-06-08', 'Japanese'),
('Marco DeLuca', '1975-09-30', 'Italian'),
('Amina Farouk', '1991-01-14', 'Egyptian'),
('Oliver Grant', '1983-12-03', 'Canadian'),
('Layla Nasser', '1987-05-25', 'Lebanese'),
('Victor Ivanov', '1970-08-19', 'Russian');


DROP TABLE IF EXISTS publishers;
CREATE TABLE IF NOT EXISTS publishers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(60),
address VARCHAR(300),
website VARCHAR(100)
);

INSERT INTO publishers (`name`, `address`, `website`) VALUES
('Aurora Press', '123 Aurora St, London, UK', 'https://aurorapress.com'),
('Horizon House', '56 Maple Ave, New York, USA', 'https://horizonhouse.com'),
('Silver Leaf Publishing', '78 Oak Rd, Toronto, Canada', 'https://silverleaf.com'),
('Crescent Moon Books', '9 Crescent Blvd, Sydney, Australia', 'https://crescentmoon.com'),
('Redwood Editions', '45 Redwood St, San Francisco, USA', 'https://redwoodeditions.com');


DROP TABLE IF EXISTS languages;
CREATE TABLE IF NOT EXISTS languages (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30)
);

INSERT INTO languages (`name`) VALUES
('English'),
('Russian'),
('Japanese'),
('Italian'),
('Spanish'),
('French'),
('German'),
('Arabic'),
('Portuguese'),
('Urdu'),
('Chinese');


DROP TABLE IF EXISTS cover_designers;
CREATE TABLE IF NOT EXISTS cover_designers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(200),
birthdate VARCHAR(30),
nationality VARCHAR(100)
);

INSERT INTO cover_designers (`name`, `birthdate`, `nationality`) VALUES
('Clara Jensen', '1986-09-12', 'Danish'),
('Miguel Alvarez', '1977-04-18', 'Spanish'),
('Priya Deshmukh', '1990-07-09', 'Indian'),
('Jonas Richter', '1981-02-28', 'German'),
('Fatima El-Sayed', '1993-11-05', 'Moroccan');


DROP TABLE IF EXISTS translators;
CREATE TABLE IF NOT EXISTS translators (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(300),
language VARCHAR(20)
);

INSERT INTO translators (`name`, `language`) VALUES
('Laura Bennett', 'French'),
('Ahmed Mansour', 'Arabic'),
('Sophie Dubois', 'Spanish'),
('Lukas Weber', 'German'),
('Yumi Tanaka', 'Japanese'),
('Pedro Silva', 'Portuguese'),
('Elena Petrova', 'Russian'),
('Farid Rahman', 'Urdu'),
('Maria Rossi', 'Italian'),
('Chen Wei', 'Chinese');


DROP TABLE IF EXISTS resources;
CREATE TABLE IF NOT EXISTS resources (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(300)
);

INSERT INTO resources (`name`) VALUES
('ISBN Registry'),
('WorldCat Catalog'),
('Google Books API'),
('Open Library'),
('Project Gutenberg'),
('JSTOR'),
('PubMed Central'),
('CrossRef'),
('DOAB'),
('Internet Archive'),
('Library of Congress'),
('British Library Catalog'),
('SpringerLink'),
('Wiley Online Library'),
('Elsevier ScienceDirect'),
('Taylor & Francis Online'),
('SAGE Journals'),
('MIT Press Open'),
('Oxford Academic'),
('Cambridge Core'),
('ACM Digital Library'),
('IEEE Xplore'),
('Scopus'),
('ERIC'),
('arXiv.org'),
('Zenodo'),
('ResearchGate'),
('Semantic Scholar'),
('Europeana Collections'),
('CORE'),
('National Library of Australia'),
('Smithsonian Digital Library'),
('HathiTrust'),
('ScienceOpen'),
('OAPEN'),
('Bookboon'),
('Directory of Open Access Journals'),
('HighWire Press'),
('EBSCOhost'),
('ProQuest'),
('CNKI Scholar'),
('Karger Journals'),
('Brill Online'),
('De Gruyter Online'),
('Maney Online'),
('Nature Publishing Group'),
('Royal Society Publishing'),
('American Chemical Society'),
('American Physical Society'),
('Annual Reviews');


DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(300),
email VARCHAR(300),
phone VARCHAR(20),
address VARCHAR(300)
);


DROP TABLE IF EXISTS book_category;
CREATE TABLE IF NOT EXISTS book_category (
book_id INTEGER,
category_id INTEGER
);

INSERT INTO book_category VALUES
(1, 2),
(1, 3),
(2, 3),
(3, 1),
(4, 2),
(4, 3),
(6, 1),
(7, 6),
(8, 3),
(9, 2),
(9, 1),
(10, 1),
(11, 3),
(13, 2),
(13, 3),
(14, 1),
(15, 3),
(16, 2),
(16, 1),
(19, 7),
(20, 1);


DROP TABLE IF EXISTS book_language;
CREATE TABLE IF NOT EXISTS book_language (
book_id INTEGER,
language_id INTEGER
);

INSERT INTO book_language (`book_id`, `language_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 10),
(12, 9),
(13, 8),
(14, 7),
(15, 6),
(16, 5),
(17, 4),
(18, 3),
(19, 2),
(20, 1);


DROP TABLE IF EXISTS book_author;
CREATE TABLE IF NOT EXISTS book_author (
book_id INTEGER,
author_id INTEGER
);

INSERT INTO book_author (`book_id`, `author_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(16, 6),
(17, 7),
(18, 8),
(19, 9),
(20, 10),
(1, 2),
(3, 4),
(5, 6),
(7, 8),
(9, 10),
(16, 1),
(17, 3),
(18, 5),
(19, 7),
(20, 9);


DROP TABLE IF EXISTS book_translator;
CREATE TABLE IF NOT EXISTS book_translator (
book_id INTEGER,
translator_id INTEGER
);

INSERT INTO book_translator (book_id, translator_id) VALUES
(1, 1),
(2, 4),
(3, 3),
(4, 10),
(5, 5),
(6, 9),
(7, 2),
(8, 6),
(9, 7),
(10, 1),
(13, 3),
(14, 7),
(15, 9),
(17, 8),
(18, 1),
(19, 5),
(20, 6);


DROP TABLE IF EXISTS book_designer;
CREATE TABLE IF NOT EXISTS book_designer (
book_id INTEGER,
designer_id INTEGER
);

INSERT INTO book_designer (`book_id`, `designer_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1),
(7, 2),
(8, 3),
(9, 4),
(10, 5),
(11, 1),
(12, 2),
(13, 3),
(14, 4),
(16, 1),
(17, 2),
(18, 3),
(19, 4),
(20, 5);


DROP TABLE IF EXISTS book_customer;
CREATE TABLE IF NOT EXISTS book_customer (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
book_id INTEGER,
rental_date VARCHAR(30),
return_date VARCHAR(30),
status VARCHAR(20)
);


DROP TABLE IF EXISTS resources_book;
CREATE TABLE IF NOT EXISTS resources_book (
book_id INTEGER,
resource_id INTEGER
);

INSERT INTO resources_book (`book_id`, `resource_id`) VALUES
(1, 3),
(2, 4),
(3, 5),
(4, 13),
(5, 10),
(7, 8),
(8, 18),
(9, 22),
(10, 27),
(11, 9),
(11,1),
(13, 21),
(14, 30),
(15, 20),
(16, 25),
(17, 26),
(18, 7),
(18,4),
(19, 17),
(20, 16);
