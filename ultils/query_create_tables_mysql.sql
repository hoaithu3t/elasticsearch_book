drop database if exists book_growth;
create database book_growth;

use book_growth;

drop table if exists books;
create table books (
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

drop table if exists authors;
create table authors (
  id varchar(255),
  name varchar(255)
);

drop table if exists attributes;
create table attributes (
  sku varchar(255),
  name varchar(255),
  type varchar(255),
  id int,
  value_id int
);

drop table if exists categories;
create table categories (
  sku varchar(255),
  id int,
  type varchar(255),
  name varchar(255),
  parent_id int,
  level int
);

drop table if exists channels;
create table channels (
  sku varchar(255),
  id int,
  name varchar(255),
  type varchar(255)
);

drop table if exists quantity;
create table quantity (
  sku varchar(255),
  last_1_week int,
  last_2_week int,
  last_3_week int,
  last_1_month int,
  last_2_month int,
  last_3_month int,
  last_1_year int
);

drop table if exists book_authors;
create table book_authors (
    sku varchar(255),
    author_id varchar(255)
);

drop table if exists value_books;
create table value_books (
  sku varchar(255),
  id int,
  option_id int,
  value varchar(255)
);

alter table attributes
add foreign key (sku) references books(sku);

alter table categories
add foreign key (sku) references books(sku);

alter table channels
add foreign key (sku) references books(sku);

alter table quantity
add foreign key (sku) references books(sku);

alter table value_books
add foreign key (sku) references books(sku);

alter table book_authors
add foreign key (sku) references books(sku);

alter table book_authors
add foreign key (author_id) references authors(id);
