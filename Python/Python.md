# 简介

解释型语言

代码不能加密（解释型的语言发布程序必须把源码发布出去）

# 安装

> Python目前有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的

安装后有

- Python解释器（负责运行Python程序）
- 命令行交互环境
- 简单的集成开发环境

## Anaconda

Anaconda是一种为科学计算而生的Python发行版，利用conda来进行包package和各个版本environment的管理。常用的package已经默认安装numpy、pandas、scipy 等等

[Anaconda | The World's Most Popular Data Science Platform](https://www.anaconda.com/)

[anaconda | 清华大学开源软件镜像站](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)

使用python3.x版本

![Anaconda安装](Python.assets/Anaconda安装.png)



## python

命令行中输入python进入交互界面

> 注意勾上`Add Python 3.8 to PATH`
>
> 在命令提示符窗口输入python后提示版本信息说明Python安装成功

编写Python代码得到的是一个包含Python代码的以`.py`为扩展名的文本文件

运行代码需要Python解释器去执行`.py`文件

> 官方版本的解释器：CPython（C语言开发的，所以叫CPython）
>
> 在命令行下运行`python`就是启动CPython解释器，CPython用`>>>`作为提示符
>
> 
>
> IPython基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。IPython用`In [序号]:`作为提示符



# 基础语法

## 注释

- 单行注释：`#`
- 多行注释：`''' '''`

## 输入输出

- `input`：返回的数据类型是`str`，可以用`int()`函数来把`str`转换成整数

  ```python
  a = input('please enter your age: ')
  age = int(a)
  ```

- `print`：依次打印每个字符串，遇到`,`会输出一个空格

  ```python
  # 输出Hello world
  print("Hello","world")
  ```

### 格式化输出

**%**

**在字符串内部**

- `%s`：表示字符串
- `%d`：表示整数
- `%f`：表示浮点数

> `%s`会把任何数据类型转换为字符串，用`%%`来表示一个`%`

有几个`%`占位符，后面就跟几个变量或者值（顺序要对应），如果只有一个`%`，括号可以省略

```python
# % 'world' 表示变量
>>> 'Hello, %s' % 'world'                   		   
'Hello, world'

>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)		多个%用（）
'Hi, Michael, you have $1000000.'
```



**.format**

用传入的参数依次替换字符串内的占位符`{0}`、`{1}`……

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)		#用.调用
'Hello, 小明, 成绩提升了 17.1%'
```



**f-string**

字符串如果包含`{xxx}`，就会以对应的变量替换：

```python
>>> r = 2.5
>>> s = 3.14 * r ** 2
>>> print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62
```

`{r}`被变量`r`的值替换，`{s:.2f}`被变量`s`的值替换，并且`:`后面的`.2f`指定了格式化参数（即保留两位小数），因此，`{s:.2f}`的替换结果是`19.62`。



## 数据类型

Python允许在数字中间以`_`分隔

- `10_000_000_000`和`10000000000`是一样的
- 十六进制数也可以写成`0xa1b2_c3d4`



## 编码

### 思想

计算机只能处理数字，如果要处理文本就必须先把文本转换为数字才能处理。Unicode字符集把所有语言都统一到一套编码里（用两个字节表示一个字符），这样就不会再有乱码问题了。

把Unicode编码转化为“可变长编码”的`UTF-8`编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。

内存中，统一使用Unicode编码，保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

Python源代码也是一个文本文件，当源代码中包含中文时，就要指定保存为UTF-8编码。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

```bash
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

### 字符

单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符：

```python
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

### 字符串

Python 3版本中，字符串是以Unicode编码的，所以Python的字符串支持多语言。

字符串的类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`。`bytes`类型的数据用带`b`前缀的单引号或双引号表示：

```python
x = "ABC"	#str的一个字符对应若干个字节
x = b'ABC'	#bytes的每个字符都只占用一个字节。
```

以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`

```python
>>> 'ABC'.encode('ascii')
b'ABC'

>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'

>>> '中文'.encode('ascii')	#会报错，因为中文超出了ascii码的范围（0-127）
```

如果从网络或磁盘上读取了字节流的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法

```python
>>> b'ABC'.decode('ascii')
'ABC'

>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

### 不可变对象

对于不变对象来说，调用对象自身的任意方法也不会改变该对象自身的内容。这些方法会创建新的对象并返回，这样就保证了不可变对象本身永远是不可变的。

```python
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b						#replace方法创建了一个新字符串'Abc'并用变量b指向该新字符串
'Abc'
>>> a						#a是变量，而'abc'才是字符串对象
'abc'					
```



### 字符串操作

#### 切割

将一个字符串切割成一些单词，你可以使用` split()`方法：

```python
delimiter = '-'      	#分隔符默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
t = s.split(delimiter)  #指定单词之间的分隔符作
```

#### 拼接

join()方法将一个字符串列表的元素拼接起来。需要一个分隔符调用它，并传入一个列表作为参数

```python
delimiter = '-'        
s = delimiter.join(t)	#用-拼接列表t中的元素
```

#### len函数

计算`str`包含多少个字符
计算`byte`包含多少个字节
计算`list`元素的个数



## 列表list[ ]

列表list是内置数据类型，是一种有序的集合a[ ]，里面元素可以改变(可变对象)。

list里面的元素的数据类型也可以不同,甚至可以是一个list，但是list计算时候只算一个元素个数。如果里面包含新的list时候，相当于一个二维的数组。

如果一个list中一个元素也没有，就是一个空的list，它的长度为0。

## 参数

list的[]中有三个参数，用冒号分割

list[param1:param2:param3]

param1，相当于start_index，可以为空，默认是0

param2，相当于end_index，可以为空，默认是list.size

param3，步长，默认为1。步长为-1时，返回倒序原序列

### 创建

创建一个元素都为0的列表：

```python
>>>l = 10
>>>lis = [0]*l
>>>lis
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### 索引

从0开始，到len()-1结束。

索引可以从后面开始取。[-1]是倒数第一个，[-2]是倒数第二个......

### 添加append

```python
>>> classmates.append('Adam')	#追加元素到列表末尾
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

### 插入insert

```python
>>> classmates.insert(1, 'Jack')	#插入元素到列表指定位置
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

### 删除pop

```python
>>> classmates.pop()	#删除列表末尾元素
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']

>>> classmates.pop(1)	#删除列表指定位置元素
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

pop()修改列表，并返回被移除的元素。如果你不提供下标，它将移除并返回最后一个元素。

pop()是返回被删除的对应下标的元素
del()是直接删除对应下标的元素
remove()是直接删除对应元素

### 赋值

```python
a = [1, 2, 3]
b, c, d = a		# 相当于b,c,d依次获得了列表a的各个元素
print(b,c,d)	# 变量数要和a内的元素个数相同才可以
1, 2, 3			# 可以写a[0:3]之类的来改变个数
```

### 替换

```python
>>> classmates[1] = 'Sarah'		#直接赋值即可
>>> classmates
['Michael', 'Sarah', 'Tracy']
```

## 拼接

```python
list1.extend(list2)  	# 把list2中的所有元素追加到list1中 

list1 += list2  		# 把list2中的所有元素追加到list1中 

list1 = list1 + list2 	# 把list2中的所有元素追加到list1中 

list[-1:] = list2		# 把list2中的所有元素追加到list1中
```

**拓展**:

```python
list1 = list("111")			#字符串被分为一个个字符
[‘1’, ‘1’, ‘1’]				

list1.append(["2","3","4"])	#append()的参数会作为一个元素追加到列表
[‘1’, ‘1’, ‘1’, [‘2’, ‘3’, ‘4’]]

list1.extend("234")			#extend()的参数是可迭代对象,会遍历后追加到列表
[‘1’, ‘1’, ‘1’, ‘2’, ‘3’, ‘4’]

list1[-1:-1] = "234"		#列表的末尾不是-1而是None,-1往后移动一位
[‘1’, ‘1’, ‘2’, ‘3’, ‘4’, ‘1’]

list1[:] = ["2","3","4"]	#[:]相当于重新定义列表元素，指向到"="右侧可迭代对象的所有元素
[‘2’, ‘3’, ‘4’]
    
list1[5:5] = "234"			#列表的切片不会越界，追加到最后
[‘1’, ‘1’, ‘1’, ‘2’, ‘3’, ‘4’]

list1[-1] = "234"			#重新定义了列表最后一个元素的指向
[‘1’, ‘1’, ‘234’]
```



## 元组tuple( )

元组是有序列表，但tuple一旦初始化就不能修改。因此定义一个tuple时里面的元素就必须被确定下来

当tuple中有list元素时候，list中元素可以改变

```python
>>> t = ()		#空的tuple 
>>> t = (1,)	#只有1个元素的tuple,会用,和运算符（1）区分。显示时也会加，
```



用一组tuple表示学生名字和成绩：

```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]	
#一组就是一个列表，列表里面的元素是tuple
#访问列表元素时，i[0]表示取的值为tuple里第一个元素；i[1]表示tuple里第二个元素
```



## 字典dict{ }

字典`dict`使用哈希表实现，键`key`必须是可哈希的`hashable`，`dict`的`key`必须是不可变对象，可变类型在哈希时可能映射成别的值，无法正确工作。所以列表`list`不能作为键`key`，只能作为值`value`。

`dict`需要占用大量的内存，内存浪费多，是用空间来换取时间的一种方法(相比于`list`)

```python
dictt['on'] = 'no'<-->{'on': 'no'}  #dictt[key]就是value，对dictt[key]操作就是对value操作
```

#### 查找

字典dictionary使用键-值`key-value`存储，字典中项`item`的顺序是不可预知的，字典中的元素不使用整数索引来索引，而是用键`key`来查找对应的值`value`。

字典使用哈希`Hash`算法。这种算法具备的特性： 无论字典中有多少项`item`，`in`运算符搜索所需的时间都是一样的。而列表list中in操作符随着列表的增长搜索时间成正比增长。

**get() 方法**

接受一个`key`和一个默认值作为参数，如果字典中存在该`key`，则返回`key`对应`value`。否则返回传入的默认值，对`dict`不影响。

```python
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
```



#### 存储

这种`key-value`存储方式在放进去的时候，必须根据`key`算出`value`的存放位置，这样取的时候才能根据`key`直接拿到`value`。

`dict`内部存放的顺序和`key`放入的顺序是没有关系的

一个`key`只能对应一个`value`，多次对相同`key`放入`value`只保存最后一次存入的`value`。

```python
>>> d['Adam'] = 67		#通过key存放k-v
67
>>> d['Adam'] = 154
154
>>> d['Adam']			#保存最后一次存入的154
154
```



#### 删除

要删除一个key，用`pop(key)`方法，对应的value也会从dict中删除：

```python
>>> d.pop('Bob')		#键值对'Bob': 75被删除
75
```



## set

`set`可以看成数学意义上的无序和无重复元素的集合。

`set`的原理和`dict`一样，所以不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证`set`内部“不会有重复元素”。

`set`是一组`key`的集合，但不存储`value`。由于`key`不能重复，所以在`set`中没有重复的元素，传入重复的元素在set中会被自动过滤。

#### 创建

创建一个set需要提供一个list作为输入集合

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}					#显示的顺序也不表示set是有序的
```



#### 添加

通过`add()`方法可以添加元素到set中，可以重复添加，但不会显示。

```python
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```



#### 删除

通过`remove()`方法可以删除元素

```python
>>> s.remove(4)
>>> s
{1, 2, 3}
```



## 条件判断

只要是非零数值、非空字符串、非空list等，就判断为`True`

缩进是4个空格

```python
if a:
    a
elif b:		#注意:
    b 
else:
    c
```



## 循环

### range

`range()`函数可以生成一个整数序列，再通过`list()`函数可以转换为`list`。

```python
>>> list(range(5))		#默认从0开始
[0, 1, 2, 3, 4]
```

range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。

range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

### for循环

把每个元素代入变量`x`，依次把`list`或`tuple`中的每个元素迭代出来,

```python
names = ['Michael', 'Bob', 'Tracy']
for x in names:			#这里面x是元素，不是下标
    print(x)
```

如何设置i从2开始循环



### while循环

```python
while a:		
    a
```



### break

`break`语句可以提前退出循环。

### continue

`continue`语句可以跳过当前的这次循环，直接开始下一次循环。



# 函数

## 调用函数

函数名其实就是指向一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

```python
>>> a = abs	    # 变量a指向abs函数
>>> a(-1) 		# 所以也可以通过a调用abs函数
1
```



## 定义函数

使用`def` 函数名、括号、括号中的参数和冒号`:`，函数的返回值用`return`语句返回。

如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`。`return None`可以简写为`return`。

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```



## 空函数

如果想定义一个什么事也不做的空函数，可以用`pass`语句

```python
def nop():	#可以用来暂存还未完成的函数
    pass
```



## 返回值

Python函数可以返回多个值。但多个值其实返回的是一个tuple。
在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值。

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
    
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```



## 函数参数

### 位置参数

调用函数时，传入的值按照括号中位置顺序依次赋给参数x,n

```python
def power(x, n):	#第一个是x,第二个是n
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```



### 默认参数

将常用或默认的参数值直接写在函数中可以简化函数的调用当传入的数据与默认参数不符合时，在传入实际值。

```python
def power(x, n=2):		#调用power(5)相当于调用power(5, 2)
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

**注意：**

- 必选参数在前，默认参数在后。

- 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

- 有多个默认参数时，调用的时候，可以按顺序提供默认参数，也可以不按顺序提供部分默认参数，但要写清楚参数名和对应值。

  

**定义默认参数必须指向不变对象(如str,None)**

如果在函数体里面执行了会改变默认参数的值的操作就会引发错误。

对象不变多任务环境下同时读取对象不需要加锁，同时也不会有读问题。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。



### 可变参数*args(turple)

传入的参数个数是可变的，可以是0，1，2个到任意个。

正常情况，我们需要将多个参数组装成`list`或者`turple`。在参数前面加了一个`*`号,参数numbers接收到的就是一个`tuple`。

```python
def calc(*numbers):		
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

>>> calc(1, 2)
5
>>> calc()
0
```

在`list`或`tuple`前面加一个`*`号，也可以把`list`或`tuple`的元素变成可变参数。

```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```



### 关键字参数**kw(dict)

关键字参数就是传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个`dict`。

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
```

也可以先组装出一个`dict`，然后用`**`该`dict`转换为关键字参数传进去

`**extra`表示把`extra`这个`dict`的所有`key-value`用关键字参数传入到函数的`**kw`参数，`kw`获得的`dict`是`extra`的一份拷贝，对`kw`的改动不会影响到函数外的`extra`。

```python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```



在函数内部通过关键字参数`kw`检查传入了哪些参数。

```python
def person(name, age, **kw):	#检查是否有city和job参数
    if 'city' in kw:		    # 有city参数
        pass
    if 'job' in kw:				# 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```



### 命名关键字参数*

因为关键字参数`key-value`的传入不受限制，如果想限制关键字参数的名字，就可以用命名关键字参数。

命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

```python
def person(name, age, *, city, job):	#只接收city和job作为关键字参数
    print(name, age, city, job)

>>> person('Jack', 24, city='Beijing', job='Engineer') #命名关键字参数必须传入参数名
Jack 24 Beijing Engineer
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了：

```
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
    
```

命名关键字参数具有默认值时，调用可不传入此参数

```python
def person(name, age, *, city='Beijing', job):		#city具有默认值
    print(name, age, city, job)
    
>>> person('Jack', 24, job='Engineer')	
Jack 24 Beijing Engineer
```



**组合**（可变参数+关键字参数）

对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。



## 递归函数

使用递归函数需要注意防止`栈溢出`。在计算机中，函数调用是通过栈`stack`这种数据结构实现的，每当进入一个函数调用栈就会加一层`栈帧`，每当函数返回栈就会减一层栈帧。由于栈的大小不是无限的，所以递归调用的次数过多会导致栈溢出。

解决递归调用栈溢出的方法是通过`尾递归`优化。
尾递归是指在函数返回的时候调用自身，并且return语句不能包含表达式。这样编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次都只占用一个栈帧，不会出现栈溢出的情况。



# 高级特性

## 切片slice

切片操作符`[n:m]`：返回从第n个元素到第m个元素的`list`或`turple`(包括第一个，但不包括最后一个)

字符串`'str'`也可以看成是一种`list`，每个元素就是一个字符。因此字符串也可以用切片操作，操作结果仍是字符串

取前3个元素

```python
>>> L[0:3]		
['Michael', 'Sarah', 'Tracy']
```

第一个索引是`0`，可以省略

```python
>>> L[:3]		#省略第一个索引，切片将从列表头开始。
['Michael', 'Sarah', 'Tracy']
```

倒数切片，倒数第一个元素的索引是`-1`,倒数第二个是`-2`

```python
>>> L[-2:]		#省略第二个索引，切片将会到列表尾结束
['Sarah', 'Tracy']
>>> L[-2:-1]
['Sarah']
```

取出某一段元素

```python
L[:10]		#取前10个元素
L[-10:]		#取后10个元素
L[10:20]	#前11-20个元素		
```

间隔取元素

```python
>>> L[:10:2]	#前10个数，每两个取一个：
>>> L[::5]		#所有数，每5个取一个：
```

复制一个`list`

```python
L[:]	#什么都不写
```



## 迭代iteration

通过`for`循环来遍历`list`或`tuple`，这种遍历称为迭代`Iteration`。

### 可迭代对象iterable

可迭代对象都可以作用于`for`循环，包括自定义的数据类型，只要符合迭代条件就可以使用`for`循环。

通过`collections`模块的`Iterable`类型判断一个对象是不是可迭代对象`iterable`

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable)   # str可迭代
True
>>> isinstance([1,2,3], Iterable) # list可迭代
True
>>> isinstance(123, Iterable)     # 整数不可迭代
False
```

**dict**

默认情况下`dict`迭代的是`key`
迭代`value`可以用`for value in d.values()`
迭代`key`和`value`可以用`for k, v in d.items()`

注意：
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
```

**字符串**

迭代每一个字符

```python
>>> for ch in 'ABC':
...     print(ch)
```

**下标迭代**

使用`enumerate`函数可以把一个`list`变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)		#0 A	1 B		2 C

```



## 列表生成式comprehensions

避免繁琐的循环

```python
>>> [x * x for x in range(1, 11)]					#for前面可以写生成式
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> L = ['Hello', 'World', 'IBM', 'Apple']			#for前面可以写函数，但元素必须可以调用函数
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']

>>> [x if x % 2 == 0 else -x for x in range(1, 11)]	#for循环前面可以写if表达式，要加上else
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

>>> [x * x for x in range(1, 11) if x % 2 == 0]		#for循环后面可以写if筛选条件，不加else
[4, 16, 36, 64, 100]

>>> [m + n for m in 'AB' for n in 'XYZ']			#两层for循环
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ']

>>> [k + '=' + v for k, v in d.items()]				#用多个变量生成list
['y=B', 'x=A', 'z=C']
```



## 生成器generator

如果`list`元素可以按照某种**算法**推算出来，那就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的`list`，从而节省大量的空间。这种**一边循环一边计算**的机制称为生成器：`generator`。

### 创建

**列表创建**

只要把一个列表生成式的`[]`改成`()`，就创建了一个`generator`

```python
>>> L = [x * x for x in range(5)]
>>> L
[0, 1, 4, 9, 16]
>>> g = (x * x for x in range(5))
>>> g
<generator object <genexpr> at 0x1022ef630>		#并不会显示
```

**函数创建**

如果推算的算法比较复杂，用类似列表生成式的`for`循环无法实现的时候，还可以用函数来实现。
在函数中用`yield`关键字代替`return`就是一个`generator`

```python
def fib():
    n, a, b = 0, 0, 1
    while true:
        yield b					#将return改为yield
        a, b = b, a + b			#是给a,b同时赋值
        n = n + 1
    return 'done'
```

**函数创建的`generator`和函数的执行流程不一样**
调用时首先要生成一个`generator`对象，在每次调用`next()`的时候执行，遇到`yield`语句返回。再次执行时从上次返回的`yield`语句处继续执行，当没有`yield`可以执行时候再调用`next()`就会报错。

```python
def odd():
    print('step 1')
    yield 1				#yield代替了return,odd()是一个generator
    print('step 2')
    yield 2
    print('step 3')
    yield 3

>>> o = odd()		#生成generator对象
>>> next(o)			#调用next()函数
step 1
1
>>> next(o)			#从上一个停止的yield处开始
step 2
2
>>> next(o)			#再next()就会报错
step 3
3
```

### 读取

`list`创建的`generator`使用`for`循环读取，因为`generator`也是**可迭代对象**

```python
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)		#0	1	4	9	16
```

`for`循环调用generator时得不到`generator`的return语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中

```python
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
>>> g = fib(3)

g: 1
g: 1
g: 2
Generator return value: done
```



`generator`保存的是**算法**，每次调用`next(g)`就计算出`g`的下一个元素的值直到最后一个元素，当没有更多的元素时抛出`StopIteration`的错误

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
```



## 迭代器iterator

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`。

可以使用`isinstance()`判断一个对象是否是`Iterator`对象

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```



生成器`generator`都是`Iterator`对象，但`list`、`dict`、`str`虽然是可迭代对象`Iterable`，却不是迭代器`Iterator`。

把`list`、`dict`、`str`等可迭代对象`Iterable`变成迭代器`Iterator`可以使用`iter()`函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```





# 函数式编程

## 高阶函数

### Map

`map()`函数接收两个参数，一个是函数，一个是可迭代对象`Iterable`。
`map()`将传入的函数**依次作用到序列的每个元素**，并把结果作为新的迭代器`Iterator`返回。

```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```



### Reduce

**from functools import reduce**

`reduce()`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数（本次运算的结果和序列的下一个元素）来计算累积结果。（`map()`是单独作用在每一个元素上）

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

**举例**：

把`str`转换为`int`的函数

```python
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]		#返回key对应的value
...
>>> reduce(fn, map(char2num, '13579'))
13579
```

### Filter

`filter()`是一个“筛选”函数，用于过滤序列。

`filter()`接收一个函数和一个序列。把**传入的函数**依次作用于**每个元素**，然后根据**返回值**是`True`还是`False`决定保留还是丢弃该元素。

在一个`list`中删掉偶数只保留奇数

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))		# 结果: [1, 5, 9, 15]
```

`filter()`函数返回的是一个迭代器`Iterator`，也就是一个惰性序列（仅仅在迭代至某个元素时才计算该元素），所以要强迫`filter()`完成计算结果需要用`list()`函数获得所有结果并返回`list`。



```python
def _odd_iter():							# 构造一个从3开始的奇数序列	
    n = 1					
    while True:
        n = n + 2
        yield n								# 惰性,返回3,调用next()才会继续算n+2,返回5

def _not_divisible(n):						# 筛选函数,
    return lambda x: x % n > 0				# lambda可以理解为一个函数生成器,返回的是一个函数
											# :之前的是输入, :之后的是输出
						
def primes():	
    yield 2									# 生成器
    it = _odd_iter()						# 初始序列从1，3开始，后面的到next()调用再计算
    while True:
        n = next(it) 						# 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) 	# 利用filter()不断产生筛选后的新的序列。

for n in primes():							# 打印1000以内的素数:
    if n < 1000:
        print(n)
    else:
        break
```



### Sorted

两个字符串或者`dict`直接比较数学上的大小是没有意义的，比较的过程必须通过函数抽象出来。

`sorted()`函数是一个**升序**排序函数，它还可以接收一个`key`函数来实现自定义的排序,`key`指定的函数将作用于`list`的每一个元素上，并根据`key`函数返回的结果进行排序。

```python
>>> sorted([36, 5, -12, 9, -21], key=abs)	# 按绝对值大小排序
[5, 9, -12, -21, 36]						# key是作用于每一个元素上面！
```



默认情况下对字符串排序是按照ASCII的大小比较的，由于`'Z' < 'a'`，大写字母`Z`会排在小写字母`a`的前面。

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```



进行反向排序，不必改动`key`函数，可以传入第三个参数`reverse` = True

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```



## 返回函数

### 嵌套函数（Nested Function）

函数可以做参数外，还可以作为结果返回。#返回的函数并不会立刻执行

```python
def lazy_sum(*args):			# *可变参数，传入的多个参数组装成一个tuple()
    def sum():					# 在外部函数lazy_sum中又定义了内部函数sum
        ax = 0					# 内部函数sum可以引用外部函数lazy_sum的参数args和局部变量
        for n in args:
            ax = ax + n
        return ax
    return sum					# 返回函数sum
>>> f = lazy_sum(1, 3, 5, 7, 9)	# 当我们调用lazy_sum()时返回的并不是求和结果而是函数sum
>>> f()							# 调用函数f()时才真正计算求和的结果
25
```



```python

```

**注意**：

当我们调用`lazy_sum()`时，每次调用都会返回一个新的函数，即使传入相同的参数，

```python
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1 == f2		# f1()和f2()的调用结果互不影响。
False	
```



### 闭包（Closure）

闭包`Closure`是词法闭包`Lexical Closure`的简称，是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外(返回的内部函数在其定义内部引用了外部函数的局部变量。)，闭包使得局部变量在函数外被访问成为可能。

闭包就像一个封闭的包裹，里面包裹着自由变量，就像在类里面定义的属性值一样，自由变量的可见范围随同包裹，哪里可以访问到这个包裹，哪里就可以访问到这个自由变量。

返回闭包时牢记：**返回函数不要引用任何循环变量或者后续会发生变化的变量**

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():			# 每次循环，都创建了一个新的函数
             return i*i		# 使用了外部变量i
        fs.append(f)		
    return fs				

f1, f2, f3 = count()		
>>> f1()					# 返回的函数引用了变量i，但它并非立刻执行
9							# 等到3个函数都返回时，它们所引用的变量i已经变成了3
>>> f2()					# 所以都是9
9
>>> f3()
9							
```



如果要引用循环变量，就要再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变。

```python
def count():
    def f(j):				# 用参数j绑定循环变量i
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) 	# f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```



## 匿名函数

有时传入函数不需要显式地定义函数，直接传入匿名函数会更方便。

匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数









## 装饰器

## 偏函数



