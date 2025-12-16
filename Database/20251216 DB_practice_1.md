Basic database and table creation



1\. create database

CREATE DATABASE company\_1;



2\. USE company\_1;



3\. CREATE TABLE vendors (v1 VARCHAR(20), v2 VARCHAR(20), 

v3 VARCHAR(20), founded DATE);



3\. SHOW TABLES;



4\. DESCRIBE vendors;



5\. mysql> SELECT v1, founded FROM vendors;



============================================================================================

【MySWL 8.0 Command Line Client】/ Execution result



mysql> USE company\_1;

Database changed

mysql> CREATE TABLE vendors (v1 CHAR(10), v2 VARCHAR(20), v3 VARCHAR(25), founded DATE);

Query OK, 0 rows affected (0.08 sec)



mysql> SHOW TABLES;

+---------------------+

| Tables\_in\_company\_1 |

+---------------------+

| vendors             |

+---------------------+

1 row in set (0.01 sec)



mysql> DESCRIBE vendors;

+---------+-------------+------+-----+---------+-------+

| Field   | Type        | Null | Key | Default | Extra |

+---------+-------------+------+-----+---------+-------+

| v1      | char(10)    | YES  |     | NULL    |       |

| v2      | varchar(20) | YES  |     | NULL    |       |

| v3      | varchar(25) | YES  |     | NULL    |       |

| founded | date        | YES  |     | NULL    |       |

+---------+-------------+------+-----+---------+-------+

4 rows in set (0.01 sec)



mysql> SELECT v1, founded FROM vendors;

Empty set (0.00 sec)

====================

