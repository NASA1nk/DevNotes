

# Neo4j

## 服务器

- 账号：neo4j

- 密码：123456

## 数据路径

数据库存储文件

- `/var/lib/neo4j/data/databases/graph.db`



## 导入数据

**CSV文件**

- 逗号分隔值的文件
- neo4j是UTF-8编码，CSV文件默认保存是ANSI编码，需要用记事本另存为成UTF-8

`LOAD CSV`

- 导入到`/var/lib/neo4j/import`路径下
- 将指定路径下的CSV文件读取出来，其中`FileUrl`是文件地址，可以是本地文件路径也可以是网址
  - 必须设置权限，以便外部源可以读取该文件
- `WITH HEADERS`：在导入CSV文件时附带上头部，**从文件中读取第一行作为参数名**
  - 只有使用该参数后才可以使用`line.name`这样的表示方式，否则需要使用`{movieId:line[0],name1:line[1],year:line[2],tag:line[3]}`的表示方式
- 每个节点的属性由导入的CSV文件的每行指定
- CSV文件的所有数据都读取为**字符串**
  - 需要使用`toInteger()`，`toFloat()`，`split()`来转换

```bash
LOAD CSV WITH HEADERS FROM “file://FileUrl” AS line
```

**导入节点文件创建节点**

```
load csv with headers from "file:/var/lib/neo4j/import/entity.csv" as line
create(entity:entity{id:line.id, name:line.name})
```

```
load csv with headers from "file:/var/lib/neo4j/import/trainticket.csv" as line
create(ticket:ticket{id:line.id,uri:line.URI,method:line.HttpMethod,description:line.Description})
```

**导入关系创建关**

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



## neo4j容器

### 数据挂载

建立四个基本的文件夹用于**挂载容器目录**

- `data`：数据存放的文件目录
- `logs`：运行的日志文件目录
- `conf`：数据库配置文件目录
  - 在配置文件`neo4j.conf`中配置开放远程连接、设置默认激活的数据库）

- `import`：批量导入csv文件的目录
  - 节点文件`node.csv`和关系文件`rel.csv`需要放到这个文件夹下


### 官方文档

- which allows you to access neo4j through your browser at [http://localhost:7474](http://localhost:7474/).This binds two ports (`7474` and `7687`) for HTTP and Bolt access to the Neo4j API. 
  - 默认的neo4j url，开放2个端口
- A volume is bound to `/data` to allow the database to be persisted outside the container.
  - 可以将`data`挂载出来持久化存储
- By default, this requires you to login with `neo4j/neo4j` and change the password. 
  - 默认的账号和密码都是neo4j
- You can, for development purposes, disable authentication by passing `--env=NEO4J_AUTH=none` to docker run.

  - `--env=NEO4J_AUTH=neo4j/123456`：指定neo4j的用户名和密码
  - `--env=NEO4J_AUTH=none`：不设置密码

### 运行neo4j容器

```bash
docker run -d --name inkneo4j \        
 -p 7474:7474 -p 7687:7687 \                                         
 -v /home/neo4j/data:/data \                                      
 -v /home/neo4j/logs:/logs \                                        
 -v /home/neo4j/conf:/var/lib/neo4j/conf \              
 -v /home/neo4j/import:/var/lib/neo4j/import \     
 --env NEO4J_AUTH=neo4j/123456 \                    
 neo4j                                                                            
```

### 更改默认配置

进入挂载在宿主机的配置目录`/home/neo4j/conf`，修改配置后重启neo4j容器

```bash
vim neo4j.conf
# 在文件配置末尾添加一行
dbms.connectors.default_listen_address=0.0.0.0   # 指定连接器的默认监听ip为0.0.0.0，即允许任何ip连接到数据库
dbms.connector.bolt.listen_address=0.0.0.0:7687  # 取消注释并把对bolt请求的监听“地址:端口”改为“0.0.0.0:7687”
dbms.connector.http.listen_address=0.0.0.0:7474  # 取消注释并把对http请求的监听“地址:端口”改为“0.0.0.0:7474“
```

### 导入数据

**数据准备**

- 清空宿主机的`data/databases/graph.db`文件夹
- 将结点文件`node.csv`和关系文件`rel.csv`拷贝到挂载目录`/home/neo4j/import`中

**进入neo4j容器然后暂停**

```bash
docker exec -it neo4j01 /bin/bash
cd bin/
neo4j stop
```

**使用官方的Neo4j-import进行导入**，然后重启容器

```bash
neo4j-admin import \
	--database=graph.db \	            # 指定导入的数据库，没有会在data/databases下自动创建一个
	--nodes ./import/nodes.csv \	    # 指定导入的节点文件位置
	--relationships ./import/rel.csv \  # 指定导入的关系文件位置
	--skip-duplicate-nodes=true \	    # 设置重复节点自动过滤
	--skip-bad-relationships=true 	    # 设置bad关系自动过滤
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

