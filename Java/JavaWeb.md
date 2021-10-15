# JavaWeb

- web即网页
- 在Java中，动态web资源开发的技术统称为JavaWeb

## Web开发

- 静态web

  - html,css
  - 提供给用户查看的数据不会发生变化
- 动态web

  - 提供给用户查看的数据会发送变化（如淘宝）
- 技术栈
- Servlet
- JSP
- B/S架构
  - 基于Java语言，本质是Servlet
- 支持高并发，高可用，高性能
- PHP
  - 作为开发速度很快，功能很强大，跨平台
  - 无法承载大访问量的情况

## web应用程序

Web应用程序

- 可以提供浏览器访问的应用程序

web资源

- 如index.html，home.html等web资源，这些web资源可以被外界访问，对外界提供服务

- 我们通过URL访问到的任何一个页面或者资源，都是存在于这个世界的某一个角落的一台计算机上（服务器）
- 这些统一的web资源会被放在服务器的同一个文件夹下，即是一个web应用程序

一个web应用由多部分组成（静态web，动态web)

- html,css,js
- jsp,servlet
- Java程序
- jar包

- 配置文件Properties

Web应用程序编写完成后，要想提供给外界访问，需要一个服务器来统一管理



## 静态web

静态web资源请求

![静态web资源请求](JavaWeb.assets/静态web资源请求.png)

缺点

- Web页面无法动态更新，所有用户看到都是同一个页面
  - JavaScript实现的轮播图和点击特效等都是伪动态
- 无法和数据库交互
  - 数据无法持久化，用户无法交互

## 动态Web

浏览器发送HTTP请求，Tomcat服务器接收请求，Servlet容器从磁盘加载静态资源，Servlet程序处理请求request ，处理结束返回response

![动态Web资源请求](JavaWeb.assets/动态Web资源请求.png)

缺点

- 服务器的动态Web资源出现错误，需要重新编写后端程序，重新发布



# Tomcat

- 轻量级应用服务器
- 开源的servlet容器
- 支持JSP动态页面，也可以处理html。但是处理html的效率不如Apache，所以想处理html静态网页还是用Apache最合适
- Apache是web服务器，Tomcat是应用服务器，它只是一个servlet容器，是Apache的扩展
- Apache和Tomcat都可以做为独立的web服务器来运行，但是Apache不能解释java程序（jsp，servlet）

B/S

- 使用tomcat作为服务器

- 客户端使用浏览器

> 上面的实现是C/S

## 安装

**下载**

- [Apache Tomcat® - Apache Tomcat 10 Software Downloads](https://tomcat.apache.org/download-10.cgi)

**配置**

分别打开`bin`目录中的`startup.bat`和`shutdown.bat`两个文件

- 在第一行`@echo off`的下面一行加上一行`SET JAVA_HOME=C:\Env\JDK17`

或者在系统的环境变量中添加`JAVA_HOME`，值为`C:\Env\JDK17`

> `.bat`是windows下的执行文件，`.sh`是linux下的执行文件

**启动**

- 进入`bin`目录，启动`startup.bat`文件


> `startup.bat`文件用于打开tomcat，`shutdown.bat`文件用于关闭tomcat

![tomcat界面](JavaWeb.assets/tomcat界面.png)

## 配置文件

核心配置文件是`conf`目录下的`server.xml`文件

修改默认启动端口号

- `conf`目录下的`server.xml`文件

- 确保服务器安全组中开放了这个端口，设置完保存然后重启下tomcat即可

```xml
<Connector port="8080" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />
```

点击Manager App的时候，会要求输入用户名和密码

- `conf`目录下的`tomcat-users.xml`

```xml

```

配置主机名称

- 默认的主机名为：`localhost`（即127.0.0.1）
- 默认应用存放的位置为：`webapps`

> 修改host name后需要在主机的`C:\Windows\System32\drivers\etc\hosts`文件中添加对应的映射，否则找不到ip
>
> 修改完后在命令行输入`ipconfig /flushdns`刷新dns缓存

```xml
<Host name="localhost"  appBase="webapps"
      unpackWARs="true" autoDeploy="true">
```

日志配置

- `conf`目录下的`logging.properties`
- 默认是UTF-8，windows需要修改为GBK

```properties
java.util.logging.ConsoleHandler.level = FINE
java.util.logging.ConsoleHandler.formatter = org.apache.juli.OneLineFormatter
java.util.logging.ConsoleHandler.encoding = GBK
```





## 目录结构

- `bin`：存放启动和关闭tomcat脚本 
- `conf`：包含不同的配置文件
  - `server.xml`（tomcat的主要配置文件）和`web.xml` 
- `work`：存放jsp编译后产生的`class`文件 
- `webapp`：存放应用程序（网站）
  - 要部署的应用程序要存放到此目录 
- `logs`：存放日志文件 
- `lib`：主要存放tomcat依赖的jar包

## 部署项目

tomcat的`webapps`目录下的5个默认的应用

 ![tomcat应用](JavaWeb.assets/tomcat应用.png)

### Web应用结构

- `http://localhost:8080/`默认访问的是tomcat的`/webapps/ROOT/`目录下的`index.jsp`文件
- 将自己的应用放在tomcat服务器的`webapps`目录下即可
  - 需要有`WEB-INF\web.xml`网站配置文件

- 访问http://localhost:8080/inkapp即可访问到`index.html`

```txt
--webapps  ：tomcat服务器的web目录
	-ROOT
	-inkapp  ：网站的目录名
		- WEB-INF
			-classes  : java程序
			-lib  ：web应用所依赖的jar包
			-web.xml  ：网站配置文件
		- index.html  ：默认首页
		- static 
            -css
            	-style.css
            -js
            -img
         -.....
```

> **访问域名**
>
> 1. 在浏览器输入一个域名，回车
> 2. 查看本机的`C:\Windows\System32\drivers\etc\hosts`配置文件是否有相应域名的映射
>    1. 若有，直接映射到对应的IP地址，进行访问
>    2. 若无，则去DNS服务器上查找对应的IP，找到就返回相应的IP并进行访问，找不到就不返回



# HTTP

超文本传输协议

- 请求响应协议
- 运行在TCP上
- 端口：80

> 超文本：图片，音乐，视频，定位，地图......

## 版本

HTTP/1.0

- 客户端与Web服务器一次连接只能获取一个Web资源，然后就会断开连接
  - 如果某个页面有多个图片资源需要加载，那么需要连接多次，影响服务器和客户端的性能

HTTP/1.1

- 客户端可以与web服务器一次连接后可以获取多个web资源

## HTTP请求

客户端 -> 发送请求（request） -> 服务器

### 请求行

```http
Request URL:https://www.baidu.com/  
Request Method:GET    
Status Code:200 OK    
Remote Address:14.215.177.39:443=
```

- 请求方式：`GET`，`POST`，HEAD，DELETE，PUT，TRACT…
  - `GET`
    - 一次请求能够携带的参数比较少
    - 大小有限制
    - 会在浏览器的URL地址栏显示数据内容，高效，不安全
  - `POST`
    - 一次请求能够携带的参数没有限制
    - 大小没有限制
    - 不会在浏览器的URL地址栏显示数据内容，安全，不高效

### 消息头

- `Accept`：支持的数据类型
- `Accept-Encoding`：支持的编码格式（GBK，UTF-8）
- `Accept-Language`：语言环境
- `Cache-Control`：缓存控制
- `Connection`：请求完成是断开还是保持连接
- `HOST`：主机



## HTTP响应

服务器 -> 响应（response）-> 客户端

### 响应状态码

- `200`：请求响应成功
- `3xx`：请求重定向
- `4xx`：找不到资源
  - `404` 
- `5xx`：服务器错误
  - `500`
  - `502`



# Maven

项目架构管理工具

- 在JavaWeb开发中需要使用大量的jar包，手动导入太复杂，需要有一个工具自动导入和配置jar包

**核心思想**：约定大于配置

- 有约束不要去违反
- Maven会规定好如何去编写Java代码，必须要按照这个规范

