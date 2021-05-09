

# 相关概念

数据是描述现实世界中的各种事物的可以识别的符号。

信息是一种已经被加工为特定形式的数据。

数据是信息的载体，是信息的具体表现形式。数据只有被加工从成信息，才具有使用价值。



一个数据库事务通常包含了一个序列的对数据库的读/写操作

SQL 结构化查询语言  structured query language



### **事务的ACID特性**

原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么全部不执行
一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序 串行执行的结果相一致
隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
持久性(Durability):对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障



# Neo4j

### 服务器DB

账号:   neo4j

密码：123456

```xshell
数据路径：/var/lib/neo4j/data/databases/graph.db
删除数据库：rm -rf /var/lib/neo4j/data/databases/graph.db
```



### 导入数据

**CSV文件**

CSV 是逗号分隔值的文件。neo4j是utf-8的，而CSV默认保存是ANSI的，需要用记事本另存为成UTF-8

使用**LOAD CSV**命令将CSV文件导入到：**/var/lib/neo4j/import**

```
LOAD CSV WITH HEADERS FROM “file:///file.name” AS line
```

将指定路径下的CSV文件读取出来，其中“file-url”是文件的地址，可以是本地文件路径也可以是网址（但是必须设置权限，以便外部源可以读取该文件）。

with headers是在导入CSV时附带上头部，**从文件中读取第一行作为参数名**，只有在使用了该参数后，才可以使用line.name这样的表示方式。否则需要使用{movieId:line[0],name1:line[1],year:line[2],tag:line[3]}的表示方式。每个节点的属性由导入的CSV文件的每行指定。

CSV 文件的所有数据都读取为**字符串**，需要使用`toInteger(),toFloat(),split()`(Cypher函数,分隔单元格中的数组)来转换。

**导入节点文件创建节点**

```
load csv with headers from "file:/var/lib/neo4j/import/entity.csv" as line
create(entity:entity{id:line.id, name:line.name})
```

```
load csv with headers from "file:/var/lib/neo4j/import/trainticket.csv" as line
create(ticket:ticket{id:line.id,uri:line.URI,method:line.HttpMethod,description:line.Description})
```

**导入关系创建关系**

```CQL
load csv with headers from "file:/var/lib/neo4j/import/a2e.csv" as line
match(from:ticket{id:line.from}),(to:entity{id:line.to})
create(from)-[r:belong{rel:line.rel}]->(to)
```

```CQL
load csv with headers from "file:/var/lib/neo4j/import/e2e.csv" as line
match(from:entity{name:line.from}),(to:entity{name:line.to})
create(from)-[r:relative{rel:line.rel}]->(to)
```





### **构建neo4j容器**

在根目录的任意一个子目录（我这里是/home)下建立四个基本的文件夹用于挂在容器目录

- data——数据存放的文件夹

- logs——运行的日志文件夹

- conf——数据库配置文件夹（在配置文件**neo4j.conf**中配置包括开放远程连接、设置默认激活的数据库）

- import——批量导入csv文件，节点文件**node.csv**和关系文件**rel.csv**需要放到这个文件夹下）

  

**官方文档说明**

> which allows you to access neo4j through your browser at [http://localhost:7474](http://localhost:7474/).（默认的neo4j浏览器）
>
> This binds two ports (`7474` and `7687`) for HTTP and Bolt access to the Neo4j API. （开放2个端口）
>
> A volume is bound to `/data` to allow the database to be persisted outside the container.（将data挂载出来持久化存储）
>
> By default, this requires you to login with `neo4j/neo4j` and change the password. （默认的账号和密码都是neo4j）
>
> You can, for development purposes, disable authentication by passing `--env=NEO4J_AUTH=none` to docker run.
>
> （--env=NEO4J_AUTH=neo4j/123456  就是指定 neo4j 的用户名和密码
>
> ​	--env=NEO4J_AUTH=none                 就是不设置密码）



**运行neo4j容器**

```
docker run -d --name container_name \        
 -p 7474:7474 -p 7687:7687 \                                         
 -v /home/neo4j/data:/data \                                      
 -v /home/neo4j/logs:/logs \                                        
 -v /home/neo4j/conf:/var/lib/neo4j/conf \              
 -v /home/neo4j/import:/var/lib/neo4j/import \     
 --env NEO4J_AUTH=neo4j/password \                    
 neo4j                                                                             
```

```
docker run -d --name neo4j01 -p 7474:7474 -p 7687:7687 -v /home/neo4j/data:/data -v /home/neo4j/logs:/logs -v /home/neo4j/conf:/var/lib/neo4j/conf -v /home/neo4j/import:/var/lib/neo4j/import --env NEO4J_AUTH=neo4j/123456 neo4j
```



**端口被占用时候查看进程并关闭**

```shell
netstat -tanlp  
kill pid              
```



**更改默认配置**

进入容器配置目录挂载在宿主机的对应目录**/home/neo4j/conf**（vim neo4j.conf）

```
在文件配置末尾添加一行
dbms.connectors.default_listen_address=0.0.0.0   //指定连接器的默认监听ip为0.0.0.0，即允许任何ip连接到数据库
dbms.connector.bolt.listen_address=0.0.0.0:7687  //取消注释并把对bolt请求的监听“地址:端口”改为“0.0.0.0:7687”
dbms.connector.http.listen_address=0.0.0.0:7474  //取消注释并把对http请求的监听“地址:端口”改为“0.0.0.0:7474“
```

保存后退出，重启neo4j容器



**导入数据**

 **数据准备**
清空宿主机**data/databases/graph.db**文件夹,将结点文件node.csv和关系文件rel.csv拷贝到宿主机挂载目录**/home/neo4j/import**中

 **进入neo4j容器然后暂停**

```
docker exec -it neo4j01 /bin/bash
cd bin/
neo4j stop
```

**使用官方的Neo4j-import进行导入**(写对应的CSV文件名)

```
neo4j-admin import \
	--database=graph.db \	            //指定导入的数据库，没有会在data/databases下自动创建一个
	--nodes ./import/nodes.csv \	    //指定导入的节点文件位置
	--relationships ./import/rel.csv \  //指定导入的关系文件位置
	--skip-duplicate-nodes=true \	    //设置重复节点自动过滤
	--skip-bad-relationships=true 	    //设置bad关系自动过滤
```

```
neo4j-admin import --database=graph.db --nodes ./import/nodes.csv --relationships ./import/rel.csv --skip-duplicate-nodes=true --skip-bad-relationships=true
```



**重启neo4j容器**

```
docker restart neo4j01
```



**创建节点和关系**

```
load csv with headers from "file:/var/lib/neo4j/import/api1.csv" as line
create(api1:api1{serviceName:line.serviceName, selfLink:line.selfLink,clusterIP:line.clusterIP,port:line.port,protocol:line.protocol})
```

```
load csv with headers from "file:/var/lib/neo4j/import/api2.csv" as line
create(api2:api2{apiName:line.apiName,serviceName:line.serviceName, url:line.url,method:line.method,describe:line.describe})
```

