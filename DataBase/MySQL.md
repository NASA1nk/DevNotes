# 部署MySQL

## 获取配置目录

- `/etc/mysql/`是docker中配置文件的文件夹
- `/var/lib/mysql/`是docker中数据的文件夹
- `/var/log/mysql`是docker中mysql日志的文件夹

```mysql
# 下载镜像
docker pull mysql:5.7
# 查看
docker images | grep mysql
# 创建
docker run --name=mysql -p 3307:3306 -d -e MYSQL_ROOT_PASSWORD=1 mysql:5.7
```

![mysql配置文件](MySQL.assets/mysql配置文件.png)

![mysql数据文件](MySQL.assets/mysql数据文件.png)

![mysql日志文件](MySQL.assets/mysql日志文件.png)



## 创建映射目录

- 配置目录：`/home/dog/yinke/mysql/conf`
- 数据目录：`/home/dog/yinke/mysql/data`
- 日志目录：`/home/dog/yinke/mysql/log`

在`conf`目录下创建`my.cnf`配置文件

```bash
[mysqld]
user=mysql
character-set-server=utf8
default_authentication_plugin=mysql_native_password
secure_file_priv=/var/lib/mysql
expire_logs_days=7
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
max_connections=1000

[client]
default-character-set=utf8

[mysql]
default-character-set=utf8
```



## 创建MySQL容器

- `--restart=always`： Docker重启时容器会自动启动
- `--privileged=true`：容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限


```bash
# 删除上一步创建的mysql容器
docker kill 21b7a7edd083
docker rm 21b7a7edd083

-v /home/mysql/conf.d:/etc/mysql/conf.d 
-v /home/mysql/my.cnf:/etc/mysql/my.cnf -p 33306:3306 --name my-mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7


# 运行mysql容器
docker run --restart=always --privileged=true -d -p 3306:3306 --name inkmysql -v /home/dog/yinke/mysql/conf/my.cnf:/etc/mysql/my.cnf -v /home/dog/yinke/mysql/data:/var/lib/mysql -v /home/dog/yinke/mysql/log:/var/log/mysql -e MYSQL_ROOT_PASSWORD=1 mysql:5.7
```



## 查看MySQL容器ip

172.17.0.9

```bash
# 在显示信息里面找
# "NetworkSettings"的"IPAddress"
docker inspect

# -f直接指定查看ip
docker inspect --format='{{.NetworkSettings.IPAddress}}' a9757d991f3c
```



## 启动MySQL数据库

- `-u`后面可以省略空格
- `-p`指定密码时中间不能有空格

> MySQL的第一个非选项参数被当作默认数据库的名称，如果没有这样的选项MySQL就不会选择默认数据库
>
> 所以说在命令行中，root的密码和`-p`或者`--password`参数之间有空格的话，MySQL会认为输入的是登录mysql后自动选择的数据库而不是密码

```bash
# 进入mysql容器
docker exec -it a9757d991f3c /bin/bash

# 直接用密码登录
mysql -uroot -p1

# 交互输入密码登录
mysql -u root -p
```



## 配置远程连接

要想在外部连接MySQL容器进行远程管理，就需要配置容器里的MySQL的root账户的主机host

- 将它修改成通配符`％`，这样就可以让任意主机连接MySQL容器

> 一般MySQL中默认的`host`是`localhost`，可以以`root`用户登录MySQL
>
> MySQL使用mysql数据库中的user表来管理权限，修改user表就可以修改权限（只有root账号可以修改）

```mysql
# 查看数据库
show databases;

# 选择数据库
use mysql;

# 查看数据库的表
show tables;

# 查看user表信息
show table status like 'user'\G;

# 查看user表的所有字段信息
show full columns from user;

# 查看Host字段的信息
SELECT Host FROM user;

# 查看2个字段信息
select user, host from user;

# 修改配置
update user set host ='％'where user ='root'

# 允许任何主机使用root账号和root的密码连接到mysql服务器
# mysql8之后要求先创建用户再授权，而不能在授权时创建用户
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '1' WITH GRANT OPTION;

# 刷新
flush privileges;
```



## 导入数据

拷贝sql文件到MySQL容器中

```bash
#docker cp 宿主机文件路径 容器id:拷贝到容器里面的绝对路径
docker cp /home/dog/yinke/mysql/CrashCourse/create.sql a9757d991f3c:/root/course
docker cp /home/dog/yinke/mysql/CrashCourse/populate.sql a9757d991f3c:/root/course
```

## 创建数据库

DATABASE（数据库）或者SCHEMA（模式）都可以

> `CREATE Schema databaseName;`
>
> `show Schemas;`

```mysql
# 创建数据库
CREATE DATABASE course；
# 切换
use course;
# 提示Query OK，表示sql文件已经被成功执行
source /root/course/create.sql;
source /root/course/populate.sql;
```



# DataGrip

## 连接数据库

输入MySQL服务器的url，用户和密码

![datagrip连接](MySQL.assets/datagrip连接.png)

## 打开控制台

右键数据库或表，打开控制台，就可以写sql

![datagripconsole](MySQL.assets/datagripconsole.png)



## 执行sql

- 打开sql文件运行
- 在控制台（console）运行（
  - 快捷键：`ctrl+enter`

> 可以运行sql文件作为一个整体



# MySQL基本概念

## DBMS数据库管理系统

MySQL是数据库软件（DBMS）

数据库（database）是通过数据库软件创建和操作的容器，使用DBMS访问数据库

## table表

特定类型数据的结构化清单

- 数据库中表的名字是唯一的
- 表具有一些特性，描述表的这组信息就**模式**

> 模式用来描述数据库中特定的表以及整个数据库（和其中表的关系）

### col列

表中的一个字段

每个col都有相应的数据类型（datatype）

### row行

表中的一个记录

表中数据按行存储

> 相当于数据库记录（record）

### primary key主键

表中一列（或一组列），其值能唯一区分表中的每一行，这个列（或一组列）成为主键

- 每个表应该都具有一个主键
- 表中任意列都可以作为主键，主要满足
  - 任意两行都具有不同的值
  - 每个行都具有一个值

> 主键不允许`NULL`值

## schema模式

关于数据库和表的布局及特性的信息

通常模式可以作为数据库的同义词

## SQL

structed query language结构化查询语句

- sql语句不区分大小写
- sql语句所有空格都被忽略
- sql语句可以分成多行书写，最后以分号`;`结束
- 多条sql语句必须以分号`;`分隔

> MySQL不需要在单条sql语句后加分号`;`，但是mysql命令行上必须加分号`;`

### 连接数据库

1. 查看数据库
   1. `show databases;`
2. 连接数据库
   1. `use databaseName;`

### auto_increment自动增量

某些表的列需要唯一值，MySQL可以自动为每一行分配一个可用值

> 需要create创建表时把它作为表定义的组成部分

### DESCRIBE

`show columns from`的快捷方式

`describe customers` = `show columns from customers`



### 子句

SQL语句由子句构成

子句通常由关键字和数据组成，如`select`的`from`子句



# 检索数据

- `select`

## 检索单列

`select prod_name from products;`

查询语句如果未过滤或排序，则返回结果的顺序无意义

## 检索多列

`select prod_id,prod_name,prod_price from products;`

col之间用逗号`,`隔开

![检索多列](MySQL.assets/检索多列.png)

## 检索所有列

`select * from table;`

使用通配符`*`

- 返回所有col的顺序无意义
- 可以检索出名字未知的col



## 检索不同行

`select distinct vend_id from products;`

`distinct`

- 只返回不同的值
- 必须直接放在col的前面
- 会应用于后面的所有col

> distinct：清晰的; 清楚的; 明白的; 明显的; 截然不同的; 有区别的; 不同种类的; 确定无疑的; 确实的; 确切的



## 限制结果

`select prod_name from products limit 10;`

`select prod_name from products limit 5,5;`

`limit`

- 限制返回不多于n col
- 指定返回从n到m的col（闭区间[n,m]）
- 必须在`order by`子句之后

> 检索结果从col 0开始

## 完全限制

`select products.prod_name from products;`

`select products.prod_name from course.products;`

同时使用database，table和col指定检索



# 排序检索数据

- `select`
- `order by`

检索返回的col不是纯粹的随机顺序，一般是将以它在底层table中出现的顺序，可能是数据最开始添加到table中的顺序，但是数据经过更新或者删除，顺序就会受到MySQL重用回收空间的影响

> 关系型数据库设计理论认为，如果不明确规定排序，就不应该假定检索出的数据的顺序有序

## 排序数据

`select prod_name from products order by prod_name;`

`order by`子句

- 默认以字母升序排序（`ASC`）
- 也可以用非检索的列排序
- 必须在`from`子句之后

## 按多个列排序

`select prod_price,prod_name from products order by prod_price,prod_name;`

指定col，用逗号`,`分开

- 排序按指定的col执行
- 只有第一个col排序具有相同的值的情况才会按照第二个col进行排序
- 如果第一个col排序没有相同的，则不会再根据第二个col进行排序

## 指定排序方向

`select prod_id,prod_price,prod_name from products order by prod_price desc;`

`select prod_id,prod_price,prod_name from products order by prod_price desc,prod_name;`

`desc`

- 按降序排列
- 只应用于直接位于其前面的col
- 不直接位于`desc`前面的col仍默认按升序排列
- 如果要在多个col上进行降序排序，必须每一个都指定`desc`

> 可以用`ASC`指定升序，但默认就是升序
>
> 可以结合`limit`检索最值



# 过滤数据

- `select`

- `where`

  - 操作符：`>`,`<`,`>=`,`<=`,`!=`,`<>`,`between`

  - 在`from`子句之后
  - 在`order by`子句之前
  - 不区分大小写

通常根据指定的搜索条件（search criteria）提取table的子集

> 搜索条件也称为过滤条件（filter condition）

## 搜索条件

`select prod_name,prod_price from products where prod_price = 2.5;`

`select prod_name,prod_price from products where prod_name = 'safe';`

`select prod_name,prod_price from products where prod_price <= 10;`

> 相等测试：检索一个col是否有指定的值
>
> `单引号`用来限定字符串

## 不匹配检查

`select prod_name,prod_price from products where prod_price <> 10;`

`select prod_name,prod_price from products where prod_price != 10;`

## 范围值检查

`select prod_name,prod_price from products where prod_price between 5 and 10;`

`between`

- 指定范围的低端值和高端值
- 低端值和高端值用`and`连接

## 空值检查

`select prod_name,prod_price from products where prod_price is null;`

`select cust_id from customers where cust_email is null;`

`is null`子句

- 一个col不包含值时，称为包含空值`null`
- `null`指无值（no value），和0,空字符串，空格不同
- `null`值不会包含在不匹配的返回数据中（数据库不知道是否匹配）

## 组合过滤

通过逻辑操作符（logical operator）连结多个`where`子句

- `and`
- `or`
- `in`
- `not`

`and`优先级大于`or`，需要使用圆括号`()`来设置计算次序

> `where`子句可以包含任意的`and`和`or`操作符

### and操作符

`select prod_id,prod_price,prod_name from products where vend_id = 1003 and prod_price <= 10;`

检索匹配多个条件

### or操作符

`select prod_price,prod_name from products where vend_id = 1003 or vend_id = 1002;`

检索匹配任一条件

### in操作符

`select prod_name,prod_price from products where vend_id in (1002,1003) order by prod_name;`

`select prod_name,prod_price from products where vend_id = 1002 or vend_id = 1003 order by prod_name;`

`in`

- 指定条件范围（范围中的每个条件都可以进行匹配）
- 实现功能和`or`相同，但是有很多优点
  - 使用长的合法选项清单时，`in`的语法更清楚直观
  - `in`的计算次序更容易管理
  - `in`一般比`or`快
  - `in`可以包含其他`select`子句

### not操作符

`select prod_name,prod_price from products where vend_id not in (1002,1003) order by prod_name;`

`not`

- 否定`not`之后的所有条件
- 一般和`in`联合使用
- MySQL支持`not`对`in`,`betweed`,`exists`子句取反

## 通配符过滤

- 通配符（wildcard）
  - 用来匹配值的一部分的特殊字符
- 搜索模式（search pattern）
  - 由字面值，通配符或二者结合组合成的搜索条件（search criteria）
- `Like`操作符
  - 指示MySQL后面跟的搜索模式利用通配符匹配而不是直接相等匹配

**注意**

- 通配符的搜索处理要花费更多时间
- 一般不要将通配符放在搜索模式的开始处

> 之前的数据过滤都是基于已知值的
>
> wildcard即sql中`where`子句中有特殊含义的字符

### 百分号%操作符

`select prod_id,prod_name from products where prod_name like 'jet%';`

`select prod_id,prod_name from products where prod_name like '%anvil%';`

`select prod_id,prod_name from products where prod_name like 's%e';`

`%`

- 匹配任意个数的任意字符
- 可以匹配0个字符，但无法匹配空值`null`
- 通配符可以在搜索模式的任意位置使用，并且可以使用多个通配符

> `'jet%'`：匹配由`jet`开头的，后面是任意个数的任意字符的值
>
> `'%anvil%'`：匹配包含`anvil`的值，`anvil`前后可以是任意个数的任意字符
>
> `'s%e'`：匹配由`s`开头，`e`结尾的，中间可以是任意个数的任意字符的值

### 下划线_操作符

`select prod_id,prod_name from products where prod_name like '_ ton anvil';`

`_`

- 匹配单个任意字符



# 正则表达式搜索

- 正则表达式（regexp）是用来匹配文本的特殊的字符集合

- MySQL允许使用正则表达式过滤select检索出来的数据
  - MySQL仅支持多数正则表达式实现的一个子集
- `regexp`操作符
  - 指示MySQL后面跟的搜索模式利用正则表达式匹配

> 所有种类的程序设计语言，文本编辑器和操作系统都支持正则表达式

## 基本字符匹配

`select prod_id,prod_name from products where prod_name regexp '1000';`

`select prod_id,prod_name from products where prod_name regexp '.000';`

`.`

- 用于匹配任意一个字符
- `regexp`是col值内匹配
- `like`是col整行值匹配

`binary`

- 用于匹配区分大小写

> 默认不区分大小写

## or匹配

`select prod_id,prod_name from products where prod_name regexp '1000|2000' order by prod_name;`

`|`

- 用于匹配其中的一个条件

## 匹配几个字符之一

`select prod_id,prod_name from products where prod_name regexp '[123] Ton' order by prod_name;`

`[]`

- 匹配方括号中的任意一个字符

> [123]相当于[1|2|3]

## 反义匹配

`select prod_id,prod_name from products where prod_name regexp '[^123] Ton' order by prod_name;`

`[^]`

- 匹配除了指定字符外的所有字符

> 需要在`[]`中来否定指定的字符集

## 匹配范围

`select prod_id,prod_name from products where prod_name regexp '[0-9] Ton' order by prod_name;`

`-`

- 定义一个范围

## 匹配特殊字符

`select prod_id,prod_name from products where prod_name regexp '\\.' order by prod_name;`

`\\`

- 用来匹配转义字符（正则表达式所用的特殊字符）
- `\\f`：换页
- `\\n`：换行
- `\\r`：回车
- `\\\`：`\`本身

## 匹配字符类

字符类（character class）

- 预定义的字符集
- `[[:alnum:]]`：文字，数字字符
- `[[:alpha:]]`：字母字符
- `[[:lower:]]`：小写字母
- `[[:upper:]]`：大写字母
- `[[:digit:]]`：小数
- `[[:space:]]`：空格
- `[[:punct:]]`：标点符号

## 匹配多个实例

`select prod_name from products where prod_name regexp '\\([0-9] sticks?\\)' order by prod_name;`

`select prod_name from products where prod_name regexp '[[:digit:]]{4}' order by prod_name;`

> - `s?`用于匹配0个或者1个`s`，这样可以匹配出`stick`和`sticks`
> - `[[:digit:]]{4}`：也可以表示为`[0-9][0-9][0-9][0-9]`

控制匹配的字符的个数

- `*`：匹配0个或者多个
- `+`：匹配1个或者多个
- `?`：匹配0个或者1个
- `{n}`：指定匹配n个
- `{n,}`：指定匹配n个或者更多个
- `{n,m}`：指定匹配的个数不少于n个，不多于m个（m<=255）

![正则匹配多个实例](MySQL.assets/正则匹配多个实例.png)

## 位置匹配

`select prod_name from products where prod_name regexp '^[0-9\\.]' order by prod_name;`

> 以数字或者小数点开头的字符

定位符用来限制搜索匹配字符所在的位置

- `^`：文本开始
- `$`：文本结尾
- `[[:<:]]`：词的开始
- `[[:>:]]`：词的结尾

> 使用定位符可以让`regexp`和`like`达到同一个效果



# 计算字段

存储在table中的数据往往不是直接需要的（不同的信息包含在不同的table和col中），所以要在database中检索出计算或格式化后的数据再返回

- 字段（`field`）：与col同义
- 计算字段运行时在select语句中创建
- 只有database知道select语句中哪些col是实际存储的col，哪些col是计算字段

> DBMS设计用来快速转换，所以不在应用程序端处理

## 拼接字段

拼接（concatenate）

`Concat()`：MySQL的拼接函数

- 指定一个或多个串，用逗号隔开

> 多数DBMS使用`+`和`||`来拼接，所以将SQL语句转换为MySQL语句时要注意

`select Concat(vend_name,'(',vend_country,')') from vendors order by vend_name;`

`select Concat(rtrim(vend_name),'(',rtrim(vend_country),')') from vendors order by vend_name;`

> - `trim()`：去掉串左右两边的空格
> - `rtrim()`：去掉串右边的空格
> - `ltrim()`：去掉串左边的空格

![Concat拼接函数](MySQL.assets/Concat拼接函数.png)

## 字段别名

拼接后的col并没有名字，所以应用程序无法引用它

alias

- 一个字段或者值的替换名
- 使用`as`关键字赋予别名

> as指示SQL创建一个指定名字的计算字段的col，就像一个实际的col一样
>
> 别名也称为导出列（derived col）

`select Concat(rtrim(vend_name),'(',rtrim(vend_country),')') as vend_titile from vendors order by vend_name;`

![别名alias](MySQL.assets/别名alias.png)

## 算术计算

对检索出来的数据进行计算

`select prod_id,quantity,item_price,quantity*orderitems.item_price as expanded_price from orderitems where order_num=20005;`

> `expanded_price` col是一个计算字段

![算术运算](MySQL.assets/算术运算.png)



# 数据处理函数