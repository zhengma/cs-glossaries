# 8 Databases 数据库

## 8.1 Databse Concepts 数据库概念

### file-based approach

store data in multiple separate files.  It has many limitations in the
integrity, privacy, redundancy, inconsistency, and dependency of data.

### data redundancy 数据冗余

the same data stored more than once.

### database 数据库

a structured collection of items of data that can be accessed by different
applications.

### relational database 关系型数据库

a database model in which each item of data is stored in a relation.

### entity 实体

an object that can have data stored about it.

### relation (table) 关系（表）

the special type of table used in a relational database.

### field 字段

a column in a relation containing values.

### attribute 属性

an individual data item stored for an entity, represented by a field in a
relation.

### record 记录

a row in a relation storing data for one entity.

### tuple 元组

data that describes one instance of an entity, represented by a record in a
relation.

### candidate key 候选键

one attribute or a combination thereof for which each no tuple has the same
value.

### primary key 主键

one candidate key or a combination thereof that has been chosen as the unique
identifier of the tuples.

### secondary key 辅助索引

a candidate key that has not been chosen as the primary key.

### foreign key 外键

an attribute in one table that refers to the primary key in another table.

### relationship 关系

the situation in which one table has a foreign key that refers to a primary
key in another table in the database.  It could be one-to-one, one-to-many,
many-to-one or many-to-many.

### Entity-Relationship (E-R) model 实体关系图

a graphical representation of a database and the relationships between the
entities.

### referential integrity 参照完整性

the use of a foreign key to ensure that a value can only be entered in one
table when the same value already exists in the referenced table.

### repeating group 冗余数据组

a set of attributes that have more than one set of values when the other
attributes each have a single value.

### normalisation 规范化

organising data into two or more tables with relationships between them to
minimise data redundancy.

### first normal form (1NF) 第一范式

entities do not contain repeated groups of attributes.

### second normal form (2NF) 第二范式

entities are in 1NF and no partial dependency
any non-key attributes depend upon the primary key.

### third normal form (3NF) 第三范式

entities are in 2NF and no non-key dependency: all non-key attributes are
independent and fully dependent on the primary key only.

## 6.2 Data Management System (DBMS) 数据库管理系统

software that controls access to data in a database.

### database administrator (DBA) 数据库管理员

a person who uses the DBMS to customise the database to suit user and
programmer requirements.

### data dictionary 数据字典

data about the characteristics of the data about to be stored (metadata), such
as field names and types, table names, relationships, etc. (example: the
information specified in CREATE TABLE).

### logical schema 逻辑模式

the conceptual data model for a specific database that is independent of the
DBMS used to build that database (example: design of entities, E-R diagram).

### developer interface 开发者界面

a software tool allowing users to create items (tables, forms, reports) in the
DBMS.

### query 查询

used to select data from a database subject to defined conditions.

### query processor 查询处理器

software tools provided by a DBMS to allow creation and execution of a query.

### index 索引表

a small secondary table used for rapid searching which contains one attribute
from the table being searched and pointers to the tuples in that table.

### 6.3 DDL and DML 数据定义与操纵语言

### data definition language (DDL) 数据定义语言

a language used to create, modify and remove the data structures that form a
database.

### data manipulation language (DML) 数据操纵语言

a language used to add, modify, delete and retrieve the data stored in a
relational database.

### Structured Query Language (SQL) 结构化查询语言

the standard language used with relational database as DDL and DML.
