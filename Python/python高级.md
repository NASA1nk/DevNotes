# 函数式编程

**函数式编程就是一种抽象程度很高的编程范式**

- 函数式编程的一个特点就是**允许把函数本身作为参数传入另一个函数，还允许返回一个函数**

> 纯粹的函数式编程语言编写的函数**没有变量**，因此任意一个函数只要输入是确定的，输出就是确定的，**这种纯函数称之为没有副作用**
>
> python对函数式编程提供部分支持，因为python允许使用变量，因此python不是纯函数式编程语言

## 闭包

`Closure`

**函数嵌套**：在一个函数中定义了另一个函数，外部函数称为enclosing function，内部函数称为enclosed function或者nested function

闭包是词法闭包`Lexical Closure`的简称，**是指引用了自由变量的函数**，这个**被引用的自由变量将和这个函数一同存在**，即使已经离开了创造它的环境 

- 外部函数**返回的内部函数在其定义内部引用了外部函数的局部变量**，闭包使得局部变量在函数外被访问成为可能
  - **即enclosed function中直接使用了enclosing funcion中的参数**
- 因为返回的函数不会立刻执行，所以**返回函数不要引用任何循环变量或者后续会发生变化的变量**，否则最后执行时使用的变量已经被改变

```python
def count():
    fs = []
    for i in range(1, 4):
        # 每次循环，都创建了一个新的函数
        def f():		
             # 使用了外部变量i
             return i*i		
        fs.append(f)		
    return fs				

# 返回的函数引用了变量i，但它并非立刻执行,等到3个函数都返回时,变量i已经变成了3,所以都是9
f1, f2, f3 = count()		

# 9
f1()					
# 9							
f2()					
# 9
f3()							
```

如果要引用循环变量，就要再创建一个函数

- **用该函数的参数绑定循环变量当前值，无论该循环变量后续如何更改，已绑定到函数参数的值不变**

```python
def count():
    # 用参数j绑定循环变量i
    def f(j):				
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        # f(i)立刻执行，因此i的当前值被传入f()
        fs.append(f(i)) 	
    return fs

f1, f2, f3 = count()
# 1
f1()

# 4
f2()

# 9
f3()
```



## 装饰器

`Decorator`

- 在代码运行期间**动态增加功能的方式称之为装饰器**
- `Decorator`本质上是一个返回函数的高阶函数

### 工作机制

其实最开始的时候就是抽取出公共的逻辑，封装成一个函数，然后**在内部调用这个函数**

- 更pythonic的写法就可以用到装饰器

装饰器则是把需要内部调用装饰器对应方法的方法作为接受的参数，将其包在里面（在内部调用这个方法），并获取到传给这个方法的参数，对其做额外的逻辑处理

> 闭包：内部函数warpper就掉用了外部函数wrap_decorator的参赛func（虽然是个函数，但也是参数）

```python
# 装饰器，方法通过@wrap_decorator使用
def wrap_decorator(func):
  # 嵌套调用，(*args, **kwargs)可以接受任意参数
  def warpper(*args, **kwargs):
    
    # 公共逻辑处理，如打印日志...
    
    # 执行装饰器修饰的目标函数
    func(*args, **kwargs)
  # 返回内部函数
  return warpper
    
@wrap_decorator
my_func(1,2,3,4)

# 等价于
warp_decorator(my_func(1,2,3,4))
```

### 函数名重写

在内部调用func时，会重写其函数名`func.__name__`，通过调用functools.wraps解决

```python
from functools import warpss

# 装饰器，方法通过@wrap_decorator使用
def wrap_decorator(func):
  # 嵌套调用，(*args, **kwargs)可以接受任意参数
  @wraps(func)
  def warpper(*args, **kwargs):
    
    # 公共逻辑处理，如打印日志...
    
    # 执行装饰器修饰的目标函数
    func(*args, **kwargs)
  # 返回内部函数
  return warpper
    
@wrap_decorator
my_func(1,2,3,4)

# 等价于
warp_decorator(my_func(1,2,3,4))
```



# 日志

`logging`

- python自身提供的用于记录日志的标准库模块

logging模块默认定义了以下几个日志等级，它允许开发人员自定义其他日志级别

- 开发应用程序或部署开发环境时，可以使用`DEBUG`或`INFO`级别的日志获取尽可能详细的日志信息来进行开发或部署调试
- 应用上线或部署生产环境时，应该使用`WARNING`或`ERROR`或`CRITICAL`级别的日志来降低机器的I/O压力和提高获取错误日志信息的效率
  - 日志级别的指定通常都是在应用程序的配置文件中进行指定的
- 列表中的日志等级是从上到下依次升高的，即`DEBUG < INFO < WARNING < ERROR < CRITICAL`，而日志的信息量是依次减少的
- 当为某个应用程序指定一个日志级别后，**应用程序会记录所有日志级别大于或等于指定日志级别的日志信息**，而不是仅仅记录指定级别的日志信息
- `logging`模块也可以指定日志记录器的日志级别，只有级别大于或等于该指定日志级别的日志记录才会被输出，小于该等级的日志记录将会被丢弃

| 日志等级（level） | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| DEBUG             | 最详细的日志信息，典型应用场景是问题诊断                     |
| INFO              | 信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照预期的那样进行工作 |
| WARNING           | 当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的 |
| ERROR             | 由于一个更严重的问题导致某些功能不能正常运行时记录的信息     |
| CRITICAL          | 当发生严重错误，导致应用程序不能继续运行时记录的信息         |

## 日志配置

### 默认配置

- 当没有提供任何配置信息的时候，日志记录函数都会去调用`logging.basicConfig(**kwargs)`方法，且不会向该方法传递任何参数

- 每行日志记录的各个字段含义分别是：**日志级别:日志器名称:日志内容**
  - 这种格式是因为`logging`模块提供的日志记录函数所使用的**日志器设置的日志格式默认**是`BASIC_FORMAT`，其值为`"%(levelname)s:%(name)s:%(message)s"`

- 在`logging`模块提供的日志记录函数所使用的**日志器设置的处理器所指定的日志输出位置默认**为
  `sys.stderr`

### 修改默认设置

- 调用上面这些日志记录函数之前，手动调用`basicConfig()`方法，把想设置的内容以参数的形式传递进去就可以了
  - `logging.basicConfig(**kwargs)`

- `logging.basicConfig()`是一个**一次性的简单配置工具**，也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作

```python
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
```

该函数可接收的关键字参数如下

| 参数名称 | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| filename | 指定日志输出目标文件的文件名，指定该设置项后日志信息就不会被输出到控制台了 |
| filemode | 指定日志文件的打开模式，默认为`'a'`。需要注意的是，该选项要在filename指定时才有效 |
| format   | 指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序，logging模块定义的格式字段下面会列出 |
| datefmt  | 指定日期/时间格式，需要注意的是，该选项要在`format`中包含时间字段`%(asctime)s`时才有效 |
| level    | 指定日志器的日志级别                                         |
| stream   | 指定日志输出目标`stream`，如`sys.stdout`、`sys.stderr`以及网络`stream`，需要说明的是，stream和filename不能同时提供，否则会引发 `ValueError`异常 |
| style    | Python 3.2中新添加的配置项，指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%' |
| handlers | Python 3.3中新添加的配置项，该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发`ValueError`异常 |

`logging`模块中定义好的可以用于`format`格式字符串中字段如下

| 字段/属性名称   | 使用格式            | 描述                                                         |
| --------------- | ------------------- | ------------------------------------------------------------ |
| asctime         | %(asctime)s         | 日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896 |
| created         | %(created)f         | 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值 |
| relativeCreated | %(relativeCreated)d | 日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的） |
| msecs           | %(msecs)d           | 日志事件发生事件的毫秒部分                                   |
| levelname       | %(levelname)s       | 该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'） |
| levelno         | %(levelno)s         | 该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）         |
| name            | %(name)s            | 所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger |
| message         | %(message)s         | 日志记录的文本内容，通过 `msg % args`计算得到的              |
| pathname        | %(pathname)s        | 调用日志记录函数的源码文件的全路径                           |
| filename        | %(filename)s        | pathname的文件名部分，包含文件后缀                           |
| module          | %(module)s          | filename的名称部分，不包含后缀                               |
| lineno          | %(lineno)d          | 调用日志记录函数的源代码所在的行号                           |
| funcName        | %(funcName)s        | 调用日志记录函数的函数名                                     |
| process         | %(process)d         | 进程ID                                                       |
| processName     | %(processName)s     | 进程名称，Python 3.1新增                                     |
| thread          | %(thread)d          | 线程ID                                                       |
| threadName      | %(thread)s          | 线程名称                                                     |

## 日志组件

logging日志模块的四大组件

> 日志器（logger）是入口，真正干活的是处理器（handler），处理器（handler）可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作

| 组件名称 | 对应类名  | 功能描述                                                     |
| -------- | --------- | ------------------------------------------------------------ |
| 日志器   | Logger    | 提供了应用程序可一直使用的接口                               |
| 处理器   | Handler   | 将logger创建的日志记录发送到合适的目的输出                   |
| 过滤器   | Filter    | 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录 |
| 格式器   | Formatter | 决定日志记录的最终输出格式                                   |

### Logger类

**创建Logger对象**

- 通过`Logger`类的实例化方法创建一个`Logger`类的实例
- 使用`logging.getLogger()`方法（推荐）
  - `logging.getLogger()`方法有一个可选参数`name`，该参数表示将要返回的**日志器的名称标识**，如果不提供该参数，则其值为`root`
  - 以相同的`name`参数值多次调用`getLogger()`方法，将会返回指向同一个`logger`对象的引用

`Logger`对象有3个任务

- 向应用程序暴露几个方法，使应用程序可以在运行时记录日志消息
- 基于日志严重等级（默认的过滤设施）或`filter`对象来决定要对哪些日志进行后续处理
- 将日志消息传送给所有感兴趣的`handlers`

`Logger`对象最常用的方法分为两类：**配置方法和消息发送方法**

常用的配置方法如下

| 方法                                          | 描述                                       |
| --------------------------------------------- | ------------------------------------------ |
| Logger.setLevel()                             | 设置日志器将会处理的日志消息的最低严重级别 |
| Logger.addHandler() 和 Logger.removeHandler() | 为该logger对象添加和移除一个handler对象    |
| Logger.addFilter() 和 Logger.removeFilter()   | 为该logger对象添加和移除一个filter对象     |

`logger`对象配置完成后，可以使用下面的方法来**创建日志记录**

- `Logger.exception()`与`Logger.error()`的区别在于：`Logger.exception()`将会输出堆栈追踪信息，另外通常只是在一个exception handler中调用该方法

| 方法                                                         | 描述                                              |
| ------------------------------------------------------------ | ------------------------------------------------- |
| Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical() | 创建一个与它们的方法名对应等级的日志记录          |
| Logger.exception()                                           | 创建一个类似于Logger.error()的日志消息            |
| Logger.log()                                                 | 需要获取一个明确的日志level参数来创建一个日志记录 |

### Handler类

`Handler`对象的作用是基于日志消息的level将消息分发到handler指定的位置（如文件、网络、邮件等）

`Logger`对象可以通过`addHandler(`)方法为自己添加0个或者更多个`handler`对象

**应用场景**：一个应用程序可能想要实现以下几个日志需求

- 把所有日志都发送到一个日志文件中
- 把所有严重级别大于等于error的日志发送到stdout
- 把所有严重级别为critical的日志发送到一个email邮件地址

这种场景就需要3个不同的`handlers`，每个`handler`负责发送一个特定严重级别的日志到一个特定的位置

**配置方法**

| 方法                                          | 描述                                        |
| --------------------------------------------- | ------------------------------------------- |
| Handler.setLevel()                            | 设置handler将会处理的日志消息的最低严重级别 |
| Handler.setFormatter()                        | 为handler设置一个格式器对象                 |
| Handler.addFilter() 和 Handler.removeFilter() | 为handler添加和删除一个过滤器对象           |

**注意**

- 不应该直接实例化和使用`Handler`实例，因为`Handler`是一个基类，它只定义了`handlers`都应该有的接口，同时**提供了一些子类可以直接使用或覆盖的默认行**为
- 下面是一些常用的`Handler`

| Handler                                   | 描述                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| logging.StreamHandler                     | 将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象 |
| logging.FileHandler                       | 将日志消息发送到磁盘文件，默认情况下文件大小会无限增长       |
| logging.handlers.RotatingFileHandler      | 将日志消息发送到磁盘文件，并支持日志文件按大小切割           |
| logging.hanlders.TimedRotatingFileHandler | 将日志消息发送到磁盘文件，并支持日志文件按时间切割           |
| logging.handlers.HTTPHandler              | 将日志消息以GET或POST的方式发送给一个HTTP服务器              |
| logging.handlers.SMTPHandler              | 将日志消息发送给一个指定的email地址                          |
| logging.NullHandler                       | 该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现 |

### Formater类

`Formater`对象用于配置日志信息的最终顺序、结构和内容

- 与`logging.Handler`基类不同，可以直接实例化`Formatter`类来获取`Formater`对象

- 如果应用程序需要一些特殊的处理行为，也可以实现一个`Formatter`的子类来完成。

`Formatter`类的构造方法如下

```python
logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
```

该构造方法接收3个可选参数

- `fmt`：指定**消息格式化字符串**，如果不指定该参数则默认使用message的原始值
- `datefmt`：指定**日期格式字**符串，如果不指定该参数则默认使用`"%Y-%m-%d %H:%M:%S"`
- style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'

## error和exception

**区别**

- `logging.error`：只记录一个日志消息，日志等级是error

- `logging.exception`：在记录消息的同时，**默认会记录错误发生的traceback信息**
  - 但是`error`也可以输出traceback信息, 只需要设置一个参数`exc_info = True`



# 测试

## 文档测试

## 单元测试

单元测试是用来对**一个模块、一个函数或者一个类**来进行正确性检验的测试工作，把多个测试用例放到一个测试模块里就是一个完整的单元测试

> 单元测试是由开发人员进行的，而其他测试都由专业的测试人员来完成

**作用**

- 单元测试通过后，如果我们对原来的代码做了修改，只需要再跑一遍单元测试

- 如果通过，说明修改不会对原来的代码造成影响，如果不通过，说明修改与原来的代码不一致，要么修改代码，要么修改测试

### Unittest

`import unittest`

#### 规则

- **测试文件**必须导入`unittest`
- **测试类**必须继承`unittest.TestCase`

- **测试方法**以`test`开头，不以`test`开头的方法测试的时候不会被执行
- **默认执行全部用例**，也可以通过加载`testsuit`执行部分用例
- `setUp()`和`tearDown()`只能针对所有用例
- `unittest.TestCase`提供了很多内置的条件判断

> Python标准库中自带的单元测试框架

```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
  	# 该方法会首先执行，方法名为固定写法
    def setUp(self):
        pass

    # self.assertEqual(a,b)
  	def test_key(self):
        d = Dict()
        d['key'] = 'value'
        # self.assertEqual通过==判断
        self.assertEqual(d.key, 'value')

    # self.assertTrue(a)
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        
    # self.assertRaises(Error)，Error是期待抛出的error
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            
    # 该方法会在测试代码执行完后执行，方法名为固定写法
    def tearDown(self):
        pass
```

#### 运行

```python
# 直接运行
if __name__ == '__main__':
    unittest.main()

python mydict_test.py

# 通过命令行参数-m unittest执行，可以一次批量运行很多单元测试
python -m unittest mydict_test

# 通过-v参数获取更详细（更多的冗余）的信息
python -m unittest -v mydict_test
```

### Pytest

`import pytest`

- 支持用简单的`assert`语句实现丰富的断言，无需复杂的`self.assert*`函数
- 自动识别测试模块和测试函数
- 模块化以管理各类测试资源
- 丰富的插件生态，已有300多个各式各样的插件

> Python的一个第三方单元测试库
>
> **兼容unittest**，可以执行unittest风格的测试用例，无须修改unittest用例的任何代码

#### 规则

- **测试文件**名必须以`test_`开头或者`test`结尾
- 测试类必须以`Test`开头，并且不能带有`__init__`方法
- **测试方法**必须以`test_`开头
- 可以通过`@pytest.mark`来标记类和方法，`pytest.main`加入参数`-m`可以只运行标记的类和方法
- 任意自定义的函数，只要加上`@pytest.fixture()`，就可以被所有用例使用
- `assert`支持各种条件表达式

```python
# test_moduleName.py  测试模块名
 
class TestClassName:
    """测试类"""
 
    def test_func_name(self):
        """测试方法"""
 
        # 预期结果
        a = ...
 
        # 用例执行结果
        x = ''
 
        # 断言
        assert x == a  # 是否相等
        assert x != a  # 是否不相等
        assert x is a  # 是否是同一内存地址
        assert x in a  # a 是否包含 x
        assert x not in a  # a 是否不包含 x
        assert x > a  # 是否大于 a
        assert x < a  # 是否小于 a
        assert isinstance(x, dict)  # x 是否是 dict 类型
        ...
```

#### 命令参数

- `-v`：显示每个测试函数的执行结果
- `-q`：只显示整体测试结果
- `-s`：显示测试函数中print()函数输出
- `-x，--exitfirst`：exit instantly on first error or failed test
- `-h`：帮助

#### 固件

`fixture`

**scope**：参数有四种，默认为`function`

- function：每个test都运行，默认是function的scope
- class：每个class的所有test只运行一次
- module：每个module的所有test只运行一次
- session：每个session只运行一次

#### mock

测试时，在不修改源码的前提下，替换某些对象，模拟测试环境



### 装饰器单元测试

```python
import wrap_response
import json


@wrap_response
def mock_func(x):
    return x


class TestWrapResponse:
    def test_str_response(self):
        str = 'Empty '
        resp = json.loads(mock_func(str).data)
        assert isinstance(resp, dict)
```

### 跳过装饰器测试

web应用时常需要验证权限，测试的时候需要忽略这个验证装饰器

```python
@login_required
def view():
    return "logged in"
```

如果该装饰器使用了@wraps装饰器，那么就可以通过访问`__wrapped__`属性来获取原函数

```python
# 装饰器
from functools import wraps
def triple(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs) * 3
    return wrapped_func

@triple
def example(x):
    return x
  
---------------------------------------------------------------------------------------
# 测试原始函数
from unittest import TestCase
class TestExample(TestCase):
    def test_with_the_decorator_returns_3(self):
        self.assertEqual(example(1), 3)
		
    # 使用example.__wrapped__调用原函数
    def test_without_the_decorator_returns_1(self):
        self.assertEqual(example.__wrapped__(1), 1)
```



### flask单元测试