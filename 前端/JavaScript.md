<!-- TOC -->

- [JavaScript](#javascript)
  - [JavaScript框架](#javascript框架)
  - [UI框架](#ui框架)
  - [JavaScript构建工具](#javascript构建工具)
- [控制台调试](#控制台调试)
- [引入JavaScript](#引入javascript)
  - [内部标签](#内部标签)
  - [外部引入](#外部引入)
- [基本语法](#基本语法)
  - [定义变量](#定义变量)
  - [条件控制](#条件控制)
  - [alert](#alert)
  - [console.log](#consolelog)
  - [注释](#注释)
- [数据类型](#数据类型)
  - [number](#number)
  - [字符串](#字符串)
  - [数组[ ]](#数组-)
  - [对象{ }](#对象-)
  - [布尔值](#布尔值)
  - [逻辑运算](#逻辑运算)
  - [比较运算符](#比较运算符)
  - [Null和undefined](#null和undefined)
- [strict模式](#strict模式)
- [字符串](#字符串-1)
  - [转义字符](#转义字符)
  - [多行字符串](#多行字符串)
  - [模板字符串](#模板字符串)
- [数组](#数组)
  - [数组长度](#数组长度)
  - [数组遍历](#数组遍历)
  - [方法](#方法)
- [对象](#对象)
  - [动态增删属性](#动态增删属性)
  - [属性判断](#属性判断)
- [流程控制](#流程控制)
  - [if判断](#if判断)
  - [while循环](#while循环)
  - [for循环](#for循环)
- [Map，Set](#mapset)
  - [Map](#map)
  - [Set](#set)
  - [iterator遍历](#iterator遍历)
- [函数](#函数)
  - [函数定义](#函数定义)
  - [调用函数](#调用函数)
    - [不传参数](#不传参数)
    - [多个参数](#多个参数)
- [变量作用域](#变量作用域)
  - [变量作用域提升](#变量作用域提升)
  - [全局变量](#全局变量)
  - [局部变量](#局部变量)
  - [常量const](#常量const)
- [解构赋值](#解构赋值)
- [方法](#方法-1)
  - [定义方法](#定义方法)
  - [this](#this)
  - [that](#that)
  - [apply](#apply)
- [内部对象](#内部对象)
  - [标准对象](#标准对象)
  - [Date](#date)
  - [JSON](#json)
    - [数据类型](#数据类型-1)
    - [格式](#格式)
    - [转换](#转换)
- [面向对象](#面向对象)
- [BOM](#bom)
  - [浏览器内核](#浏览器内核)
  - [BOM对象](#bom对象)
- [DOM](#dom)
  - [获得DOM节点](#获得dom节点)
  - [更新DOM节点](#更新dom节点)
    - [操作文本](#操作文本)
    - [操作CSS](#操作css)
  - [删除DOM节点](#删除dom节点)
  - [插入DOM节点](#插入dom节点)
- [表单](#表单)
  - [操作表单](#操作表单)
  - [表单提交和验证](#表单提交和验证)
- [jQuery](#jquery)
  - [获取jQuery](#获取jquery)
  - [jQuery公式](#jquery公式)
  - [jQuery选择器](#jquery选择器)
  - [jQuery事件](#jquery事件)
    - [页面载入](#页面载入)
    - [鼠标事件](#鼠标事件)
  - [jQuery操作DOM](#jquery操作dom)
    - [DOM节点文本操作](#dom节点文本操作)
    - [DOM节点CSS操作](#dom节点css操作)
    - [DOM元素操作](#dom元素操作)
    - [Ajax](#ajax)

<!-- /TOC -->
# JavaScript

弱类型**脚本语言**，源代码不需要编译，由**浏览器解释**运行。用于控制网页行为

原生JS开发按照`ECMAScript`标准（JS的一种规范），简称ES

- ES5：所有浏览器都支持
- ES6：主流版本，`webpack`打包成ES5支持

> JavaScript 的创造者Netscape公司将JavaScript 提交给国际标准化组织ECMA，希望这种语言能够成为**国际标准**。次年ECMA 发布262号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为ECMAScript，这个版本就是1.0版
>
> 该标准从一开始就是针对 JavaScript 语言制定的

## JavaScript框架

- `Angular`（模块化开发）
- `React`（虚拟DOM）
- `Vue`（结合以上2种）

`jQuery`（库）

## UI框架

- `Ant-Design`

- `ElementUI`（基于Vue）

  `vue-element-admin`

- `Bootstrap`

- `AmazeUI`

## JavaScript构建工具

- `Babel`
- `WebPack`

# 控制台调试

可以设置断点，刷新重新运行，右侧有调试信息

- `Elements`：爬网站信息
- `Console`：调试JS
- `Source`：设置断点
- `Network`：抓包
- `Application`：查看网站cookie

![控制台调试](JavaScript.assets/%E6%8E%A7%E5%88%B6%E5%8F%B0%E8%B0%83%E8%AF%95.png)

# 引入JavaScript

文件目录格式

- js文件夹
  - script.js
- css文件夹
  - style.css
- images
- index.html

![新建JavaScript项目](JavaScript.assets/新建JavaScript项目.png)

![JavaScript目录](JavaScript.assets/JavaScript目录.png)

## 内部标签

`script`

JS代码写在`body`的最后

`<script type="javascript"></script>`不用定义`type`,默认是JS

```html
<body>
    <!-- script标签，写JS代码 -->
    <script>
        alert("hello world");
    </script>
</body>
```

## 外部引入

`<script src=""></script>`（不再是`link`）

```javascript
alert("hello world");
```

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/ink.js"></script>
</head>
```

# 基本语法

JavaScript**严格区分大小写**

JavaScript每个语句以**分号**结束，但是**JavaScript并不强制要求在每个语句的结尾加分号**

> 浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上分号。不要将`return`语句拆行写

## 定义变量

变量类型 变量名=变量值

**只有一种变量类型**`var`，所有定义都是`var`

> ES6中，局部变量用`let`定义

```javascript
var num = 1; // 变量名不能以数字或一些特殊符号开头
var 王者荣耀 = 倔强青铜;
```

## 条件控制

```javascript
if (condition){
	alert("1");
}
else if(){
    alert("2");
}
else{
    alert("3");
}
```

## alert

弹出（在控制台弹出变量时需要代码中有定义）

![alert](JavaScript.assets/alert.png)

## console.log

在浏览器的控制台打印变量（代码中需有定义）

相当于`System.out.println()`

![console.log](JavaScript.assets/console.log.png)

## 注释

- 单行注释：// + 空格
- 多行注释：/* */

# 数据类型

数值，文本，图形，音频，视频

## number

JavaScript**不区分浮点数和整数**，统一用`Number`表示

```javascript
// console控制台打印
123		// 整数
123.1 	// 浮点数
1.12e4	// 科学计数法
-99		// 负数
NaN		// not a number
Infinity	//无穷大
```

## 字符串

字符串是以单引号`'`或双引号`"`括起来的任意文本

```javascript
"abc"
'abc'
'\n'
```

## 数组[ ]

因为各种”类型“变量都是`var`，**所以数组中可以有各种“类型”**

```javascript
var arr = [1,2,3,"buaa",true,null]; //推荐[ ]
new Array(1,2,3,"buaa",true,null);
```

## 对象{ }

对象的内部属性是键值对`key-value`，每个属性用`，`隔开（最后一个不用）

对象的**键都是字符串类型**，**值可以是任意数据类型**

```javascript
var person = {
    name:"ink", 
    age:24,
    tags:["java","js"]
}
```

取对象值：

![对象](JavaScript.assets/%E5%AF%B9%E8%B1%A1.png)

## 布尔值

`true` `false`

```javascript
console.log(2>1)
true
```

## 逻辑运算

```javascript
&& 	 // 与
|| 	 // 或
！ 	// 非
```

## 比较运算符

**不要使用`==`，使用`===`**

- `==`：会自动转换数据类型再比较
- `===`：不会自动转换数据类型，如果数据类型不一致，返回`false`，如果一致再比较

```javascript
=   // 赋值
==  // 等于(类型不同，值相同也会判断为true)   "1" = 1
=== // 绝对等于(类型，值都相同才会判断为true)
```

**NaN**

- **NaN和所有数值都不相等，包括自己**。

- 只能通过`isNaN`方法判断这个数是否是NaN

![NaN](JavaScript.assets/NaN.png)

**浮点数比较**

- 尽量避免使用浮点数进行运算，会有精度问题
- 做差判断

![浮点数比较](JavaScript.assets/%E6%B5%AE%E7%82%B9%E6%95%B0%E6%AF%94%E8%BE%83.png)

## Null和undefined

- `Null`：表示一个“空”的值，它和`0`以及空字符串`''`不同
- `undefined`：表示**未定义**

# strict模式

**严格检查模式**

预防JavaScript随意性导致的安全问题，必须写在JavaScript的**第一行**

> ES6标准

```javascript
'use strict';
i = 1	// 局部变量用let定义，此时i会提示不规范
```

# 字符串

字符串：用`" "` `' '`包围，字符串不可变

字符串**长度**：`str.length`

## 转义字符

用`\`

​	`\'`

​	`\n`：换行

​	`\t`：制表符tab

```javascript
'use strict';
console.log('a\'');
console.log("a");
```

![转义字符](JavaScript.assets/%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6.png)



## 多行字符串

在**反引号``**之中即可（ESC下方）

![多行字符串](JavaScript.assets/%E5%A4%9A%E8%A1%8C%E5%AD%97%E7%AC%A6%E4%B8%B2.png)

```javascript
'use strict';
var str =`
    buaa
    nmb
    nlsde
`
alert(str)
```

## 模板字符串

要把多个字符串连接起来，可以用`+`号连接

ES6新增了模板字符串：`${变量}`

```javascript
'use strict';
let name = "ink";
let age = 24;
let msg = `你好,${name}`
console.log(msg)
```

![模板字符串](JavaScript.assets/%E6%A8%A1%E6%9D%BF%E5%AD%97%E7%AC%A6%E4%B8%B2.png)

# 数组

数组Array中可以有各种数据类型   

```javascript
// 一维数组,a[1]
var array = [1,2,3,4,"5","6"]
// 二维数组,a[1][1]
var array = [ [1,2],[3,4],["5","6"] ]
```

## 数组长度

`array.length`

注意：

数组长度`array.length`可以被赋值改变，此时数组也会发生变化

- 当数组变大时：用**未定义的empty**填充
- 当数组变小时，数组元素就会**丢失**

通过索引赋值时，索引超过了范围，同样会引起Array大小的变化：

![数组](JavaScript.assets/%E6%95%B0%E7%BB%84.png)

## 数组遍历

- `for of` ：输出数组值
- `for in` ：输出数组索引

```javascript
'use strict';
var arr = [3,4,5];
for (let x of arr){
    console.log(x)	// 3,4,5
}
for (let x in arr){
    console.log(x) // 0,1,2
}
```

## 方法

- `indexOf()`：通过元素获取下标索引
- `slice()`：截取数组的一部分（**包括开始索引，不包括结束索引**），返回一个新的数组，类似`substring()`，不传递参数则复制数组
- `push()`：向**数组尾部**添加一个元素
- `pop()`：弹出数组**尾部元素**（最后一个元素）
- `unshift()`：向**数组头部**添加一个元素
- `shift()`：弹出数组**头部元素**（第一个元素）
- `sort()`：排序（直接修改当前数组）
- `reverse()`：反转数组
- `concat()`：**拼接数组**，返回一个新的数组（并不修改原数组）
- `join()`：使用特定字符拼接数组，返回一个字符串
- `splice()`：**从指定的索引开始删除若干元素，然后再从该位置添加若干元素**

# 对象

对象是一种**无序的集合数据类型**，它由若干**键值对**（内部属性）组成，每个键值对用`，`隔开（最后一个不用）

**属性名（key）必须是一个有效的变量名**，如果属性名包含特殊字符，就必须用`''`括起来：

```javascript
'use strict';
var person = {
    name:"ink",
    age:23,
    school:"buaa",
    position:"nmb"
    'middle-school': 'No.1 Middle School'
}
```

对象赋值

```javascript
person.name = "inkk"
```

注意：

使用不存在的对象属性，不会报错，会提示undefined

![对象未定义属性](JavaScript.assets/%E5%AF%B9%E8%B1%A1%E6%9C%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.png)

## 动态增删属性

JavaScript的对象是**动态类型**

- `delete`：删除一个属性
- 直接定义一个属性(即添加)

![动态改变属性](JavaScript.assets/%E5%8A%A8%E6%80%81%E6%94%B9%E5%8F%98%E5%B1%9E%E6%80%A7.png)

## 属性判断

注意：**所有键key都是字符串，值value是任意类型**

- 判断属性是否在这个对象中

  `"key" in 对象名`

  `in`判断一个属性存在，**这个属性不一定是对象的，它可能是地对象继承得到的**（父类对象的属性）

  > 所有对象最终都会在原型链上指向`object`

- 判断属性是否是这个对象**自身拥有**

  `hasOwnProperty()`方法



![属性判断](JavaScript.assets/%E5%B1%9E%E6%80%A7%E5%88%A4%E6%96%AD.png)

# 流程控制

## if判断

```javascript
'use strict';
var age = 5;
if(age>3){
    alert("hhh");
}
else if(age<3){
    alert("jjj")
}
else{
    alert("ggg")
}
```

## while循环

```javascript
'use strict';
var age = 5;
while(age<10){
    age = age + 1
}
alert(age)
```

## for循环

注意：for循环中定义的let局部变量出循环后就无效了

```javascript
'use strict';
var age = 5;
for (let i = 0; i < 10; i++) {
    age = age + 1;
    alert(age)
}
```

# Map，Set

ES6新特性

## Map

`Map`是一**组**键值对的结构

- `get()`
- `set()`：增加，**一个key只能对应一个value**，多次对一个key放入value，后面的值会把前面的值**冲掉**
- `delete()`：删除

```javascript
'use strict';
// 初始化Map需要一个二维数组,或者初始化一个空Map
var m = new Map(); 
var map = new Map([["tom",100],["jack",95]]);
var stu = map.get("tom");
map.set("admin",90);
map.delete("tom")
console.log(stu);
```

![map](JavaScript.assets/map.png)

## Set

`Set`是一组key的集合，但不存储value。且在`Set`中，没有重复的key

> 无序！不重复！重复元素在`Set`中自动被过滤

- `add()`：增加，可以重复添加，但不会有效果
- `delete()`：删除元素
- `has()`：判断是否含有某个元素

```javascript
'use strict';
// 创建一个Set需要一个Array,或者直接创建一个空Set
var set = new Set([1,1,1,3]);
```

![set](JavaScript.assets/set.png)

## iterator遍历

遍历`Map`和`Set`无法使用下标

ES6标准引入了新的`iterable`类型，`Array`、`Map`和`Set`都属于`iterable`类型

具有`iterable`类型的集合可以通过for of`循环来遍历

> `for in`实际遍历的是对象的属性名称。一个`Array`数组实际上也是一个对象，它的每个**元素的索引**被视为一个属性，所以会有bug

最好使用`iterable`内置的`forEach`方法，它接收一个函数，每次迭代就自动回调该函数

> `forEach()`方法是ES5.1标准引入

`Map`的回调函数参数依次为`value`、`key`和`map`

```javascript
var m = new Map([[1,'x'], [2,'y'], [3,'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});
```

# 函数

**方法**：面向对象（属性，方法）

**函数**：面向过程

JavaScript的函数**可以像变量一样使用**

## 函数定义

`function`

- 执行到`return`结束
- 如果没有执行到`return`，函数会返回`undefined`（NaN）

**JavaScript的函数也是一个对象**。定义的函数实际上是一个**函数对象**，而函数名可以视为**指向该函数的变量**

```javascript
// 定义方式1
function abs(x){
    if (x>=0){
        return x;
    }
    else{
        return -x;
    }
}
// 定义方式2
// 这是一个匿名函数，将匿名函数赋值给了变量，变量abs就可以调用该函数
var abs = function(x){
    if (x>=0){
        return x;
    }
    else{
        return -x;
    }
};
// 按照完整语法需要在函数体末尾加一个;表示赋值语句结束
```

## 调用函数

JavaScript**可以传多个参数，也可以不传参数**

```javascript
abs(10)
10
abs(-10)
10
```

### 不传参数

参数`x`将收到`undefined`，计算结果为`NaN`

```javascript
// 返回NaN
abs();
// 添加判断，手动定义异常
if (typeof x !== 'number'){
    throw "Not a Number！"
}
```

![参数异常](JavaScript.assets/%E5%8F%82%E6%95%B0%E5%BC%82%E5%B8%B8.png)

### 多个参数

`arguments`

> `arguments`是JavaScript的一个关键字，包含传递进来的所有的参数(包括定义的参数)，**是一个数组**

`arguments.length`：获得传入参数的个数

```javascript
'use strict';
function abs(x){
    console.log("x=>"+x);
    for(let i = 0;i<arguments.length;i++){
        console.log(arguments[i]);
    }
    if (x>=0){
        return x;
    }
    else{
        return -x;
    }
}
```

![多个参数](JavaScript.assets/%E5%A4%9A%E4%B8%AA%E5%8F%82%E6%95%B0.png)

`rest`

`rest`包含传递进来的**除定义参数外的所有的额外参数**，是一个数组

`rest`参数只能写在最后，前面用`...`标识

```javascript
'use strict';
function test(a,b,...rest){
    console.log("a=>"+a);
    console.log("b=>"+b);
    console.log(rest);
}
```

![rest](JavaScript.assets/rest.png)

# 变量作用域

`var`定义的变量存在**作用域**

- **函数体内**声明的变量在函数体外不可以使用
- 不同的函数使用相同的变量名，只要在**函数内就不冲突**
- **内部函数可以访问外部函数的成员变量**，反之不行
- 函数查找变量从自身函数开始，由内向外查找（就近原则）

```javascript
// Uncaught ReferenceError: x is not defined
'use strict';
function a(){
    var x = 1;
    x = x + 1;
}
x = x+2

// 不同函数不冲突
function a(){
    var x = 1;
    x = x + 1;
}function b(){
    var x = 2;
}

// b()可以调用a中的x,但是a不能调用b中的y
function a(){
    var x = 1;
    function b(){
        var y = x + 1;
        console.log(y);
    }
    b();
}
a();
```

## 变量作用域提升

JavaScript的函数定义会**先扫描整个函数体的语句，把所有声明的变量“提升”到函数顶部**，但不会赋值

> JavaScript引擎自动提升

```javascript
// x undefined,说明y定义了但未赋值
'use strict';
function a(){
    var x = "x" + y;
    console.log(x);
    var y = "y";
}
a();
// 等价写法
function a(){
    var y;
    var x = "x" + y;
    console.log(x);
    y = "y";
}
```

## 全局变量

不在任何函数内定义的变量就具有**全局作用域**

1. JavaScript只有一个全局作用域`window`
2. 默认**所有的全局变量**（包括以**变量形式定义的函数**）都会自动绑定在`window`对象下
3. 任何变量（函数也视为变量）在没有函数作用范围找到时，就会向外查找，最终查找到`window`。如果`window`也没找到，就会报错`ReferenceError`

> `alert()`函数也是`window`变量

```javascript
'use strict';
var x = 1;
function a(){
    console.log(x);
}
a();
// 输出1 1
console.log(x); 

// window对象
'use strict';
var x = 1;
alert(x);
alert(window.x);
```



**由于所有的全局变量都会自动绑定在window对象下，那么多个JavaScript文件如果使用了相同的全局变量，就会冲突**

解决方法：`jQuery` `$`

定义唯一全局变量，把所有的代码全部绑定到一个全局变量中

```javascript
'use strict';
// 唯一全局变量all
var all = {};

all.name = 'ink';
all.add = function (a,b){
    return a+b;
}
```

## 局部变量

用`let`（替代`var`）可以申明一个**块级作用域**的变量

> ES6新特性

## 常量const

ES6引入`const`

`const`与`let`都具有**块级作用域**

> ES6之前：通常用全部大写的变量来表示“这是一个常量，不要修改它的值”

```javascript
'use strict';
const PI = 3.14;
console.log(PI);
PI = 3.1415 // Uncaught TypeError
```

# 解构赋值

JavaScript可以同时**对一组变量进行赋值**

> ES6开始引入解构赋值
>
> 在支持ES6解构赋值特性的浏览器中才能正常运行。

1. 对**数组元素**进行解构赋值时，多个变量要用`[]`括起来

   ```javascript
   'use strict';
   // x, y, z分别被赋值为数组对应元素
   var [x, y, z] = ['hello', 'JavaScript', 'ES6'];
   ```

2. 解构赋值可以**忽略某些元素**

   ```javascript
   // 忽略前两个元素，只对z赋值第三个元素
   let [, , z] = ['hello', 'JavaScript', 'ES6'];
   ```

3. 交换变量

   ```javascript
   var x=1, y=2;
   [x, y] = [y, x]
   ```

4. 给对象的**若干指定属性进行赋值**

   ```javascript
   'use strict';
   var person = {
       name: '小明',
       age: 20,
       gender: 'male',
       passport: 'G-12345678',
       school: 'No.4 middle school'
   };
   // name, age, passport分别被赋值为对应属性
   var {name, age, passport} = person;
   ```

5. 给**嵌套的对象属性**进行赋值

   如果对应的属性不存在，变量将被赋值为`undefined`

   可以使用默认值赋值，避免不存在的属性返回`undefined`

   ```javascript
   var person = {
       name: '小明',
       age: 20,
       gender: 'male',
       passport: 'G-12345678',
       school: 'No.4 middle school',
       address: {
           city: 'Beijing',
           street: 'No.1 Road',
           zipcode: '100001'
       }
   };
   // address不是变量，而是为了让city和zip获得嵌套的address对象的属性
   // name='小明',city='Beijing'
   var {name, address: {city, zip}} = person; 
   
   //zip=undefined,因为没有这个属性名
   
   // single会返回默认值true
   var {name, single=true} = person;
   ```



# 方法

**对象内部的函数就是方法**

对象

- 属性
- 方法

## 定义方法

```javascript
// 属性:person.name
// 方法:person.age()
'use strict';
var person = {
    name:'ink',
    birth:1997,
    // 方法
    age:function (){
        let now = new Date().getFullYear();
        return now - this.birth; //this代表当前对象
    }
}
```

## this

`this`是一个特殊变量

- 在一个方法内部，它始终指向**当前对象**
- 以对象的方法形式调用，该函数的`this`指向被调用的对象
- 单独调用`getAge()`函数，`this`就会指向全局对象`window`
- 保证`this`指向正确，必须用`obj.xxx()`的形式调用

> Java中`this`是无法指向的，默认指向调用它的人

```javascript
// 拆开写法
function getAge(){
    let now = new Date().getFullYear();
    return now - this.birth;
}

var person = {
    name:'ink',
    birth:1997,
    // 键值对:age = getAge() 
    age:getAge
}
// 正确写法
person.age();

// 错误写法
// 先拿到xiaoming的age函数
var fn = person.getAge; 
// NaN
fn(); 
```

## that

`this`指针只在对象的方法内指向对象，在函数内部定义的函数中`this`还是指向`undefined`

需要用`that`捕获`this`：`var that = this;`

> 在非strict模式下，它重新指向全局对象`window`

```javascript
'use strict';
var person = {
    name: 'ink',
    birth: 1997,
    age: function () {
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            // this获取不到当前对象
            return y - this.birth;
        }
        return getAgeFromBirth();
    }
};
// Uncaught TypeError: Cannot read property 'birth' of undefined
person.age();
```

`that`捕获

```javascript
'use strict';

var person = {
    name: 'ink',
    birth: 1997,
    age: function () {
    	// 在方法内部一开始就捕获this
        var that = this; 
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            // 用that
            return y - that.birth; 
        }
        return getAgeFromBirth();
    }
};
```

## apply

JavaScript中可以控制`this`的指向

所有函数都有`apply()`方法

`apply()`接收两个参数

- `this`：需要绑定的`this`变量
- `Array`：表示函数本身的参数

```javascript
'use strict';
function getAge(){
    let now = new Date().getFullYear();
    return now - this.birth;
}
var person = {
    name:'ink',
    birth:1997,
    age:getAge
};
```

![apply](JavaScript.assets/apply.png)

# 内部对象

## 标准对象

![标准对象](JavaScript.assets/%E6%A0%87%E5%87%86%E5%AF%B9%E8%B1%A1.png)

## Date

```javascript
var now=new Date();
// 方法
now.getFullYear();	// 年
now.getMonth();		// 月(0~11)
now.getDate();		// 日
now.getDay(); 		// 星期
now.getTime(); 		// 时间戳,全世界唯一

// 返回时间
console.log(new Date(时间戳)) 

// 返回本地时间(调用方法)
now.toLocalString()
```

## JSON

**JavaScript Object Notation**

json是一种轻量级的**数据交换格式**，**层次结构**简洁清晰，易于阅读编写，易于机器解析和生成，可以有效提升网络传输效率。

JavaScript中一切皆对象（定义一个函数function，它也是一个对象），**任何JavaScript支持的类型都可以用JSON表示**

> 早期数据传输习惯使用xml文件（重量级）,XML标记比数据多，增加了交换产生的流量
>
> BSON（Binary JSON）也是一种计算机数据交换格式，主要用于MongDB数据库，是一种二进制表示形式
>
> JavaScript内置了JSON的解析，在JavaScript中可以直接使用JSON

### 数据类型

- `number`：JavaScript的`number`
- `boolean`：JavaScript的`true`或`false`
- `string`：JavaScript的`string`
- `null`：JavaScript的`null`
- `array`：JavaScript的`array`
- `object`：JavaScript的`{ ... }`

> JSON的字符串必须用双引号`""`，object中的键也必须用双引号`""`

### 格式

- 对象用`{}`
- 数组用`[]`
- 所有键值对都是用`key：value`
  - key：string类型
  - value：任何基本类型或数据结构

> **首先一个{}，整个代表一个对象**
>
> JSON的字符集必须是UTF-8

- JSON：格式化的**字符串**

  ```javascript
  {"name": "ink", "age": 23, "school": "buaa"}
  ```

- JavaScript对象

  ```javascript
  var person = {name: "ink", age: 23, school: "buaa"}
  ```

### 转换

- 序列化`stringify()`：JavaScript对象转换为JSON字符串
- 反序列化`parse()`：JSON字符串转换为JavaScript对象

```javascript
'use strict';
// 逗号隔开(最后一个不用)
var person = {
    name:"ink",
    age:23,
    school:"buaa"
}
// person对象转换为json字符串
var jsonuser = JSON.stringify(person)

// json字符串转换为obj对象
// 注意：json字符串用"",外面就得用''
var obj = JSON.parse('{"name": "ink", "age": 23, "school": "buaa"}')
```

![json](JavaScript.assets/json.png)

# 面向对象

一般的面向对象，Java，C++

- 类：模板（抽象）
- 对象：实例（具体表现）

**在JavaScript中有些不同**

- 原型继承

  ```javascript
  // ink对象的原型是user对象
  ink.__proto__ = user
  ```

- class继承

  > class关键字是在ES6引入
  >
  > 本质还是查看对象原型

  ```javascript
  //定义类
  class user{
      // 构造器
      constructor(name){
          this.name = name;
      }
      hello(){
          alert('hello')
      }
  }
  var ink = new user("ink");
  
  // 继承
  class miniuser extends user{
      constructor(name,age){
          // 实现父类方法
          super(name);
          this.age = age;
      }
      myage(){
          alert(this.age);
      }
  }
  var youyu = new miniuser("ink",23);
  ```

![class](JavaScript.assets/class.png)

> 原型链：
>
> JavaScript中，每个函数都有一个prototype属性，这个属性指向函数的**原型对象**

![原型链](JavaScript.assets/原型链.png)

# BOM

浏览器对象模型BrowserObjectModel

> JavaScript就是为了让它在浏览器中运行（操作浏览器）

## 浏览器内核

- IE 6-12
- Chrom
- FireFox
- Safari

## BOM对象

- window：代表浏览器窗口
- Navigator：封装了浏览器的信息（可被人为修改，不建议使用）
- screen：代表全屏幕属性
- location：代表当前页面url信息（可被重定向）
- document：代表当前页面（可以获取具体的文档树节点，cookie）
- history：代表浏览器的历史记录（back后退，forward前进）

# DOM

文档对象模型`DocumentObjectModel`

> 整个浏览器网页就是一棵DOM树

操作**(需要先获得节点)**

- **更新DOM节点**
- **遍历DOM节点**
- **删除DOM节点**
- **添加DOM节点**

## 获得DOM节点

依靠css选择器，`document.getElementById`和`document.getElementsBy...`

> 因为id是唯一的，而ClassTame和TagName是会有相同的。所以一个是`getElement`，一个是`getElements`。
>
> `getElementById`返回一个dom对象，可以直接操作。`getElementsByClassName`返回一个dom数组，就要通过索引操作dom对象。

![doc](JavaScript.assets/doc.png)

原生代码，后面使用`JQuery`

```html
<body>
<div id = "div">
    <h1 class="h1">标题一</h1>
    <p class="p1">p1</p>
    <p id="p2">p2</p>
</div>
<script src="js/ink.js"></script>
</body>
```

```javascript
var di = document.getElementById("div");
var p = document.getElementsByTagName("p");
var h1 = document.getElementsByClassName("h1");
var p1 = document.getElementsByClassName("p1");
var p2 = document.getElementById("p2");
var dc = div.children;
```

![获取dom](JavaScript.assets/获取dom.png)

## 更新DOM节点

### 操作文本

- 修改Text文本值`innerText `

![修改Text文本值](JavaScript.assets/修改Text文本值.png)

- 解析HTML文本标签`innerHTML`

![解析HTML文本标签](JavaScript.assets/解析HTML文本标签.png)

### 操作CSS

- 属性使用字符串（"red"）
- 驼峰命名（fontSize）

![修改CSS](JavaScript.assets/修改CSS.png)

## 删除DOM节点

步骤：

1. 获取删除目标节点的**父节点**`parentElement`
2. 通过父节点删除目标节点

```javascript
var self = document.getElementById("p2");
var father = self.parentElement;
father.removeChild(self)
```

注意：

- `removeChild`要求是dom对象，所以id选择的可以直接操作,如果是class数组,就要写成p1[0]形式
- 删除多个数组节点的时候，dom对象数组是在动态变化的，下标一定要注意（比如3个节点，删了一个后，再用索引2就会报错）

![删除dom](JavaScript.assets/删除dom.png)

## 插入DOM节点

`innerText` 和`innerHTML`只适用于向**空**的dom节点中添加元素，**如果节点中存在元素，就会被覆盖**

- 创建节点：`createElement(tagName)`
- **追加**节点：
  - `append()`
  - `appendChild()`
  - `insertBefore(newNode,targetNode)`
- 设置属性：`setAttribute('key','value')`

```html
<body>
<p id="js">JavaScript</p>
<div id = "div">
    <p id="se">javase</p>
    <p id="ee">javaee</p>
    <p id="me">javame</p>
</div>
<script src="js/ink.js"></script>
</body>
```

```javascript
// 创建p标签
var n = document.createElement("p");
// 设置p标签的id属性
// 等价写法setAttribute('id','n');
n.id = n;
n.innerText = "Create new dom"
var js = document.getElementById("js");
var div = document.getElementById("div");
div.append(js);
div.appendChild(n);

// 创建script标签节点
var myscript = document.createElement('script');
//设置标签属性,相当于<script type="text/javascript"></script>
myscript.setAttribute('type',`text/javascript`);
div.appendChild(myscript);

// TagName返回的是一个dom数组
var body = document.getElementsByTagName('body')[0];
body.style.backgroundColor = '#319981';
```

![dom插入](JavaScript.assets/dom插入.png)

# 表单

> 在前端验证

表单`form`也是DOM树中的一个节点，用来**提交信息**

常见表单：

1. 文本框：input（text）
2. 下拉框：select
3. 多选框：input（checkbox）
4. 隐藏域：hidden
5. 密码框：input（password）

## 操作表单

```html
<body>
    <form action="#", method="post">
        <p>
            <span>用户名:</span> <input type="text", id="username">
        </p>

        <p>
            <span>性别:</span>
            <input type="radio", name="sex", value="man">男
            <input type="radio", name="sex", value="woman">女
        </p>

    </form>
    <script src="js/ink.js" ></script>
</body>
```

```javascript
// 获取输入框中的内容
var username = document.getElementById('username');
// 设置输入框中的内容
username.value = 'inkeee';

var sex = document.getElementsByTagName('input')[2]
```

![获取表单内容](JavaScript.assets/获取表单内容.png)



## 表单提交和验证

**正常代码，提交信息会被暴露**

```html
<body>
    <form action="post">
        <p>
            <span>用户名:</span> <input type="text", id="username", name= "username">
        </p>
        <p>
            <span>密码: </span> <input type="password", id="password", name= "password">
        </p>
        <!-- 绑定事件,onclick被点击时触发事件-->
        <button type="submit", onclick="f()">提交</button>

    </form>
    <script src="js/ink.js" ></script>
</body>
```

```javascript
function f() {
    alert("提交成功")
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    console.log(username.value);
    console.log(password.value);
}
```

![表单提交](JavaScript.assets/表单提交.png)

![抓包信息](JavaScript.assets/抓包信息.png)



**MD5加密，密码被加密**

> MD5工具类：
>
> https://cdn.bootcss.com/blueimp-md5/2.10.0/js/md5.min.js

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="css/style.css">
    <!-- MD5工具类-->
    <script src="https://cdn.bootcss.com/blueimp-md5/2.10.0/js/md5.min.js" ></script>
</head>
<body>
    <form action="post">
        <p>
            <span>用户名:</span> <input type="text", id="username", name= "username">
        </p>
        <p>
            <span>密码: </span> <input type="password", id="password", name= "password">
        </p>
        <!-- 绑定事件,onclick被点击时触发事件-->
        <button type="submit", onclick="f()">提交</button>

    </form>
    <script src="js/ink.js" ></script>
</body>
</html>
```

```javascript
function f() {
    alert("提交成功")
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    console.log(username.value);
    console.log(password.value);
    // MD5加密算法
    password.value = md5(password.value);
    console.log(password.value);
}
```

![md5加密](JavaScript.assets/md5加密.png)



**表单优化，隐藏原始密码**

```html
<body>
    <form action="post">
        <p>
            <span>用户名:</span> <input type="text", id="username", name= "username">
        </p>
        <p>
            <span>密码: </span> <input type="password", id="input-password">
        </p>
        <input type="hidden", id="md5-password", name="password">
        <!-- 绑定事件,onclick被点击时触发事件-->
        <button type="submit", onclick="f()">提交</button>

    </form>
    <script src="js/ink.js" ></script>
</body>
```

```javascript
function f() {
    alert("提交成功")
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var md5password = document.getElementById('md5-password');
    // 隐藏password
    md5password.value = md5(password.value);
    console.log(md5password.value);
}
```

![隐藏密码](JavaScript.assets/隐藏密码.png)



# jQuery

**jQuery库**：里面有大量封装好的JavaScript函数

`$`：代表jQuery

> 浏览器本身处理DOM也是有性能瓶颈的，尤其是在传统开发中，用JQuery或者原生的JavaScript DOM操作函数对DOM进行频繁操作的时候，**浏览器要不停的渲染新的DOM树**，导致页面看起来非常卡顿。

## 获取jQuery

1. 官网下载

   > jQuery官网：https://jquery.com/

   点开**保存**（ctrl+s）到项目`lib`目录下

   ![下载jQuery](JavaScript.assets/下载jQuery.png)

   ```html
   <body>
   <script src="lib/jquery-3.6.0.js"></script>
   </body>
   ```

2. 搜索**cdn jquery**

   复制所需要的jQuery版本的`script`标签即可

   https://www.bootcdn.cn/jquery/

   https://www.jq22.com/cdn/

   ```html
   <body>
   <!--cdn绑定-->
   <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js"></script>
   </body>
   ```



## jQuery公式

**选择器+事件**

`$(selector).action()`

> selector：CSS中的选择器



```html
<body>
<a href="", id="test-jQuery">点击</a>
<script src="lib/jquery-3.6.0.js"></script>
<script src="js/jQ.js"></script>
</body>
```

```javascript
// JavaScript正常写法
// var a = document.getElementById('test-jQuery');
// id.click(function ());

// jQuery写法
// CSS id选择器#
$('#test-jQuery').click(function (){
    alert('Hello jQuery');
})
```

![第一个jQuery程序](JavaScript.assets/第一个jQuery程序.png)



## jQuery选择器

**原生JavaScript**

- 标签选择器：`document.getElementsByTagName()`
- id选择器：`document.getElementById()`
- 类选择器：`document.getElementsByTagName()`

**jQuery**：能用CSS的所有选择器

- 标签选择器：`$('p').click()`
- id选择器：`$('#id').click()`
- 类选择器：`$('.class').click()`

> jQuery API文档：https://jquery.cuishifeng.cn/

![jQuery选择器](JavaScript.assets/jQuery选择器.png)

![jQuery选择器例](JavaScript.assets/jQuery选择器例.png)



## jQuery事件

- 鼠标事件
- 键盘事件
- 其他事件

![常用事件](JavaScript.assets/常用事件.png)



### 页面载入

**ready(fn)**

> ```javascript
> // 当网页元素加载完毕之后响应事件
> // 原始完整写法
> // $(document).ready(function (){
> //
> // })
> // 简便写法 $()
> ```

![ready事件](JavaScript.assets/ready事件.png)



### 鼠标事件

`mouse`

- 按下
- 移动

![鼠标选择器](JavaScript.assets/鼠标选择器.png)



**获取鼠标当前坐标**

```html
<body>
mouse: <span id="mouseMove"></span>
<div id="divMove">
    在这里移动鼠标
</div>
    
<script src="lib/jquery-3.6.0.js"></script>
<script src="js/jQ.js"></script>
</body>
```

```css
#divMove{
    width: 200px;
    height: 200px;
    border: 1px solid red;
}
```

```javascript
$(function (){
    $('#divMove').mousemove(function (e){
        $('#mouseMove').text('x: '+e.pageX+' '+'y: '+e.pageY);
    })
})
```

![鼠标事件](JavaScript.assets/鼠标事件.png)



## jQuery操作DOM

### DOM节点文本操作

```javascript
// 获得dom中内容
$('#test-ul li[name = python]').text();

// 设置dom中内容
$('#test-ul li[name = python]').text('设置内容');

$('#test-ul li[class = JavaScript]').html('<strong>JavaScript</strong>');
```

![操作dom](JavaScript.assets/操作dom.png)



### DOM节点CSS操作

传入**键值对**

> API文档

![jQuery操作css](JavaScript.assets/jQuery操作css.png)

```javascript
$('#test-ul li[name = python]').css({ "color": "#ff0011", "background": "blue" });
```

![jQuery操作CSS](JavaScript.assets/jQuery操作CSS-1618588254793.png)



### DOM元素操作

元素的显示和隐藏

本质：`display：none`

```javascript
// 显示
$('#test-ul li[name = python]').show();
$(window).width();

// 隐藏
$('#test-ul li[name = python]').hide();
```



### Ajax