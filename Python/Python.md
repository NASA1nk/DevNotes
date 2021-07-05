# 简介

- 解释型语言

- 代码不能加密（解释型的语言发布程序必须把源码发布出去）
- python目前有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的



# 安装

标准的python环境安装后有：

- Python解释器（负责运行Python程序）
- 命令行交互环境
- 简单的集成开发环境



安装完成后在命令提示符窗口输入python后提示版本信息说明Python安装成功

编写Python代码得到的是一个包含Python代码的以`.py`为扩展名的文本文件，运行代码需要Python解释器去执行`.py`文件

官方版本的python解释器：CPython（C语言开发）

> 在命令行下运行`python`就是启动CPython解释器，CPython用`>>>`作为提示符
>
> IPython基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。IPython用`In []:`作为提示符



# Anaconda

- conda：包和环境管理器
- pip：包管理器
- virtualenv：环境管理器

> **conda**： 开源包管理系统和环境管理系统，支持Python, Java, C/C++ 等多种语言，支持Windows, macOS 和 Linux 上运行
>
> **pip**：官方包管理器，推荐用于安装Python包索引（`PyPI`）上发布的包

Anaconda是一种为科学计算而生的Python发行版，包括：

- 标准的python环境
- conda(包和环境的管理器)
- 科学包以及依赖项

[Anaconda | The World's Most Popular Data Science Platform](https://www.anaconda.com/)

[anaconda | 清华大学开源软件镜像站](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)

> miniconda
>
> 安装anaconda就不需要单独装python
>
> 安装完成后重启生效

添加环境变量

使用python3.x版本

![Anaconda安装](Python.assets/Anaconda安装.png)

## 运行

- 输入`python`进入**交互式界面**
- 输入`ipython`进入**交互式界面**
- `ctrl+d`退出

**交互式**

![ipython](Python.assets/ipython.png)



**bash（批量）方式**

```bash
python temp.py
```

![spyder](Python.assets/spyder.png)



## conda

可以自动处理包之间的依赖关系（相比pip）

- which conda/conda -version：检查是否安装正确
- conda list：查看安装的包
- conda install * ：安装
- conda update：升级
- remove/uninstall * ：卸载

```bash
conda create -n ink python=3.6
conda activate ink
conda deactivate ink
```

在Anaconda中，conda和pip安装的包都是python环境的一部分（安装在同一路径），项目对于包的使用是没有区别的

- conda下载的包，conda和pip都可以更新和卸载
- pip下载的包，只能由pip更新和卸载，conda卸载不了



# Pyenv

Python环境管理工具，可以切换全局解释器版本



# 基础语法

- python是动态语言，**变量不用声明**
- python没有终止符，`;`可以让多个语句写在一行
- python没有代码块，用相同的**缩进**表示同一代码块
  - Tap
  - 4个空格
- help()：可以展示帮助信息

![help](Python.assets/help.png)

## 编码

计算机只能处理数字，如果要处理文本也必须先把文本转换为数字才能处理，Unicode字符集把所有语言都统一到一套编码里（**两个字节表示一个字符**），这样就不会再有乱码问题

把Unicode编码转化为“可变长编码”的`UTF-8`编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节。如果传输文本包含大量英文字符，用UTF-8编码就能节省空间。

- **内存中统一使用Unicode编码**
- **硬盘或者传输的时候使用UTF-8编码**

python源代码也是一个文本文件，当源代码中包含中文时就要指定保存为UTF-8编码

当python**解释器**读取源代码时，为了让它按UTF-8编码读取，通常在文件开头写上两行代码

- 可以让`.py`文件直接在Unix/Linux/Mac上运行
- 表示`.py`文件本身使用标准UTF-8编码

```bash
#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
```



**字符**

**单个字符**的编码

- `ord()`函数：获取字符的整数表示
- `chr()`函数：把编码转换为对应的字符

```python
# 65
ord('A')

# 20013
ord('中')

# 'B'
chr(66)

# '文'
chr(25991)
```



**字符串**

字符串的类型是`str`，**在内存中以Unicode表示**，一个字符对应若干个字节

如果要在网络上传输或者保存到磁盘上，就需要把字符串`str`转换成**以字节为单位**的`bytes`。`bytes`类型的数据用带`b`前缀的单引号或双引号表示：

```python
x = 'ABC'	#str的一个字符对应若干个字节
x = b'ABC'	#bytes的每个字符都只占用一个字节。
```

`str`通过`encode()`方法编码为指定的`bytes`

```python
# b'ABC'
'ABC'.encode('ascii')

# b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('utf-8')

# 报错，因为中文超出了ascii码的范围（0-127）
'中文'.encode('ascii')	
```

`bytes`通过`decode()`方法转换为`str`

```python
# 'ABC'
b'ABC'.decode('ascii')

# '中文'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
```



## 注释

- 单行注释：`#`
- 多行注释：`''' '''`



## 关键字

**保留字不可以做变量名**

- `and`
- `as`
- `assert`
- `class`
- `def`
- `del`
- `elif`
- `except`
- `try`
- `lambda`
- `None`



## 输入输出

**输入**

`input`：接受并返回用户输入内容，返回的数据类型是字符串`str`

```python
# 提示输入
a = input("please enter your age: ")

# 可以用int()把字符串str强制转换成整形
age = int(a)
```

**输出**

`print`：依次打印输出每个字符串，遇到`,`会**输出一个空格**

```python
# 输出Hello world
print("Hello","world")
```

**格式化输出**

**.format**

用传入的参数依次替换字符串内的占位符`{}`

```python
# 输出Hello world
print("{} {}".format("Hello","world"))

# 输出Hello ink, 成绩提升了20.1%
print("Hello {}, 成绩提升了{:.1f}%".format("ink", 20.12))
```

> `:.1f` ：`:`后面的`.1f`指定了格式化参数（保留一位小数）



**%**

**在字符串内部**

- `%s`：表示字符串
- `%d`：表示整数
- `%f`：表示浮点数

> `%s`会把任何数据类型转换为字符串
>
> 转义字符：
>
> - `%%`：`%`
> - `\\`：`\`

有几个`%`占位符后面就跟几个变量或者值（顺序对应，写在括号中），如果只有一个`%`，括号可以省略

```python
# 输出ink
print("%s" % "ink")

# 输出Hi ink, you have 1000000元
print("Hi %s, you have %d元" % ("ink",1000000))
```



**f-string**

用`f`指定f-string格式化输出

以对应的变量替换字符串中包含的含对应变量名的`{}`

```python
# 输出The area of a circle with radius 2 is 12.56
r = 2
s = 3.14 * r * 2
print(f"The area of a circle with radius {r} is {s:.2f}")
```

> `{r}`被变量`r`的值替换，`{s:.2f}`被变量`s`的值替换



## 不可变对象

调用不可变对象自身的任意方法都不会改变对象自身的内容

**这些方法会创建新的对象并返回**，这样就保证了不可变

```python
# b = 'Abc'
# replace方法创建了一个新的字符串"Abc"并用变量b指向它
# a = 'abc'不变
a = 'abc'
b = a.replace('a', 'A')	
```



# 数据类型

python允许在数字中间以`_`分隔

- `10_000_000_000`和`10000000000`是一样的
- 十六进制数也可以写成`0xa1b2_c3d4`

## None

不是没定义

```python
# None
ink = None
print(ink)
```



## 字符串

`str`

### 切割

`split(delimiter)`：将字符串切割成一些单词**存入list中**

> `delimiter`分隔符默认为所有的空字符，包括空格、换行`\n`、制表符`\t`等

```python
# t = ['hello', 'world']
s = "hello-world"
delimiter = '-'      	
t = s.split(delimiter)
```

### 拼接

`delimiter.join(list)`：将列表中的字符串元素拼接起来，需要指定`delimiter`分隔符

```python
# s = hello-world
delimiter = '-'        
s = delimiter.join(t)	#用-拼接列表t中的元素
```

### len

**python内置函数**

- 计算`str`包含多少个字符
- 计算`byte`包含多少个字节
- 计算`list`元素的个数



## 列表list

列表list是内置数据类型，是一种有序的集合`[]`，里面元素可以改变(可变对象)

- list里面的元素的数据类型可以不同，也可以是一个list（list计算时只算一个元素个数）相当于一个二维的数组

- 空的list长度为0


### 参数

**list中有三个参数，用冒号分割**（切片）

`list[param1:param2:param3]`

- `param1`：相当于start_index，可以为空，**默认是0**
- `param2`：相当于end_index，可以为空，**默认是list的长度**
- `param3`：步长，**默认为1**。当步长为-1时，返回原序列的倒序

### 创建

1. 直接创建空list
2. 使用`[0]`和数创建元素都为0的list
3. 使用`range()`函数生成整数序列（默认从0开始），再通过`list()`函数生成一个list
   1. `range(1, 101, 2)`：可以用来产生1到100的奇数
   2. `range(100, 0, -2)`：可以用来产生100到1的偶数
4. 用字符串创建list，**list的每一个元素就是字符串的每一个字符**
5. 使用切片`[:]`创建list，`[:]`相当于重新定义列表元素，指向到`=`右侧**可迭代对象的所有元素**

```python
# l = []
l = []

# m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = 10
m = [0]*n

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
list(range(0, 20, 2))

# ['1', '1', '1']	
list1 = list('111')	

# ['2', '3', '4']
list[:] = ['2','3','4']
```

### 赋值

变量个数要和list的元素个数相同

可以使用**切片**`[:]`来改变要赋值的list的元素个数

```python
a = [1, 2, 3]

# b = 1, c = 2, a = 3 相当于b,c,d依次获得了列表a的各个元素
b, c, d = a		
print(b,c,d)

# e = 1, f = 2 相当于e,f依次获得了列表a的第一个元素和第二个元素
e,f  = a[0:2]
print(e,f)
```

### 替换

下标替换

```python
# a = [1, 'ink', 3]
a = [1, 2, 3]
a[1] = 'ink'
print(a)
```

### 索引

**list索引可以是负数，表示从末尾倒数取元素**

- `[-1]`：倒数第一个元素
- `[-2]`：倒数第二个元素

```python
# 输出world
print(t[-1])
```

### 添加

`append()`：追加元素到list的末尾，`append()`的参数会作**为一个元素**追加到列表末尾

```python
# t = ['hello', 'world', 'ink']
t.append("ink")	

# t = ['hello', 'world', 'ink', ['1', '2', '3']]
t.append(["2","3","4"])
```

### 插入

`insert()`：插入元素到list的指定位置

```python
# t = ['hello', 'god', 'world', 'ink']
t.insert(1,"god")
```

### 删除

`pop()`：删除list的指定位置元素，不提供位置默认删除list的末尾元素

> - `pop()`：删除列表元素并返回被删除的元素
> - `del()`：直接删除对应下标的元素
> - `remove()`：直接删除对应元素

```python
# t = ['hello', 'god', 'world']
t.pop()

# t = ['god', 'world', 'ink']
t.pop(0)
```

### 拼接

- `+=`：拼接
- `extend()`：`extend()`的参数是可迭代对象，会遍历list后追加到list末尾
  - 字符串`str`也是一种`list`，**每个元素就是一个字符**，`extend()`会切分字符串
- `[len(list):]`：切片，从`len()`后追加
  - **列表的末尾不是-1**而是None（-1后一位）
  - 列表的切片**不会越界**（追加到最后）

```python
# list1 = ['1', '1', '1']
# list2 = ['ink']
# 把list2中的所有元素追加到list1中 
# list1 = ['1', '1', '1', 'ink']
list1 += list2  		
list1 = list1 + list2 	
list1.extend(list2)  	
list1[len(list1):] = list2

# list1 = ['1', '1', '1', '2', '3', '4']
list1.extend('234')

# list1 = ['1', '1', '2', '3', '4', '1']
list1[-1:-1] = '234'

# list1 = ['1', '1', '2', '3', '4']
list1[-1:] = '234'

# list1 = ['1', '1', '1', '2', '3', '4']
list1[5:5] = '234'	
```



## 元组tuple

**元组tuple是不可变的列表list**（不可变对象）

- tuple一旦初始化就**不能修改**。因此定义一个tuple时里面的元素就必须被确定下来

- 当tuple中有list元素时候，list中的元素可以改变

- 只有**1个元素**的tuple会用`,`和运算符`1`区分（打印时也会显示）

- 列表list中的元素也可以是元组

  > 访问列表元素时，i[0]表示tuple里第一个元素，i[1]表示tuple里第二个元素

```python
# 空的tuple 
t = ()		

# 1个元素的tuple
t = (1,)

# 用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]	
```



## 字典dict

字典`dict`使用哈希表实现，使用`key-value`键值对存储

- `dict`的键`key`必须是可哈希的`hashable`
- `dict`的键`key`必须是不可变对象

因为可变类型在哈希时可能映射成别的值（无法正确工作）。所以**列表`list`不能作为键`key`，只能作为值`value`**

> `dict`需要占用大量的内存，内存浪费多，是用空间来换取时间的一种方法(相比于`list`)

```python
# dictt[key]就是value，对dictt[key]操作就是对value操作
# {'on': 'no'}  
dictt['on'] = 'no'
```



### 查找

字典`dict`中的项`item`的顺序是未知的，所以字典`dict`中的元素不使用整数索引而是用键`key`来查找对应的值`value`

字典使用哈希`Hash`算法，无论字典中有多少项`item`，`in`运算符搜索所需的时间都是一样的。

> 列表list中`in`操作符随着列表的增长搜索时间成正比增长



`get()`：接受一个`key`和一个默认值作为参数，

- `dict`中存在该`key`，返回`key`对应`value`
- `dict`中不存在该`key`，返回传入的默认值，对`dict`不影响。



### 存储

`key-value`存储方式在**存**的时候必须根据`key`算出`value`的存放位置，这样取的时候才能根据`key`直接拿到`value`

- `dict`内部存放的顺序和`key`放入的顺序是没有关系的
- 一个`key`只能对应一个`value`，多次对相同`key`放入`value`只保存最后一次存入的`value`（覆盖）




### 删除

`pop(key)`：删除dict中的key和对应的value



## set

**无序**和**无重复元素**的集合

- `set`不存储`value`，是一组`key`的集合。
- `set`中没有重复的元素（因为`key`不能重复），传入重复的元素在`set`中会被自动过滤
- `set`的原理和`dict`一样，所以**不能放入可变对象**（因为无法判断两个可变对象是否相等，也就无法保证`set`内部**不会有重复元素**）

### 创建

使用list作为输入集合创建`set`

```python
# s = {1, 2, 3}
# 显示的顺序不表示set是有序的
s = set([1, 2, 3])		
```

### 添加

`add()`：添加元素到set中，重复添加不会显示

```python
# s = {1, 2, 3, 4}
s.add(4)
s.add(4)
```



### 删除

`remove()`：删除元素

```python
# s = {1, 2, 3}
s.remove(4)
```



# 控制结构

## 条件判断

只要是非零数值，非空字符串，非空list等就判断为`True`

```python
# 输出ink
if 2>4:
    print("Yes")
elif 2==4:
    print("No")
else:
    print("ink")

# 一行赋值形式
result = 'ink' if a >= b else 'yinke'
```



## 循环

### for循环

**遍历元素**

变量`x`依次将`list`或`tuple`中的每个元素迭代出来

```python
names = ['Michael', 'Bob', 'Tracy']
# x是元素,不是下标
for x in names:			
    print(x)
```

**遍历索引**

使用`range()`和`len()`函数生成索引

```python
# 0 Michael
# 1 Bob
# 2 Tracy
names = ['Michael', 'Bob', 'Tracy']
for index in range(len(names)):
   print(index,names[index])
```

> 如何设置i从2开始循环



### while循环

```python
while a:		
    a
```

### break

`break`语句可以提前退出循环

### continue

`continue`语句可以跳过当前的这次循环，直接开始下一次循环



# 函数

**递归函数**

使用递归函数要防止`栈溢出`

在计算机中，函数调用是通过栈`stack`实现的

- 每进入一个函数调用，栈就会加一层**栈帧**
- 每当函数返回，栈就会减一层**栈帧**

栈的大小不是无限的，所以**递归调用的次数过多会导致栈溢出**

解决递归调用栈溢出的方法是通过**尾递归优化**

尾递归是指**在函数返回的时候调用自身，并且return语句不能包含表达式**。这样编译器或者解释器就可以把尾递归做优化，使**递归本身无论调用多少次都只占用一个栈帧**，不会出现栈溢出的情况



## 定义函数

`def` 函数名 括号 参数 `:`

函数的返回值用`return`语句，如果没有`return`语句，函数执行完毕后返回`None`。

> `return None`简写为`return`

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```



## 调用函数

函数名是**指向一个函数对象的引用**。可以把函数名赋给一个变量，相当于给这个函数起了一个**别名**

```python
>>> a = abs	    # 变量a指向abs函数
>>> a(-1) 		# 所以也可以通过a调用abs函数
1
```



## 空函数

用`pass`语句定义一个**什么事也不做**的空函数（占位）

> 否则程序无法正常执行

```python
# 用来暂存还未完成的函数
def nop():	
    pass
```



## 函数返回值

函数可以返回多个值，**多个值其实返回的是一个tuple**

- 返回一个tuple时可以省略括号
- 多个变量可以同时接收一个tuple，按位置赋给对应的值

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    
# (151.96152422706632, 70.0)
r = move(100, 100, 60, math.pi / 6)
```



## 函数参数

### 位置参数

调用函数时，传入值按照**位置顺序**依次赋给参数

```python
# 第一个是x,第二个是n
def power(x, n):	
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

### 默认参数

常用或默认的参数值可以直接写在函数中从而简化函数的调用，当传入的数据与默认参数不符合时再传入实际值

- 必选参数在前，**默认参数在后**
- 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面（变化小的参数就可以作为默认参数）
- 当函数有多个默认参数时
  - 调用时按顺序提供默认参数
  - 调用时不按顺序提供部分默认参数要写清楚参数名和对应值

> **定义默认参数必须指向不变对象(如str,None)**
>
> 如果在函数体里面执行了会改变默认参数的值的操作就会引发错误

```python
# power(5)实际上是power(5, 2)
def power(x, n=2):		
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```



### 可变参数

`*args`

- 在参数前面加`*`，参数接收到的就是一个`tuple`（个数可变）
- 在`list`或`tuple`前面加`*`可以把`list`或`tuple`的元素变成可变参数

```python
def calc(*numbers):		
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 5
calc(1, 2)

# 0
calc()

nums = [1, 2, 3]
# 14
calc(*nums)
```



### 关键字参数

`**kw`

传入0个或任意个**含参数名的参数**，关键字参数在函数内部自动组装为一个`dict`

在`dict`前加上`**`，可以把该`dict`转换为关键字参数

> `**extra`表示把`extra`这个`dict`中的所有`key-value`键值对传入到函数的关键字参数，`kw`获得的`dict`是`extra`的一份拷贝，对`kw`的改动不会影响`extra`

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
# name: Bob age: 35 other: {'city': 'Beijing'}    
person('Bob', 35, city='Beijing')

# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
```

可以在函数内部通过关键字参数`kw`检查传入了哪些参数

```python
#检查是否有city和job参数
def person(name, age, **kw):
    if 'city' in kw:
        print("有city")
    if 'job' in kw:
        print("有job")
    print('name:', name, 'age:', age, 'other:', kw)
    
# 有city
# name: Bob age: 35 other: {'city': 'Beijing'
person('Bob', 35, city='Beijing')
```



### 命名关键字参数

关键字参数`key-value`的传入不受限制，如果想**限制关键字参数的名字**就要用**命名关键字参数**

- 命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数
- 如果函数中已经有了一个可变参数，后面的命名关键字参数就不再需要特殊分隔符`*`
- 命名关键字参数具有**默认值**时，调用函数时可不传入此参数

```python
# 只接收city和job作为关键字参数
def person(name, age, *, city, job):	
    print(name, age, city, job)

# 命名关键字参数必须传入参数名
person('Jack', 24, city='Beijing', job='Engineer') 
Jack 24 Beijing Engineer

# 不再需要特殊分隔符*
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
    
#city具有默认值
def person(name, age, *, city='Beijing', job):		
    print(name, age, city, job)

# Jack 24 Beijing Engineer
person('Jack', 24, job='Engineer')	
```



### 组合参数

可变参数+关键字参数

任意函数都可以通过类似`func(*args, **kw)`的形式调用，无论它的参数是如何定义的

## hash和id

`id`：取对象的地址（cpython中）

区分可变和不可变类型

- **不可变类型**：改变对象会创建一个新的对象并指向新的对象（地址发生变化）

- **可变类型**：值改变时，地址不发生变化

  > 无法用于hash函数
  >
  > 可变类型`list`就是一个unhashable type



`hash`

`hash`的实现和地址有关系

相同内容的哈希值一定是相同的



**哈希碰撞**

`collision`：不同的输入得到同一个哈希值

防止哈希碰撞的最有效方法就是扩大哈希值的取值空间

> 黑客攻击的一种方法就是设法制造"哈希碰撞"，然后入侵系统窃取信息

# 高级特性

## 切片

`slice`

切片操作符`[n:m]`：返回从第n个元素到第m个元素的`list`或`turple`（**包括第一个但不包括最后一个**：`[)`）

> 字符串`str`也可以看成是一种`list`，**每个元素就是一个字符**。因此字符串也可以用切片操作

- 省略第一个索引n，切片将从列表头开始（第一个索引0也可以省略）

- 倒数第一个元素的索引是`-1`，省略第二个索引m，切片将到列表尾结束

- 两个索引n和m都省略就是操作整个`list`或`turple`

- `[n:m:l]`：可以间隔切片，l是间隔距离（每l个取一个），**当l步长为负数时，表示倒序**（此时n要大于m）

  > [::-1]切片：从列表最后一位开始，步长为-1，即从[-1]开始，索引值每次累加-1，累加值为-`len()`时结束

```python
L = [0,1,2,3,4,5,6,7,8,9,10]
# 取前10个元素
L[:10]		

# 取后10个元素
L[-10:]	

# 前11-20个元素	
L[10:20]	

# 末尾2个元素(倒数第二个和倒数第一个元素)
L[-2:]

# 倒数第二个元素
L[-2:-1]

# 前10个数,从第一个数开始,每两个取一个[0, 2, 4, 6, 8]
L[:10:2]

# 所有数,从第一个数开始,每5个取一个[1, 6]
L[::5]	

# 倒序
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
L[::-1]

# [10, 7, 4, 1]
L[::-3]

# [6, 5, 4, 3]
L[6:2:-1]

# []
L[2:6:-1]
```



## 迭代

`iteration`

通过`for`循环来遍历`list`或`tuple`称为迭代`Iteration`

### 可迭代对象

`iterable`

可迭代对象都可以作用于`for`循环。自定义的数据类型只要符合迭代条件就可以使用`for`循环

通过`collections`模块的`Iterable`类型可以判断**是不是可迭代对象**`iterable`

```python
from collections import Iterable

# True,str可迭代
isinstance('abc', Iterable)   

# True,list可迭代
isinstance([1,2,3], Iterable)

# False,整数不可迭代
isinstance(123, Iterable)   

# True,dict可迭代
isinstance({'a':'1'}, Iterable)
```

**字典**

`dict`默认迭代的是键`key`

- 迭代值`value`：`for value in d.values()`
- 迭代`key`和`value`：`for k, v in d.items()`

> dict的存储不是按照list的方式顺序排列，所以迭代出的结果顺序可能不一样

```python
# a
# b
# c
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
```

**字符串**

`str`迭代每字符串的每一个字符

```python
# A
# B
# C
for ch in 'ABC':
    print(ch)
```

**下标迭代**

`enumerate()`：可以把`list`转换成**索引-元素**对，这样就可以在`for`循环中同时迭代索引和元素本身

```python
# 0 A
# 1 B
# 2 C
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
```



## 列表生成式

`comprehensions`

创建list，避免繁琐的循环

- `for`前面可以写生成式
- `for`前面可以写函数，元素必须可以调用函数
- `for`前面可以写`if`表达式，必须加上`else`
- `for`后面可以写`if`表达式，不用加上`else`
- `for`可以嵌套

```python
# 生成式,[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x * x for x in range(1, 11)]					

# 调用函数,['hello', 'world', 'ibm', 'apple']
L = ['Hello', 'World', 'IBM', 'Apple']			
[s.lower() for s in L]

# if-else表达式,[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
[x if x % 2 == 0 else -x for x in range(1, 11)]	

# if表达不加else,[4, 16, 36, 64, 100]
[x * x for x in range(1, 11) if x % 2 == 0]		

# 两层for循环,['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ']
[m + n for m in 'AB' for n in 'XYZ']			

# 多个变量生成list,['y=B', 'x=A', 'z=C']
[k + '=' + v for k, v in d.items()]				
```



## 生成器

`generator`

如果`list`元素可以按照某种**算法**推算出来就可以在循环的过程中**不断推算出后续的元素**。这样就不必创建完整的`list`，从而节省大量的空间。

这种**一边循环一边计算**的机制称为生成器`generator`

### 创建

**列表创建**

把列表生成式的`[]`改成`()`就创建了一个`generator`

```python
# 列表生成式,[0, 1, 4, 9, 16]
L = [x * x for x in range(5)]

# 不显示列表,<generator object <genexpr> at 0x00000237FFE714C0>
g = (x * x for x in range(5))
print(g)
```

**函数创建**

算法比较复杂时用类似列表生成式的`for`循环无法实现。可以用函数实现。

在函数中用`yield`关键字代替`return`就是一个`generator`

```python
def fib():
    n, a, b = 0, 0, 1
    while true:
        # 将return改为yield
        yield b			
        # 给a,b同时赋值
        a, b = b, a + b			
        n = n + 1
    return 'done'
```

**调用函数创建的`generator`和函数的执行流程不一样**

1. 调用前要生成一个`generator`对象
2. 在每次调用`next()`的时候执行，遇到`yield`语句返回
3. 再从上次返回的`yield`语句处继续执行
4. 当没有`yield`可以执行时调用`next()`就会报错

```python
# yield代替了return,odd()是一个generator
def odd():
    print('step 1')
    yield 1				
    print('step 2')
    yield 2
    print('step 3')
    yield 3

# 1.生成generator对象
o = odd()	

# 2.调用next()函数
# step 1
# 1
next(o)			

#从上一个停止的yield处开始
# step 2
# 2
next(o)			

# 再next(o)就会报错
# step 3
# 3
next(o)			
```



### 读取

列表创建的`generator`可以使用`for`循环读取，因为`generator`也是**可迭代对象**

```python
# 0 1 4 9......
g = (x * x for x in range(10))
for n in g:
    print(n)
```



`for`循环调用`generator`时得不到`generator`的return语句的返回值

想要拿到返回值必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中

> `generator`保存的是**算法**，每次调用`next(g)`就计算出`g`的下一个元素的值直到最后一个元素，当没有更多的元素时抛出`StopIteration`的错误

```python
# g: 1
# g: 1
# g: 2
# Generator return value: done
def fib(n):
    a, b = 0, 1
    while n:
        yield b
        a, b = b, a + b
        n = n - 1
    return 'done'

while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break

g = fib(3)
```



## 迭代器

`iterator`

可以被`next()`函数调用并不断返回下一个值的**对象**称为迭代器：`Iterator`。

使用`isinstance()`判断一个对象是否是迭代器（`Iterator`对象）

- 生成器`generator`都是`Iterator`对象，
- `list`、`dict`、`str`是可迭代对象`Iterable`却不是迭代器`Iterator`
- 使用`iter()`函数可以将`list`、`dict`、`str`等可迭代对象`Iterable`转换成迭代器`Iterator`

```python
from collections.abc import Iterator

# True
isinstance((x for x in range(10)), Iterator)

# False
isinstance([], Iterator)

# False
isinstance({}, Iterator)

# False
isinstance('abc', Iterator)

# True
isinstance(iter([]), Iterator)

# True
isinstance(iter('abc'), Iterator)
```



# 函数式编程

函数式编程就是一种抽象程度很高的编程范式

纯粹的函数式编程语言编写的函数没有变量，因此任意一个函数只要输入是确定的，输出就是确定的，这种纯函数称之为没有副作用。

函数式编程的一个特点就是允许把函数本身作为参数传入另一个函数，还允许返回一个函数。

> python对函数式编程提供部分支持。由于python允许使用变量，因此python不是纯函数式编程语言

## 高阶函数

### Map

`map()`接收两个参数，一个是函数，一个是可迭代对象`Iterable`
`map()`将传入的函数**依次作用到序列的每个元素**，并把结果作为新的迭代器`Iterator`返回

```python
# r = [1, 4, 9, 16, 25, 36, 49, 64, 81]
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)
```

### Reduce

`reduce()`接收两个参数，一个是函数，一个是可迭代对象`Iterable`

`reduce()`将传入的函数作用在一个序列上来计算累积结果

> 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用function函数运算，最后得到一个结果

```python
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
from functools import reduce

def f(x,y):
    return x * y
# S = 24
s = reduce(f, [1,2,3,4])

# 把str转换为int
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # 返回key对应的value
    return digits[s]

# 输出13579
reduce(fn, map(char2num, '13579'))
```

### Filter

`filter()`是一个**筛选**函数

`filter()`接收一个函数和一个序列

`filter()`把传入的函数**依次作用于序列的每个元素**，然后根据**返回值**是`True`还是`False`决定保留还是丢弃该元素

`filter()`函数返回的是一个迭代器`Iterator`，也就是一个惰性序列（仅仅在迭代至某个元素时才计算该元素），所以要强迫`filter()`完成计算结果需要用`list()`函数获得所有结果并返回`list`

```python
# 删掉list中的偶数
def is_odd(n):
    return n % 2 == 1

# [1, 5, 9, 15]
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))	
```



素数

> `Iterator`是惰性计算的序列，所以可以用Python表示**全体自然数，全体素数**这样的序列
>
> 关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数

```python
# 生成器,构造一个从3开始的无限奇数序列	
def _odd_iter():							
    n = 1					
    while True:
        n = n + 2
        # 惰性,返回3停止,调用next()才会继续算n+2
        yield n								

# 筛选函数
def _not_divisible(n):			
    # lambda可以理解为一个函数生成器,返回的是一个函数
    # :之前的是输入, :之后的是输出
    return lambda x: x % n > 0				
											
# 生成器,生成素数列表			
def primes():
    # 第一个素数2
    yield 2					
    # 生成generator对象,序列从3开始，后面的到next()调用再计算
    it = _odd_iter()						
    while True:
        # 返回序列的第一个数
        n = next(it) 						
        yield n
        # 利用filter()不断产生筛选后的新的序列
        it = filter(_not_divisible(n), it) 	

# 打印1000以内的素数
for n in primes():							
    if n < 1000:
        print(n)
    else:
        break
```



### Sorted

两个字符串或者`dict`的比较必须通过函数

`sorted()`函数是一个**升序**排序函数

- 它可以接收一个`key`函数来实现自定义的排序，`key`指定的函数**作用于每一个元素上**，并根据`key`函数返回的结果进行排序
- 它可以接收第三个参数`reverse`，True时即是反向排序（不用修改key）
- 字符串排序默认情况下按照ASCII的大小进行比较

```python
# 按绝对值大小排序,[5, 9, -12, -21, 36]
sorted([36, 5, -12, 9, -21], key=abs)	

# ['Credit', 'Zoo', 'about', 'bob']
sorted(['bob', 'about', 'Zoo', 'Credit'])

# ['Zoo', 'Credit', 'bob', 'about']
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
```



## 返回函数

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回，返回的函数并不会立刻执行

**嵌套函数（Nested Function）**

> 调用`lazy_sum()`时每次调用都会返回一个新的函数（即使传入相同的参数）
>
> 在函数`lazy_sum`中又定义了函数`sum`，内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，**相关参数和变量都保存在返回的函数中**，称为**闭包**（Closure）

```python
# *可变参数，传入的多个参数组装成一个tuple
def lazy_sum(*args):
    # 在外部函数lazy_sum中定义内部函数sum
    # 内部函数sum可以引用外部函数lazy_sum的参数args和局部变量
    def sum():					
        ax = 0					
        for n in args:
            ax = ax + n
        return ax
    # 返回函数sum
    return sum					

# 调用lazy_sum()时返回的是函数sum
f = lazy_sum(1, 3, 5, 7, 9)

# 调用函数f()时才真正计算求和的结果25
f()							

# f1()和f2()的调用结果互不影响。
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

# False	
f1 == f2		
```



## 闭包

闭包`Closure`是词法闭包`Lexical Closure`的简称，**是引用了自由变量的函数**

这个**被引用的自由变量将和这个函数一同存在**，即使已经离开了创造它的环境（返回的内部函数在其定义内部引用了外部函数的局部变量)，闭包使得局部变量在函数外被访问成为可能



返回闭包时：**返回函数不要引用任何循环变量或者后续会发生变化的变量**

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

如果要引用循环变量，就要再创建一个函数。用该函数的参数绑定循环变量当前值，无论该循环变量后续如何更改，已绑定到函数参数的值不变

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



## 匿名函数

有时传入函数不需要显式地定义函数，直接传入匿名函数会更方便

**限制**：

只能有一个表达式，不用写`return`，返回值就是该表达式的结果

**优点**：

- 因为函数没有名字所以不必担心函数名冲突
- 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

```python
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 相当于
def f(x):
    return x * x


f = lambda x: x * x
# 25
f(5)
```



## 装饰器

在代码运行期间动态增加功能的方式称之为**装饰器**Decorator

> 本质上Decorator是一个返回函数的高阶函数

- 函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用函数
- 函数对象有一个`__name__`属性，可以获取函数的名字

```python
def now():
    print('2015-3-25')
# 赋值
f = now

# 2015-3-25
f()

# now
print(now.__name__)

# now
print(f.__name__)
```

`log()`返回一个函数，所以原来的`now()`函数仍然存在，只是现在同名的`now`变量指向了新的函数，所以调用`now()`将执行新函数，即在`log()`函数中返回的`wrapper()`函数

`wrapper()`函数的参数定义是`(*args, **kw)`，因此`wrapper()`函数可以接受任意参数的调用。在`wrapper()`函数内，首先打印日志，再紧接着调用原始函数

```python
# log是一个decorator,接受一个函数作为参数并返回一个函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 相当于now = log(now)
@log
def now():
    print('2015-3-25')
    
# call now():
# 2015-3-25
now()
```



## 偏函数

`functools.partial`

把一个函数的某些参数固定（也就是设置默认值），返回一个新的函数



# 模块

**Module**

在python中一个`.py`文件就称之为一个**模块**

使用模块可以避免函数名和变量名冲突，相同名字的函数和变量可以分别存在不同的模块中，因此在编写模块时不必考虑名字会与其他模块冲突

模块名不要和python自带的模块名称冲突

> 检查方法：在python交互环境执行`import 模块名`，成功则说明系统存在此模块

**Package**

pythonz中引入了**按目录来组织模块**的方法避免模块名冲突，称为**包**

只要模块所在的包名不冲突，那包下所有模块都不会冲突（相当于 **包名.模块名**）

每一个包目录下面都会有一个`__init__.py`文件，这个文件是必须存在的，否则python就把这个目录当成普通目录，而不是一个包。

`__init__.py`可以是空文件，也可以有python代码，因为`__init__.py`本身就是一个模块，它的模块名就是包名



## 作用域

python通过`_`**前缀**来实现变量和函数的作用域

- 正常的函数和变量名是**公开的**（public），可以被直接引用
- `_xxx`和`__xxx`这类的函数和变量是**非公开的**（private），不应该被直接引用
- `__xxx__`这类的变量是**特殊变量**，可以被直接引用，但是有特殊用途（比如`__name__`就是特殊变量），自己的变量一般不要用这种变量名

> private函数和变量**不应该被直接引用**，而不是**不能被直接引用**。因为python并没有方法完全限制访问private函数或变量。从编程习惯上不应该引用private函数或变量
>
> 外部不需要引用的函数全部定义成private，外部需要引用的函数定义为public



## 第三方模块

在python中安装第三方模块：通过包管理工具`pip`完成

**Anaconda**

一个基于Python的数据处理和科学计算平台，内置了许多非常有用的第三方库

Anaconda会把系统Path中的python指向自己自带的Python

Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录

## 模块使用

**标准文件模板**

1. `#!/usr/bin/env python3`：让`.py`文件直接在Unix/Linux/Mac上运行
2. `# -*- coding: utf-8 -*-`：表示`.py`文件本身使用标准UTF-8编码
3. 模块代码的**第一个字符串**都被视为模块的文档注释
4. `__author__`变量可以表明作者

**导入模块**

导入`sys`模块后就有了变量`sys`指向该模块，利用`sys`这个变量就可以访问`sys`模块的所有功能

```python
import sys
```

在**命令行运行**`.py`模块文件时，Python解释器把特殊变量`__name__`置为`__main__`，而如果在其他地方导入该模块时，`if`判断将失败

因此这种`if`测试可以让一个模块通过**命令行运行**时执行一些额外的代码，最常见的就是运行测试

```
if __name__=='__main__':
    test()
```

**模块搜索路径**

当试图加载一个模块时，python会在**指定的路径**下搜索对应的`.py`文件，如果找不到就会报错

> 默认情况下python解释器会搜索**当前目录**、**所有已安装的内置模块**和**第三方模块**，搜索路径存放在`sys`模块的`path`变量中

手动添加搜索路径（目录）有两种方法

- 直接修改`sys.path`，添加要搜索的目录

  > 在运行时修改，运行结束后失效

  ```python
  import sys
  sys.path.append('/Users/michael/my_py_scripts')
  ```

- 设置环境变量`PYTHONPATH`，该环境变量的内容会被自动添加到模块搜索路径中

  > 设置方式与设置Path环境变量类似，只需要添加自己的搜索路径，python本身的搜索路径不受影响



# 面向对象

面向对象编程`Object Oriented Programming`（OOP）

是一种程序设计思想，OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

**面向对象的三大特点**

- 封装
- 继承
- 多态

> python中所有数据类型都可以视为对象



## 类和实例

1. 在python中通过`class`关键字定义类
2. `(object)`表示该类是从哪个类继承下来的，如果没有合适的继承类就使用`object`类（所有类最终都会继承的类）
3. `__init__`方法
   1. 第一个参数`self`表示创建的实例本身，所以在`__init__`方法内部就可以把各种属性绑定到实例上，即`self`
   2. 有了`__init__`方法，在创建实例的时候就不能传入空的参数，必须传入与`__init__`方法匹配的参数，不需要传`self`，python解释器自己会把实例变量传进去
4. python是动态语言，允许对实例变量绑定任何数据，也就是说同一个类的不同实例变量可以拥有的不同的变量名称
5. `isinstance()`可以判断实例是否是某个类的实例

```python
class Student(object):
	
    # 创建实例的时候绑定name，score属性
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 变量bart指向的就是一个Student的实例        
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

bart.age = 8
# 8
bart.age
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'age'
lisa.age
```

## 访问限制

**让外部代码不能随意修改对象内部的状态**

如果要让内部属性不被外部访问，可以把**属性的名称前**加上两个下划线`__`。在python中实例的变量名如果以`__`开头就是一个**私有变量**（private），只有内部可以访问，外部不能访问

> 注意不要和特殊变量（`__xxx__`）混淆
>
> 双下划线开头的实例变量不是一定不能从外部访问。不能从外部直接访问`__name`是因为python解释器对外把`__name`变量改成了`_Student__name`，所以可以通过`_Student__name`来访问`__name`变量
>
> 不同版本的python解释器可能会把`__name`改成不同的变量名
>
> 所以外部即使设置同名变量也不是内部的变量，而是新增了一个变量

```python
class Student(object):

    def __init__(self, name, score):
        # name,score是私有变量,无法从外部访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```



## 继承和多态

### 单继承

没有继承就写`(object)`

当子类和父类都存在相同的方法时，子类的方法会覆盖了父类的方法（在代码运行的时候总会调用子类的方法）

在继承关系中如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类，反过来不行

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

# 继承Animal类
class Dog(Animal):
    pass

class Cat(Animal):
    pass

# a是Animal类型
a = Animal() 
# b是Dog类型
b = Dog() 

# True
isinstance(a, Animal)
# True
isinstance(b, Dog)
# False
isinstance(a, Dog)
```

> **静态语言 vs 动态语言**
>
> 对于静态语言（例如Java）来说，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或者它的子类，否则无法调用`run()`方法
>
> 对于python这样的动态语言来说，则不一定需要传入`Animal`类型，只需要保证传入的对象有一个`run()`方法就可以了（`file-like object`）

### 多重继承

**通过组合而非多层次继承**

MixIn：设计目的是给一个类增加多个功能。在设计类的时候优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系

```python
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 多继承
class bird(Animal,Flyable,Runnable):
    pass
```



## 对象信息

**对象类型**

- `type()`：判断对象类型（变量指向函数或者类也可以判断）
- `type()`函数返回对应的Class类型
- 使用`types`模块中定义的常量判断一个对象是否是函数
  - FunctionType
  - BuiltinFunctionType
  - LambdaType
- `isinstance()`：判断有继承关系的class类型（父继承链）

> 优先使用isinstance()判断类型

```python
# int
type(123)

# str
type('str')

# NoneType
type(None)

# builtin_function_or_method
type(abs)

# True
type(123)==type(456)

# True
>>> type(123)==int

# True
>>> type('abc')==type('123')

# True
>>> type('abc')==str

# False
>>> type('abc')==type(123)
```

**对象属性和方法**

`dir()`：返回一个包含**对象的所有属性和方法**的list

> 如果试图获取不存在的属性会抛出AttributeError的错误

## 属性和方法

**实例属性和类属性**

python是动态语言，根据类创建的实例可以**任意绑定属性**

通过实例变量或者`self`变量给实例绑定属性。**相同名称的实例属性将屏蔽掉类属性**，当删除实例属性后再使用相同的名称访问到的将是类属性

- 实例属性属于各个实例所有，互不干扰
- 类属性属于类所有，所有实例共享

**实例方法和类方法**

实例可以**任意绑定方法**。给一个实例绑定的方法对另一个实例是不起作用的

class绑定方法后所有实例均可调用

### slots

`__slots__`

在定义class的时候定义一个特殊的`__slots__`变量来限制该class**实例能添加的属性**

`__slots__`变量定义的属性仅对**当前类**实例起作用，对继承的子类是不起作用的，如果要限制子类实例绑定属性，就要在子类中也定义`__slots__`，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`

```python
class Student(object):
    # 用tuple定义允许绑定的属性
    __slots__ = ('name', 'age') 
```

### @property

python内置的装饰器，用来把一个方法变成属性（属性的方法名不要和实例变量重名）

把方法变成属性只需要在方法上加`@property`

> 用方法设置属性可以保证对参数进行必要的检查

```python
class Student(object):

    @property
    def score(self):
        return self._score
	
    # @property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()

# 实际转化为s.set_score(60)
s.score = 60 

# 实际转化为s.get_score(),输出60
s.score 

# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
s.score = 9999
```



## 定制类

### 打印

`__str__`：调用`print()`返回的方法

`__repr__`：直接打印变量返回的方法

通常`__str__()`和`__repr__()`代码都是一样的

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    # 偷懒写法
    __repr__ = __str__
```

### 循环

`__iter__`：如果一个类想被用于`for...in`循环就必须实现一个`__iter__()`方法，该方法**返回一个迭代对象**

`__next__`：`for`循环不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环

```python
# 斐波那契类
class Fib(object):
    def __init__(self):
        # 初始化两个计数器a,b
        self.a, self.b = 0, 1 
	
    # 实例本身就是迭代对象,返回自己
    def __iter__(self):
        return self 

    def __next__(self):
        # 计算下一个值
        self.a, self.b = self.b, self.a + self.b 
        # 退出循环条件
        if self.a > 10: 
            raise StopIteration()
        # 返回下一个值
        return self.a 

# 1 1 2 3 5 8
for n in Fib():
    print(n)
```

### 索引

`__getitem__`：实现`__getitem__()`方法就可以按下标访问数列的任意一项。`__getitem__()`传入的参数可能是一个`int`，也可能是一个切片对象`slice`

> 没有对step参数作处理，也没有对负数作处理

```python
class Fib(object):
    def __getitem__(self, n):
        # n是索引
        if isinstance(n, int): 
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # n是切片
        if isinstance(n, slice): 
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# 3
f[3]
# 1 1 2
f[0:3]
```

## 枚举类

`Enum`

定义常量时通常用大写变量通过整数来定义

为枚举变量定义一个class类型，每个常量都是class的一个唯一实例

> class不可变，class中成员可以直接比较

```python
from enum import Enum

# 可以直接使用Month.Jan来引用一个常量,或者枚举它的所有成员
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# value属性则是自动赋给成员的int常量,默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
```

**自定义枚举类**

从`Enum`派生

`@unique`装饰器可以帮助检查保证没有重复值

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

访问

- 根据**成员名称**引用枚举常量
- 根据**value的值**获得枚举常量

```python
day1 = Weekday.Mon

# Weekday.Mon
print(day1)

# Weekday.Tue
print(Weekday.Tue)

# Weekday.Tue
print(Weekday['Tue'])

# 2
print(Weekday.Tue.value)

# Weekday.Mon
>>> print(Weekday(1))

# True
print(day1 == Weekday.Mon)

# True
print(day1 == Weekday(1))


# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
```

## 元类

动态语言：函数和类的定义不是在编译时定义，而是运行时动态创建

# 错误和调试

## 错误处理

`try...except...finally...`：处理错误

某些代码可能会出错时可以用`try`来运行这段代码。如果执行出错则后续代码不会继续执行，而是直接跳转至错误处理代码，即`except`语句块，执行完`except`后，如果有`finally`语句块，则执行`finally`语句块

- 可以没有`finally`语句，但如果有`finally`，就一定会被执行
- 可以有多个`except`来捕获不同类型的错误
- 可以在`except`语句块后面加一个`else`，当没有错误发生时会自动执行`else`语句
- python的错误也是class，所有的错误类型都继承自`BaseException`
- 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```

`raise`：抛出错误实例

错误是class，捕获一个错误就是捕获到该class的一个实例。要抛出错误，可以定义一个错误的class，然后用`raise`语句抛出一个错误的实例

> `raise`语句如果不带参数就会把当前错误原样抛出

```python
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

**组合处理**：处理错误并抛出

捕获错误目的只是记录以便于后续追踪。当前函数不知道应该怎么处理该错误时就继续往上抛，让顶层调用者去处理错误

```python
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

## 调试

`assert`：用`print()`来辅助查看的地方都可以用断言`assert`来替代

- 断言失败`assert`语句本身就会抛出`AssertionError`
- 启动python解释器时可以用`-O`参数来关闭`assert`，关闭后所有的`assert`语句都当成`pass`

```python
def foo(s):
    n = int(s)
    # 表达式n != 0应该是True，否则根据程序运行的逻辑后面的代码会出错
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# 运行
python -O err.py
```



`logging`：用`print()`来辅助查看的地方都可以用`logging`来替代

`logging`不会抛出错误，但可以输出到文件

```python
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```



`pdb`：启动python的调试器pdb，让程序以单步方式运行

```
python -m pdb err.py
```

# 测试

## 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作

把多个测试用例放到一个测试模块里就是一个完整的单元测试

## 文档测试



# IO编程

`Input/Output`

**数据交换**的地方通常是磁盘、网络等，需要IO接口

CPU和内存的速度远远高于外设的速度，所以在IO编程中存在**速度不匹配**的问题

- 同步IO
- 异步IO

## 文件读写

在磁盘上读写文件的功能都是由**操作系统**提供的，现代操作系统不允许普通的程序直接操作磁盘

所以读写文件就是

1. **请求操作系统打开一个文件对象**（通常称为**文件描述符**）,`open()`
2. 通过操作系统提供的接口从这个文件对象中读取数据或者把数据写入这个文件对象



**读文件**

1. 调用`open()`方法以读文件的模式打开一个文件对象并传入文件名和标示符`r`（read）
   1. 读取二进制文件（例如图片、视频）用`'rb'`模式打开
   2. 读取非UTF-8编码的文本文件需要给`open()`函数传入`encoding`参数
2. 调用`read()`方法读取文件的全部内容到内存，用一个`str`对象表示
   1. 调用`readline()`每次读取文件的一行内容
   2. 调用`readlines()`一次读取文件的所有内容并按行返回`list`
3. 调用`close()`方法关闭文件

> 如果文件不存在，`open()`函数会抛出`IOError`错误，给出错误码和详细的信息告诉文件不存在
>
> `read()`会一次性读取文件的全部内容，如果文件太大会爆内存
>
> 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
>
> 默认读取UTF-8编码的文本文件

```python
f = open('/path/test.txt', 'r')

f.read()
f.close()

# 打开二进制文件
f = open('/path/test.jpg', 'rb')

# 打开GBK编码的文件
f = open('/path/test.txt', 'r', encoding='gbk')

# for循环
for line in f.readlines():
    print(line.strip()) 
```



`with()`

文件读写时都有可能产生`IOError`，一旦出错后面的`f.close()`就不会再调用。所以为了保证无论是否出错都能正确地关闭文件，可以使用`try...finally`来实现

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```

python引入了`with`语句来自动调用`close()`方法

```python
with open('/path/file', 'r') as f:
    print(f.read())
```

**file-like Object**

像`open()`函数返回的对象，它有`read()`方法，在python中统称为`file-like Object`。除了文件外还可以是内存的字节流，网络流，自定义流等

file-like Object不要求从特定类继承，只要有`read()`方法就可以



**写文件**

1. 调用`open()`方法以写文件的模式打开一个文件对象并传入文件名和标示符w（write）
2. 调用`write()`方法写内容到文件中（可以反复调用`write()`来写入文件）
3. 调用`close()`方法关闭文件

> 以`'w'`模式写入文件时，如果文件已存在则会直接覆盖（相当于删掉后新写入一个文件）。如果希望追加到文件末尾可以传入`'a'`（append）以追加模式写入
>
> 操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用`close()`方法时操作系统才保证把没有写入的数据全部写入磁盘。忘记调用`close()`的后果是数据可能只写了一部分到磁盘，剩下的丢失

```python
f = open('/path/test.txt', 'w')

# 写入Hello, world
f.write('Hello, world!')

f.close()
```

`with`

```python
with open('/path/test.txt', 'w') as f:
    f.write('Hello, world!')
```

## StringIO

在内存中读写`str`

写入`StringIO`

1. 创建一个`StringIO`
2. 像文件一样写入
3. `getvalue()`方法用于获得写入后的`str`

```python
from io import StringIO

f = StringIO()

f.write('hello')
f.write(' ')
f.write('world!')

# hello world!
print(f.getvalue())
```



读取`StringIO`

1. 用一个`str`初始化`StringIO`
2. 像读文件一样读取

```python
from io import StringIO

# 初始化,\n是换行
f = StringIO('Hello!\nHi!\nGoodbye!')

# Hello!
# Hi!
# Goodbye!
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
```

## BytesIO

在内存中读写`bytes`（二进制数据）

```python
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))

# b'\xe4\xb8\xad\xe6\x96\x87'
print(f.getvalue())


from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

# b'\xe4\xb8\xad\xe6\x96\x87'
f.read()
```



## 操作文件和目录

python内置的`os`模块可以直接调用操作系统提供的接口函数

- `os`模块的某些函数是跟操作系统相关的（在Windows上不提供`uname()`函数）
- 操作系统中定义的环境变量保存在`os.environ`变量

> - `posix`：`Linux`、`Unix`或`Mac OS X`系统
> - `nt`：`Windows`系统

```python
import os

# 操作系统类型,'nt'
os.name 

# 获取详细的系统信息
os.uname()

# 环境变量
os.environ

# 获取某个环境变量的值
os.environ.get('PATH')
```



**操作文件和目录**

操作文件和目录的函数一部分放在`os`模块中，一部分放在`os.path`模块中

- `os.mkdir()`：创建文件夹
- `os.rmdir()`：删除文件夹
- `os.rename`：文件重命名
- `os.remove`：删除文件
- `os.path.abspath('.')`：查看当前目录的绝对路径
- os.`path.join()`：合并路径
- `os.path.split()`：拆分路径
- `os.path.splitext()`：获取文件扩展名

> 合并路径时不要直接拼字符串而要通过`os.path.join()`函数，这样可以正确处理不同操作系统的路径分隔符
>
> 拆分路径时不要直接去拆字符串而要通过`os.path.split()`函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
>
> 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

```python
# 查看当前目录的绝对路径:'C:\\Users\\54164\\Desktop\\py'
os.path.abspath('.')

# 创建新目录之前把新目录的完整路径表示出来:'C:\\Users\\54164\\Desktop\\py\\testdir'
os.path.join('C:\\Users\\54164\\Desktop\\py', 'testdir')

# 然后创建新目录
os.mkdir('C:\\Users\\54164\\Desktop\\py\\testdir')

# 删掉目录
os.rmdir('C:\\Users\\54164\\Desktop\\py\\testdir')

# 拆分目录和文件路径:('/Users/michael/testdir', 'file.txt')
os.path.split('/Users/michael/testdir/file.txt')

# 获取文件扩展名:('/path/to/file', '.txt')
os.path.splitext('/path/to/file.txt')

# 对文件重命名
os.rename('test.txt','test.py')
# 删除文件
>>> os.remove('test.py')
```

## 序列化

`pickling`：变量从内存中变成**可存储**或传输的过程称之为**序列化**

`unpickling`：把变量从序列化的对象重新读到内存里称之为**反序列化**

> 序列化之后就可以把内容写入磁盘，或者通过网络传输到别的机器上

`pickle`

**序列化**

- `pickle.dumps()`：把对象序列化成一个`bytes`
- `pickle.dump()`：直接把对象序列化后写入一个`file-like Object`

**反序列化**

- `pickle.loads()`：反序列化出对象
- `pickle.load()`：从一个`file-like Object`中反序列化出对象

```python
import pickle

d = dict(name='Bob', age=20, score=88)
# 把一个对象序列化并写入文件:b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

# {'age': 20, 'score': 88, 'name': 'Bob'}
d
```

## JSON

在不同的编程语言之间传递对象必须把对象**序列化**为**标准格式**（比如XML，JSON)

- JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输
- JSON比XML更快，而且可以直接在Web页面中读取
- JSON表示的对象就是标准的JavaScript语言的对象
- JSON标准规定JSON编码是UTF-8

JSON和Python内置的数据类型对应如下：

| JSON类型   | Python类型 |
| :--------- | :--------- |
| {}         | dict       |
| []         | list       |
| "string"   | str        |
| 1234.56    | int或float |
| true/false | True/False |
| null       | None       |

`json`

python内置的`json`模块提供了Python对象到JSON格式的转换

> python的`dict`对象可以直接序列化为JSON的`{}`

**序列化**

- `json.dumps()`：返回一个`str`，内容是标准JSON格式
- `json.dump()`：把JSON写入一个`file-like Object`

**反序列化**

- `json.loads()`：把JSON字符串反序列化
- `json.load()`：从`file-like Object`中读取JSON字符串并反序列化

```python
import json

d = dict(name='Bob', age=20, score=88)

# '{"name": "Bob", "age": 20, "score": 88}'
json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

# {'age': 20, 'score': 88, 'name': 'Bob'}
json.loads(json_str)
```

**进阶**

用`class`表示对象，然后再序列化

正常情况类的实例对象不是一个可序列化为JSON的对象

`dumps()`方法的可选参数`default`就是把任意一个对象变成一个可序列为JSON的对象

通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，用来存储实例变量

先将实例转换为`dict`，再序列化

```python
print(json.dumps(s, default=lambda obj: obj.__dict__))
```

# 进程和线程

对于操作系统

- `Process`：操作系统的一个任务就是一个进程
- `Thread`：进程内的一个子任务就是一个线程

多任务实现：

- 多进程模式
- 多线程模式
- 多进程+多线程模式

> python既支持多进程又支持多线程

## 多进程

**Unix/Linux**提供了`fork()`系统调用

`fork()`调用一次，返回两次，因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回。子进程永远返回`0`，而父进程返回**子进程的ID**

> 普通的函数调用调用一次返回一次
>
> 一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，子进程调用`getppid()`可以拿到父进程ID
>
> 有了`fork`调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务。常见的Apache服务器就是由父进程监听端口，每当有新的http请求时就fork出子进程来处理新的http请求



`fork`

python的`os`模块封装了`fork`系统调用

>  **Only works on Unix/Linux/Mac**



`multiprocessing`

`Process`

`multiprocessing`是**跨平台版本**的**多进程模块**，提供了一个`Process`类来代表一个进程对象

> Windows没有`fork`调用，`multiprocessing`其实是**模拟**`fork`的效果，父进程所有python对象都必须通过`pickle`序列化再传到子进程去

创建子进程（`Process`实例）时，只需要传入一个执行函数`target`和函数的参数`args`

- `start()`：启动进程
- `join()`：等待子进程结束后再继续往下运行，通常用于进程间的同步

```python
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s:%s...' % (name, os.getpid()))

    
# Parent process 15696.
# Child process will start
# Run child process test:3004...
# Child process end
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # Process类
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    # 启动一个子进程并等待其结束
    p.start()
    p.join()
    print('Child process end')
```



`Pool`

需要启动大量的子进程的时候可以用**进程池**`Pool`的方式批量创建子进程

> `Pool`的默认大小是CPU的核数

对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用`join()`之前必须先调用`close()`，调用`close()`之后就不能继续添加新的`Process`了

```python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s:%s...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s' % os.getpid())
    # 批量创建子进程
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
```

### 子进程

`subprocess`

`subprocess`模块可以启动一个子进程，然后控制其输入和输出

`subprocess.call()`：调用

`communicate()`：输入

```python
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

### 进程通信

`multiprocessing`

`multiprocessing`模块包装了底层机制，提供了`Queue`、`Pipes`等多种方式来交换数据

`Queue`

- `put()`
- `get()`

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue,并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw,写入:
    pw.start()
    # 启动子进程pr,读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```

## 多线程

线程是操作系统直接支持的执行单元。多任务可以由多进程完成，也可以由一个进程内的多线程完成

- python的线程是真正的`Posix Thread`，而不是模拟出来的线程
- python标准库提供了两个模块：绝大多数情况下只需要使用`threading`高级模块
- - `_thread`：低级模块
  - `threading`：高级模块，对`_thread`进行了封装
- 任何进程默认会启动一个主线程（`MainThread`），主线程可以启动新子线程（子线程的名字在创建时指定）
- `threading`模块中的`current_thread()`函数会返回当前的线程实例

> 启动一个线程就是把一个函数`target`传入并创建`Thread`实例，然后调用`start()`开始执行

```python
import time, threading

# 新线程
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s : %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

wo