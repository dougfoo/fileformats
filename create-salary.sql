# sql to create table 
#    Job Titles,Department,Annual Salary,Lname,Fname,sex

DROP TABLE salary;
DROP FOREIGN TABLE salarycs;

# bad name shoudl be non-cstore ts
CREATE TABLESPACE salaryts LOCATION '/var/lib/postgresql/10/main/cstorets';

CREATE EXTENSION cstore_fdw;
CREATE SERVER cstore_server FOREIGN DATA WRAPPER cstore_fdw;

CREATE  TABLE salary
(
    id integer NOT NULL,
    fname varchar(128) NOT NULL,
    lname varchar(128) NOT NULL,
    department varchar(128) NOT NULL,
    jobtitle varchar(128) NOT NULL,
    gender char(1) NOT NULL,
    salary integer NOT NULL
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
    salary integer NOT NULL
)
SERVER cstore_server
OPTIONS(compression 'pglz');

# Id,Title,Department,Salary,Lname,Fname,Gender no header
\COPY salarycs FROM 'chicago-salary-gender.csv' WITH CSV;

insert into salary select * from salarycs;


