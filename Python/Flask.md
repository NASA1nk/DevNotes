# Flask

**web框架**

- 可以**不用关心底层的请求响应处理**
- 只保留了web开发的核心功能，其他均由**外部扩展**实现

**虚拟环境**

- 隔离的python解释器环境
- 不同的项目会依赖不同的python版本和不同版本的库
- 可以方便区分和记录每个项目的依赖

## 程序实例

`pip install flask`

- 程序实例`app`由`Flask`类的构造方法生成
- `Flask`类构造方法的**第一个参数是模块或包的名称**，使用特殊变量`__name__`
  - python会根据**所处模块**来赋予`__name__`变量对应的值

- 可以直接在程序实例`app`上调用`Flask`类的属性和方法
  - 比如存储程序名称的属性：`app.name`

```python
# app.py

# 从flask包中导入Flask类
from flask import Flask

# 初始化Flask应用
# 实例化Flask类，得到程序实例app
app = Flask(__name__)
```

## 注册路由

客户端和服务器上的Flask程序的交互

1. 用户在浏览器中输入URL访问某一个资源
2. Flask接收用户请求并解析请求URL
3. **Flask为这个请求URL找到对应的处理函数**
4. 执行函数生成响应，返回给浏览器
5. **浏览器接收响应并解析**，将信息显示在页面中

Flask**使用WSGI将HTTP格式的请求转换为Flask程序能够使用的python数据**

Flask的**响应也会经过WSGI转换生成HTTP响应**

> 请求-响应循环：Request-Response Cycle
>
> 客户端（Client Side）是提供给用户的与服务器通信的软件，一般指web浏览器

### route

路由负责管理**URL和函数之间的映射**，函数被称为**视图函数**（View）

- 需要建立对应的处理函数，并为其定义URL规则

- 为处理函数附加上`app.route()`**装饰器**，并传入URL规则作为参数

### URL规则

- `route()`装饰器的**第一参数是URL规则**，用字符串表示
- 相对URL，必须以`/`开始，对应的是根地址
- **一个试图函数可以绑定多个URL**

**动态URL**

可以在URL规则中添加变量部分，表示为`<变量名>`

- 处理请求时会把变量传入视图函数
- 可以通过参数获取这个变量值
- 可以给变量设置默认值
  - 避免匹配失败返回404
  - 使用`defaults`参数设置，接受字典输入

```python
# app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return <h1>hello</h1>

@app.route('/he')
@app.route('/hw')
def index():
    return <h1>hellohhh</h1>

@app.route('/user/<name>')
def user():
    return <h1>hello，%s</h1> %name

@app.route('/user',defaults={'name',"ink"})
@app.route('/user/<name>')
def user():
    return <h1>hello，%s</h1> %name
```

## 开发服务器

**Flask内置了一个开发服务器**

- Flask通过click依赖包内置了一个命令行交互（Command Line Interface，CLI）系统
- 安装`flask`后，会自动添加一个Flask命令脚本，可以通过`flask`命令执行内置命令，扩展命令以及自定义命令

`flask run`

- 启动内置服务器
- 默认监听：`127.0.0.1:5000`

### 自动发现

一般在执行`flask run`命令前，需要提供**程序实例所在模块的位置**，**Flask会自动探测程序实例，自动探测规则**

- 从**当前目录**寻找`app.py`模块和`wsgi.py`模块，并从中寻找名为`app`或`application`的程序实例
- 从环境变量`FLASK_APP`对应的**模块名/导入路径**寻找名为`app`或`application`的程序实例
  - 如果程序主模块不叫`app.py`，则需要设置环境变量`FLASK_APP`
    - linux：`export FLASK_APP = server`
    - window：`set FLASK_APP = server`
- 如果安装了`python-dotenv`，那么在使用`flask run`命令时会自动从`.flaskenv`和`.env`文件中加载环境变量
  - 因为普通的环境变量在新创建命令行窗口或重启后就消失了
  - `.flaskenv`文件存储公开的环境变量，如`FLASK_APP`
  - `.env`文件存储私有的环境变量，如邮箱账户密码
  - 环境变量以键值对的形式定义，每行一个

### 外部可见

默认启动的web服务器是对外不可见的，使用`host`参数将主机地址设为`0.0.0.0`使其对外可见（**让服务器监听所有外部请求**）

> 个人计算机一般是没有公网IP的，所以只能被局域网的其他用户通过内网IP访问

```python
flask run --host=0.0.0.0
```

### 改变端口

默认启动的web服务器会监听来自5000端口的请求，使用`port`参数修改监听的端口

```python
flask run --port=9000
```



## 项目配置

配置变量

- Flask中配置变量就是一些**大写形式**的python变量，又叫**配置参数**或**配置键**
- 配置变量通过Flask对应的`app.config`属性作为统一的接口来设置和获取，它指向的`Config`类实际上是字典的子类
  - 也可以使用`update()`方法来一次加载多个值
  - 也可以将配置变量存储在单独的python脚本，json文件或python文件中，再批量导入

```python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 邮件服务器配置
# 配置名称必须全大写
app.config["MAIL_SERVER"] = "smtp.163.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

# 实例化发邮件对象
mail = Mail(app)


app.config.update(
    MAIL_SERVER = "smtp.163.com",
    MAIL_PORT= 465,
    MAIL_USE_TLS = False
)
```



# 请求和响应

## HTTP请求

请求url：协议/域名（ip:port）/资源路径

请求报文

- 报文首部
  - 请求行：方法，url，协议
  - 首部字段
- CRLF
- 报文体（payload）

### Request对象

Flask的请求对象`request`**封装了从客户端发过来的请求报文**

> 实际上封装大部分由Werkzeug完成，Flask子类化Werkzeug的请求和响应

`request`对象的常用属性和方法

- `query_string`：获取未解析的原生查询字符串
- `args`：存储解析后的查询字符串，通过字典方式来获取键值
- `cookies`：包含所有随请求提交的cookie的字典
- `get_data(cache=True,as_text=False,parse_form_data=False)`：返回字符串格式的请求数据
  - `cache`设置是否缓存解析过的数据以供后续调用，因为解析表单数据的函数不缓存解析结果
  - `as_text`设置返回值是解码后的unicode字符串，默认读取是**字节字符串**
- `get_json(self,force=False,silent=False,cache=True)`：作为json解析并返回数据，如果MIME的类型不是json，则返回None（除非`force`设为True）
- `files`：包含所有上传的文件，可以用字典的形式获取文件
  - 文件名为`<input>`标签中的`name`属性值
  - 可以调用`save()`方法并传入保存的路径来保存文件
- `form`：和files类似，包含解析后的表单数据
  - 表单字段值为`<input>`标签中的`name`属性值

> 不要使用键索引获取数据，如果没有对应的键会返回400错误，要使用`get`方法

### 处理请求

#### 路由匹配

- 程序实例app中存储了一个路由表（`app.url_map`），其中存储了url规则和视图函数的映射关系
- 当获取到请求时，flask应用会根据请求报文中的url来和表中的所有url进行匹配

```bash
# 获取url解析
flask routes
```

### 请求钩子

`Hook`

- 有时候需要对请求进行预处理（preprocessing）和后处理（postprocessing），这时候就可以使用flask提供的请求钩子
- hook可以用来注册在请求处理的不同阶段执行的处理函数（callback，回调函数）
- hook使用装饰器实现，通过程序实例`app`调用

请求钩子函数

- before_first_request
- before_request
- after_request
- teardown_request
- after_this_request

## HTTP响应

### 响应报文

HTTP响应中数据可以通过多种格式传输，不同的响应数据格式需要设置不同的`MIME`类型，`MIME`类型在响应报文首部的`Content-Type`字段中定义，**Flask中默认是HTML格式**

- `Contene-Type：text/html; charset=utf-8`

> MIME类型是一种**标识文件类型的机制**，又叫media type或content type
>
> - 可以让客户端区分不同的内容类型，执行不同的操作
> - 一般格式为：**类型名/子类型名**，子类型名一般为**文件扩展名**

请求报文

- 报文首部
  - 状态行：协议，状态，原因
  - 首部字段
- CRLF
- 报文体（响应内容）

Flask提供`make_response()`方法**生成响应对象**，传入响应的主体作为参数，使用响应对象的`mimetype`属性设置`MIME`类型

```python
# -*- coding: utf-8 -*-
from flask import Flask,make_response

app = Flask(__name__)

@app.route('/foo')
def foo():
    response = make_respons('hello world')
    # 纯文本
    response.mimetype = 'text/plain'
    # json
    response.mimetype = 'application/json'
    return response
```

### json序列化

Flask引入python标准库中的`json`模块，可以直接从Flask中导入`json`对象（`from flask import json`）

- 调用`dumps()`方法将字典，列表和元组序列化为`json`字符串
- 然后修改`MIME`类型即可返回`json`响应

**Flask封装了这些方法**，提供一个更方便的`jsonify()`函数

- 只需要传入数据或参数，它就会对传入的参数序列化，转换成`json`字符串作为响应主体，**然后生成一个响应对象**（会修改正确的mime类型）
- `jsonify()`函数默认生成`200`响应，可以通过附加状态码来修改

```python
# -*- coding: utf-8 -*-

# jsonify()
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/foo')
def foo():
    return jsonify(name='ink',gender='male')

@app.route('/bar')
def bar():
    return jsonify(name='ink',gender='male'), 20000

# 原始方法
from flask import Flask,json

app = Flask(__name__)

@app.route('/foo')
def foo():
    data = {
        'name':'ink',
        'gender':'male'
    }
    # 序列化，serialize
    response = make_response(json.dumps(data))
    # json
    response.mimetype = 'application/json'
    return response
```

### 重定向

- **状态码为302的重定向的响应主体为空**，响应首部将`Location`字段设置为重定向的目标url
- 浏览器在接收到重定向响应后会向这个目标url发起请求

### 错误响应

`abort()`函数：传入相应的错误状态码

## Cookie

HTTP是无状态（stateless）协议，在一次请求响应结束后，服务器不会留下任何对方状态的信息

cookie通过**在请求和响应报文中添加cookie数据来保存客户端的状态信息**（主要存储用户的认证信息）

- cookie数据是**保存在客户端浏览器中**的小型文本数据
- 浏览器会保存一定时间，并在向同一个服务器发送请求时附带cookie数据

Flask中使用`Response`类提供的`set_cookie()`方法来添加生成cookie

- cookie可以通过请求对象的cookies属性和获取：`request.cookies.get()`

## Session

session对象一般用于对cookie加密

# 项目结构

## 蓝本模块

将视图函数升级为blueprints子包

- **使用蓝本可以将程序模块化**，目的是将程序的某一部分的操作集中在一起

  - 蓝本实例和一系列注册在蓝本实例上的操作的集合被成为一个蓝本

  - 蓝本只有将它注册到程序实例上后，才能发挥作用

- 因此一般将程序按照不同的功能分成不同的组件，用蓝本来组织这些组件

- **一个程序实例可以注册多个蓝本**，蓝本不仅仅是在代码层面上组织程序，还可以在程序层面定义属性

  - 具体形式是蓝本下的**所有路由设置不同的url前缀或子域名**

### 创建蓝本

Flask提供的`Blueprint`类可以创建一个蓝本实例

- 蓝本实例可以跟程序实例一样注册路由，请求处理函数...
- 蓝本实例也有一个`route()`装饰器

`auth.py`

```python
from flask import Blueprint

# 蓝本实例，Blueprint（蓝本名称，包或模块的名称）
auth_bp = Blueprint('auth', __name__)
```

### 装配蓝本

蓝本中的视图函数通过蓝本实例提供的`route()`装饰器注册

`auth.py`

```python
from flask import Blueprint

# 蓝本实例，Blueprint（蓝本名称，包或模块的名称）
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/hi')
def hi():
    pass

@auth_bp.route('/hello')
def hello():
    pass
```

### 注册蓝本

使用Flask的`register_blueprint()`方法将蓝本实例注册到程序实例上

`app.py`

```python
from flask import Blueprint
from auth impot auth_bp

# 传入参数必须是蓝本对象
app.register_blueprint(auth_bp)

# 可以额外传入url_prefix参数来为蓝本下所有视图url附加url前缀
app.register_blueprint(auth_bp, url_prefix='/auth')
```

### 蓝本端点

端点是url规则和视图函数的中间媒介：`url -> endpoint -> view func`

默认情况下，端点是视图函数的名称，但是在使用蓝本后，蓝本的视图函数对应的端点名称变成了`蓝本对象名·视图函数名`，**即端点实现了蓝本的视图函数命名空间**

- 这样不同的蓝本中就可以定义同名的视图函数，解决了视图函数重名问题
- 如果要使用`url_for()`函数，就要明确端点的蓝本值



## 类组织配置

