# Nginx

反向代理器和负载均衡器

# 虚拟主机

在有nginx服务的机器中做虚拟主机技术主要应用于HTTP服务

将一台服务器的某项或者全部服务内容逻辑**划分为多个服务单位**，**对外表现为多个服务器**，从而充分利用服务器硬件资源

```bash
cd  /usr/local/lnmp/nginx/conf
 ##设置虚拟服务器##在大括号里面加
vim nginx.conf  
server{
       listen 80;
       server_name localhost;
       location / {
          root  /usr/share/nginx/html;
          index  index.html;
    }
}
}
```

# 配置

- 主配置文件：`/usr/local/nginx/conf/nginx.conf`
- 通过`nginx -c`可以指定要读取的配置文件来启动

## web服务器

**nginx作为web服务器时使用的配置**

**http{}段配置的参数**

- http{}段：由`ngx_http_core_module`模块引入
- http配置主要包含四个区块

    ```nginx
    http {            			## 协议级别
     include mime.types;
     default_type application/octet-stream;
     keepalive_timeout 65;
     gzip on;
     sendfile on;				## 指定nginx是否调用sendfile函数（zero copy）来输出文件，对于普通应用必须设为on，如果用来进行下载等应用磁盘I/O重负载应用，可设置为OFF，以平衡磁盘与网络I/O处理速度，降低系统的uptime
     autoindex on;				## 开启目录列表访问，适合下载服务器，默认关闭
        upstream {              ## 负载均衡配置
        ...
        }
        server {             	## 服务器级别，每一个server类似于httpd中的一个<VirtualHost,通俗来说就是一个网站>
            listen80;
            server_name localhost;
            location / {        ##请求级别，类似与httpd中的<Location>，用于定义URL与本地文件系统的映射关系
                root html;
                index index.html index.htm;
            }
        }
    }
    ```

### http{}段配置指令

`server{}`：定义一个**虚拟主机**

- `listen`：指定监听的地址和端口
  - `listen ADDRESS[:PORT];`
  - `listen PORT;`
- `server_name NAME1 [NAME2...];`：后面可以跟多个主机，名称可以用正则表达式或通配符。当有多个server时，匹配顺序如下
  - 先做精确匹配检查
  - 左侧通配符匹配检查，如`*.idfsoft.com`
  - 右侧通配符匹配检查，如`mail.*`
  - 正则表达式匹配检查，如`~ ^.*\.idfsoft\.com$`
  - `default_server`

```nginx
server {
 	listen 80;
 	server_name www.idfsoft.com;
 	root "/vhosts/web";
}
```

`location{}`：通过指定模式来**与客户端请求的URI相匹配**

- 允许根据用户请求的URI来**匹配定义的各个location**
- 匹配到时，**此请求将被响应的location配置块中的配置所处理**

**语法**：`location [修饰符] pattern {…}`

| 修饰符 | 功能                                                         |
| ------ | ------------------------------------------------------------ |
| =      | 精确匹配                                                     |
| ~      | 正则表达式模式匹配，区分大小写                               |
| ~*     | 正则表达式模式匹配，不区分大小写                             |
| ^~     | 前缀匹配，类似于无修饰符的行为，也是以指定模块开始。不同的是，如果模式匹配，那么就停止搜索其他模式了，不支持正则表达式 |
| @      | 定义命名location区段，这些区段客户端不能访问，只可以有内部产生的请求访问，如try_files或error_page等 |

**优先级**：查找顺序和优先级由高到底依次为

- 带有`=`的精确匹配优先
- 正则表达式
- 没有修饰符的精确匹配

> 有多个正则表达式出现时，按照它们在配置文件中定义的顺序

```nginx
# 没有修饰符:表示必须以指定模式开始
# 可以匹配
# www.baibai.com/abc
# www.baibai.com/abc/
# www.baibai.com/abc?.…
server {
 	server_name www.baibai.com;
 	location /abc {               
 	......
 	}
}

# =修饰符表示必须与指定的模式精确匹配
# 可以匹配
# www.baibai.com/abc
# www.baibai.com/abc?.…
# 不可以匹配
# www.baibai.com/abc/
# www.baibai.com/abc/adcde
server {
 	server_name www.baibai.com;
 	location = /abc {
 	......
 	}
}
```

**访问控制**

用于`location`段，可以用主机地址表示，**也可用网段表示**，必须一起用

- `allow`：设定允许哪台或哪些主机访问，多个参数间用空格隔开
- `deny`：设定禁止哪台或哪些主机访问，多个参数间用空格隔开

```nginx
location / {
    root   html;
    index  index.php index.html index.htm;
    allow  192.168.91.129/32;     # /32表示一个网段
    deny   all;
}
```



# Docker部署

nginx镜像中的**默认配置**

- 日志位置：`/var/log/nginx/`

  - `access.log`
  - `error.log`

- 配置文件：`/etc/nginx/nginx.conf`，`/etc/nginx/conf.d/default.conf`

- 文件位置：`/usr/share/nginx/html`

  - `index.html`
  - `50x.html`

  > nginx静态目录，不用修改，不用挂载

```bash
# 必须后台启动 -d
docker run -d -p 1010:80 --name inknginx nginx
```

挂载配置文件

- 将打包好的前端目录`dist`直接放到对应的copfront.admin文件夹内

```bash
docker run --name inknginx -p 1010:80 -d -v /home/dog/yinke/nginx/nginx.conf:/etc/nginx/nginx.conf -v /home/dog/yinke/nginx/logs:/var/log/nginx -v /home/dog/yinke/nginx/dist/:/usr/share/html/frontend/ nginxcd d
```

