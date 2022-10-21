CREATE DATABASE School;
show databases;

use school;

CREATE table Student(
	StudentId	integer,
    Fname	varchar(10),
    Gender	char(1),
    DOJ		date
);

SHOW tables;

drop table Student;


CREATE table Student(
	StudentId  integer not null,
    Fname	varchar(10),
    Gender	char(1),
    DOJ		date
);

CREATE table Student(
	StudentId  integer,
    Fname	varchar(10),
    Gender	char(1),
    DOJ	date default curdate()
);

select curdate();



