# sql to create table 
#    Job Titles,Department,Annual Salary,Lname,Fname,sex

DROP TABLE salary;
DROP TABLE salarycs;

CREATE TABLESPACE salaryts LOCATION '/var/lib/postgresql/12/main/dtestdir';


CREATE FOREIGN TABLE salary
(
    id integer NOT NULL,
    fname varchar(128) NOT NULL,
    lname varchar(128) NOT NULL,
    department varchar(128) NOT NULL,
    jobtitle varchar(128) NOT NULL,
    gender char(1) NOT NULL,
    salaryk integer NOT NULL
)
tablespace salaryts;

CREATE FOREIGN TABLE salarycs
(
    id integer NOT NULL,
    fname varchar(128) NOT NULL,
    lname varchar(128) NOT NULL,
    department varchar(128) NOT NULL,
    jobtitle varchar(128) NOT NULL,
    gender char(1) NOT NULL,
    salaryk integer NOT NULL
)
SERVER cstore_server
OPTIONS(compression 'pglz');
