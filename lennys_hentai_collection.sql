/*
19.07.2020 phase 2 in dbs_project
mysql-script for creating tables in ur database

InnoDB Engine cuz features we need ...
https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html

+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| c_id         | int          | NO   | PRI | NULL    | auto_increment |
| continent    | varchar(100) | NO   |     | NULL    |                |
| name         | varchar(255) | NO   |     | NULL    |                |
| geo_id       | varchar(10)  | NO   |     | NULL    |                |
| pop_data     | int          | YES  |     | NULL    |                |
| gdp          | int          | YES  |     | NULL    |                |
| avg_age      | tinyint      | YES  |     | NULL    |                |
| bed_per_100k | tinyint      | YES  |     | NULL    |                |
| first_rec    | date         | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
 
*/
/* main table */
create table if not exists country 
(
    c_id int auto_increment primary key,
    continent varchar(100) not null,
    name varchar(255) not null,
    geo_id varchar(10) not null,
    pop_data int default null,
    gdp float default null,
    avg_age float default null,
    bed_per_100k float default null,
    first_rec date
) engine=InnoDB;

/*
+--------------+------+------+-----+---------+----------------+
| Field        | Type | Null | Key | Default | Extra          |
+--------------+------+------+-----+---------+----------------+
| l_id         | int  | NO   | PRI | NULL    | auto_increment |
| date_rep     | date | YES  |     | NULL    |                |
| cases        | int  | YES  |     | NULL    |                |
| total_cases  | int  | YES  |     | NULL    |                |
| deaths       | int  | YES  |     | NULL    |                |
| total_deaths | int  | YES  |     | NULL    |                |
| recovered    | int  | YES  |     | NULL    |                |
| c_id         | int  | NO   | MUL | NULL    |                |
+--------------+------+------+-----+---------+----------------+
*/

/* secondary-table */
create table if not exists data_log
(
    l_id int auto_increment primary key,
    date_rep date,
    cases int default null,
    total_cases int default null,
    deaths int default null,
    total_deaths int default null,
    recovered int default null,
    c_id int not null,
    constraint fk_category
    foreign key (c_id)
        references country(c_id)
        on update cascade
        on delete cascade
) engine=InnoDB;

/* maybe special DE table?? */

