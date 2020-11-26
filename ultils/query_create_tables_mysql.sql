drop database if exists book_growth;
create database book_growth;

use book_growth;

CREATE TABLE attributes (
  sku varchar(255),
  name varchar(255),
  type varchar(255),
  id int,
  value_id int
);

CREATE TABLE categories (
  sku varchar(255),
  id int,
  type varchar(255),
  name varchar(255),
  parent_id int,
  level int
);

CREATE TABLE books (
  sku varchar(255) PRIMARY KEY,
  name varchar(255),
  description varchar(255),
  rating double,
  quantity_in_stock int,
  import_price int,
  final_price int,
  discount int,
  discount_percent int,
  promotion_price int,
  number_of_pages int,
  publisher varchar(255)
);


CREATE TABLE channels (
  sku varchar(255),
  id int,
  name varchar(255),
  type varchar(255)
);

CREATE TABLE quantity (
  sku varchar(255),
  last_1_week int,
  last_2_week int,
  last_3_week int,
  last_1_month int,
  last_2_month int,
  last_3_month int,
  last_1_year int
);

CREATE TABLE authors (
  id varchar(255),
  name varchar(255)
);

CREATE TABLE book_authors (
    sku varchar(255),
    author_id varchar(255)
);

CREATE TABLE value_books (
  sku varchar(255),
  id int,
  option_id int,
  value varchar(255)
);

