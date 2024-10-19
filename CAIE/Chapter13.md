# 13 Data Representation 数据的表示

## 13.1 User-defined data types 自定义数据类型

a data type based on an existing data type or other data types that have been
**defined by the programmer**. It allows data types unavailable in a programming
language to be constructed, and hence offers flexibility.

### composite data type 复合型数据类型

a data type, ususally user-defined, that is a collection of data that can
consist of multiple elements of different or the same data types, grouped under
a single identifier. Examples: record, class, set.

### record 记录

a composite data type comprising several related items that may be of the same
or different data types.

### set 集合

a given list of **unordered, unique** elements to which set theory operations
can be applied.

### non-composite data type 非复合数据类型

a data type that is defined without referencing another data type, such as a
primitive data type found in a programming language or a user-defined data type.
Examples: enumerated, pointer.

### enumerated 枚举

a user-defined non-composite (data type) with an **ordered list** of all possible
values.

### pointer 指针

a user-defined non-composite that stores **memory addresses** only
and indicates the type of data stored in the memory location.

## 13.2 File organisation and access 文件的组织与访问

### file 文件

a collection of data stored by a computer program to be used again.
In CAIE Computer Science Paper 3, we mainly concern on data files comprising of
records, which in turn comprises of fields.

### serial file 序列文件

a file organisation in which records are physically stored one after another,
in the chronological order.

### sequential file 顺序文件

a file organisation in which records are ordered based on a value of a key field.
In order to update the file, a new version has to be created from scratch.

### random file 随机文件

also known as *direct access file*. A file organisation in which records are
stored in no particular order within the file.  The location of a record within
the file is related to the key of the record by a hashing algorithm. Updates to
the file can be carried out directly.

### file access 文件访问

physically find a record in the file.

### Sequential access 顺序访问

a method of file access in which records are searched one after another from the
physical start of the file until the required record is found.

### direct access 直接访问

also known as *random access*. A method of file access in which a record can be
physically found in a file without physically reading other records.

### hashing algorithm 哈希算法

a mathematical function that maps each input value to an output value, and
generally yields different output for different input.  In random file, hashing
algorithm maps the value of the key field to the physical location of the record.

### hash collision 哈希碰撞

when the two values, passing through a hashing algorithm, result in the same
hash value. In the storage of random file, the result is the storage location as
determined by the hashing algorithm has already been used for another record.

## 13.3 Floating-point numbers, representation and manipulation 浮点数的表示与操纵

### Mantissa 尾数

the fractional part of a floating point number.

### Exponent 指数

the power of 2 that the mantissa (fractional part) is raised to in a
floating-point number.

### Overflow 上溢

the result of carrying out a calculation which produces a value too large for
the computer’sallocated word size.

### Underflow 下溢

the result of carrying out a calculation which produces a value too small for
the computer’s allocated word size.
