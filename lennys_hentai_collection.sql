/*
19.07.2020 phase 2 in dbs_project
mysql-script for creating tables in ur database

InnoDB Engine cuz features we need ...
https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html

*/
/* main table */
create table if not exists country 
(
    c_id int auto_increment primary key,
    continent varchar(100) not null,
    name varchar(255) not null,
    geo_id varchar(10) not null,
    pop_data int default null,
    gdp_per_capita float default null,
    median_age float default null,
    bed_per_1k float default null,
    first_rec date 
) engine=InnoDB;

/*

*/

/* secondary-table */
create table if not exists data_log
(
    l_id int auto_increment primary key,
    geo_id varchar(10) not null,
    date_rep date,
    cases int default null,
    deaths int default null
) engine=InnoDB;

/* maybe special DE table?? */

