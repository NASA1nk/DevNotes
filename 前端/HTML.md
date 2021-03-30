[TOC]



# HTML5

#  简介

超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage。（超文本：包括文字，图片，音频，视频，动画等）

- 标记语言是一套**标记标签** (markup tag)

- HTML使用标记标签来**描述**网页

- HTML文档包含了**HTML标签**（HTML tag）及**文本内容**

- HTML文档也叫做 **web 页面**

```html
<!--
HTML标签是由尖括号<>包围的关键词<html>
HTML标签通常是成对出现的<标签>内容</标签>
一个HTML元素包含了开始标签与结束标签
HTML标签对大小写不敏感,通常小写
-->
```

## VSCode编写HTML文档

VSCode 安装 `open in browse`插件，输入`！`出现模板

快捷键`Alt + B` 在默认浏览器下打开页面了

快捷键 `Shift + Alt + B` 可以选择其他浏览器打开

```html
<!-- HTML5声明 -->
<!DOCTYPE html>
<html lang="en">
<!-- head标签-网页头部 -->
<head>
    <!-- meta标签-描述信息 -->
    <meta charset="UTF-8"> 
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- title标签-网页标题 -->
    <title>Document</title>
</head>
<!-- body标签-网页主体 -->
<body>
    
</body>
</html>

<!--
<!doctype>或者<!DOCTYPE>用于声明HTML的版本（浏览器正确显示网页内容）	
meta描述标签，后面+键值对
只有<body></body>区域会在浏览器中显示（网页主体）
-->
```

# HTMl元素

HTML文档由相互**嵌套**的HTML元素构成。

语法：

- HTML元素以**开始标签**起始，**结束标签**终止
- 某些 HTML 元素具有**空内容（empty content）**
- 空元素**在开始标签中进行关闭**（以开始标签的结束而结束）
- 大多数 HTML 元素可拥有**属性**

```html
<!--
<br>就是没有关闭标签的空元素
在开始标签中添加斜杠是关闭空元素的正确方法 <br/>
-->
```

# HTML属性

- HTML 元素可以设置**属性**
- 属性可以在元素中添加**附加信息**
- 属性一般描述于**开始标签**
- 属性总是以`名称/值`对的形式出现

```html
<!--
属性值应该始终被包括在引号内。
双引号是最常用的，不过使用单引号也没有问题
如果属性本身含有双引号，必须使用单引号
属性和属性值对大小写不敏感，尽量小写
-->
```

属性实例

| 属性  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| class | 为html元素定义一个或多个类名（classname）(类名从样式文件引入)<br />**class=" "** （引号里面可以填入多个class属性） |
| id    | 定义元素的唯一id<br />**id=" "**（只能填写一个，多个无效）   |
| style | 规定元素的行内样式（inline style）                           |
| title | 描述了元素的额外信息 (作为工具条使用)                        |

# HTML基础

快捷键：标签字母+Tap

## 标题

浏览器会自动地在**标题**的前后添加空行。

```html
<!-- 1-6级标题(1到6号标题与1到6号字体逆序对应) -->
<h1></h1>
...
<h6></h6>
```

## 段落

浏览器会自动地在段落的前后添加空行（`</p>` 是块级元素）

段落的行数依赖于浏览器窗口的大小

```html
<p></p>

<!-- 段落中也可以插入换行 -->
<p> <br/> <br/> </p>
```

## 换行

```html
<br/>

<!-- 用pre标签可以控制空格和空行 -->
<pre></pre>
```

### 行内元素

不独占一行

- span
- a
- img
- strong

### 块元素

无论内容多少，该元素单独占一行

- h1~h6
- p
- div
- ul li

**行内元素可以包含在块元素里，块元素无法包含在行内元素里**

## 水平线

```html
<hr>
<hr/>
```

## 注释

快捷键：CTRL+/

```html
<!-- 这是一个注释 -->
```

## 链接

链接可以是一个字，一个词，也可以是一幅**图像**，可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。（鼠标指针移动到网页中的某个链接上时，箭头会变为一只小手）

在标签`<a> `中使用了`href`属性来描述链接的地址。

```html
<a href=""></a>
<a href="oath" target="目标窗口位置">链接文本或图像</a>
```

### target属性

- target="_self" 表示在本窗口打开链接（默认）

- target="_blank" 表示在新窗口打开链接

### 存放图像标签

```html
<a href="">
	<img src="" alt="">
</a>
```

### 锚链接

使用#实现页面内和页面间的跳转

```html
<!-- 用a标签的name属性作为标记，使用#来跳到标记 -->
<a name="top">顶部</a>
<a href="#top">回到顶部</a>
```

### 邮件链接

mailto:邮箱地址

```
<a href="mailto:541640794@qq.com">点击联系我</a>
```

### 引用和引入

- href是HyperText Reference的缩写,表示超文本引用,用来建立当前元素和文档之间的链接
- src是Source的缩写，src的内容是页面必不可少的一部分，表示引入。src指向的内容会嵌入到文档中当前标签所在的位置

## 图像

图像格式：JPG,GIF,PNG,BMP(位图)

```html
<img src="" alt="">
<!-- src,alt属性必填 -->
<img src="path" alt="text" title="text" width="x" height="y" />

<!--
src:图像地址（路径）
	推荐用相对路径 ../表示上一级目录
alt:图像的替代文字（图片加载失败时）
title:鼠标悬停时提示文字
width:宽度
height:高度
-->
```

# HTML文本

格式化标签

```html
<!--
如<b>("bold")与<i>("italic")对输出的文本进行格式(加粗和斜体)
可以用标签<strong>替换加粗标签<b>来使用,<em>替换<i>标签使用

含义不同:
<b>与<i>定义粗体或斜体文本。
重要的文本应该用 <strong> 标签表示,被强调的文本应该用 <em> 标签表示
-->
```

## 实例

一般用strong和em

| 标签   | 描述                          |
| ------ | ----------------------------- |
| i      | 斜体                          |
| b      | 粗体                          |
| strong | 重要文本(粗体)                |
| em     | 强调文本（斜体）（emphasize） |
| big    | 大号字体                      |
| small  | 小号字体                      |
| sub    | 下标                          |
| sup    | 上标                          |
| ins    | 插入文本（下划线）            |
| del    | 删除文本（划掉）              |

## 缩写

把鼠标移至缩略词语上时，`<abbr>` 标签的 `title` 属性可被用来展示缩写词/首字母缩略词的完整版本。

```html
<abbr></abbr>

<abbr title="etcetera">etc.</abbr>
```

## 文字方向

bdo 指的是 bidi 覆盖（Bi-Directional Override）

```html
<bdp></bdp>

<bdo dir="rtl">该段落文字从右到左显示。</bdo>
```

| 属性                                                | 值   | 描述     |
| :-------------------------------------------------- | :--- | :------- |
| [dir](https://www.runoob.com/tags/att-bdo-dir.html) | ltr  | 从左到右 |
|                                                     | rtl  | 从右到左 |

## 特殊符号

格式：`&`开头，`；`结尾

- 空格&nbsp;：`&nbsp;`

- 大于号&gt;：`&gt;`

- 小于号&lt;：`&lt;`

- 版权符号&copy;：`&copy;`

# 列表

## 有序列表

order list

```html
<ol>
    <li>java</li>	
    <li>python</li>
    <li>c++</li>
</ol>
<!--
1.
2.
3.
-->
```

## 无序列表

unorder list

```html
<ul>
    <li>java</li>	
    <li>python</li>
    <li>c++</li>
</ul>
```

## 自定义列表

define list

```html
<dl>
    <dt>语言</dt>
    <dd>java</dd>
    <dd>python</dd>
    <dd>C++</dd>
</dl>
<!--
dt:列表名称
dd:列表内容
-->
```

# 表格

table

## 行,列

- 行：tr

- 列：td

```html
<table border="1px">
    <tr>
        <td>1-1</td>
        <td>1-2</td>
    </tr>
    <tr>
        <td>2-1</td>
        <td>2-2</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td>3-2</td>
    </tr>
</table>
<!--
3行2列
border属性代表边框
-->
```

## 跨行，跨列

跨列`colspan`：将一行多列合并

```html
<table border="1px">
    <tr>
        <td colspan="2">1-1</td>
    </tr>
    <tr>
        <td>2-1</td>
        <td>2-2</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td>3-2</td>
    </tr>
</table>
<!--
colspan="2"代表第一行跨2列只有一列
-->
```

跨行`rowspan`：将一列多行合并

```html
<table border="1px">
    <tr>
        <td colspan="2">1-1</td>
    </tr>
    <tr>
        <td rowspan="2">2-1</td>
        <td>2-2</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td>3-2</td>
    </tr>
</table>
<!--
rowspan="2"代表第二列跨了2行
-->
```

跨行和跨列会将之前的空间存的数据**挤出去**

# 媒体

## 视频

video

```html
<video src="path"></video>

<!--controls表示播放选项  -->
<video src="" controls></video>

<!--autoplay表示自动播放  -->
<video src="" controls autoplay></video>
```

## 音频

audio

```html
<audio src=""></audio>

<!--controls表示播放选项  -->
<audio src="" controls></audio>

<!--autoplay表示自动播放  -->
<audio src="" controls autoplay></audio>
```

# 页面结构

| 元素    | 描述                                               |
| ------- | -------------------------------------------------- |
| header  | 页面头部区域内容（用于页面或页面中的一块区域）     |
| footer  | 页面底部区域内容（用于整个页面或页面中的一块区域） |
| section | 页面的一块独立区域                                 |
| article | 文章内容                                           |
| aside   | 相关内容或应用（一般用于侧边栏）                   |
| nav     | 导航类辅助类容                                     |

```html
<header>
	<h2>网页头部</h2>
</header>
<section>
	<h2>网页主体</h2>
</section>
<footer>
	<h2>网页底部</h2>
</footer>
```

# iframe内联框架

```html
<iframe src="path" name="mainFrame" frameborder="0"  width="" height=""></iframe>
<!-- 
src:地址
name:框架标识名 
-->
```

B站分享-`嵌入代码`，就可以在网页看到相应视频

```html
<iframe src="//player.bilibili.com/player.html?aid=55631961&bvid=BV1x4411V75C&cid=97257967&page=11" 
        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```

# 表单

## form

常用于登录注册

```html
<form action="" method=""></form>
```

- action：向哪里发送表单数据

- method：规定如何发送表单数据

  - get：可以在url中看到提交的信息（不安全），不能传输（提交）大文件

    ```
    ink.html?username=ink&password=123
    ```

  - post：不能在url中看到提交的信息，可以传输大文件

    ```
    可以在网页检查中由network(网络)的form data中看到
    ```

登录框

```html
<form action="ink.html" method="get">
    <p>名字：<input type="text" name="username"></p>
    <p>密码：<input type="password" name="password"></p>
    <p>
        <input type="submit">
        <input type="reset">
    </p>
</form>

<!--
    input type="text":文本输入框 
    input type="password":密码框(不显示内容)
	input type="submit":提交
	input type="reset":重置(清空表单)
	<p></p>中是块元素，所以提交和重置在一行中
-->
```

## input

上传形式都是name的值和内容

```html
<input type="text" name="" id="">
<!-- get方法也会将value,name信息追加到url后 -->
```

| 属性      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| type      | 指定元素类型：text(默认),password,radio,submit,reset,file,image,button |
| name      | 指定表单元素名称                                             |
| value     | 指定元素初始值，type为radio时必须指定值                      |
| size      | 指定表单元素初始宽度(单位：像素)，type为text或password时，宽度单位为字符 |
| maxlength | type为text或password时可以输入的最大字符数                   |
| checked   | type为radio或checkbox时，指定按钮是否被选中                  |

type：

- radio：单选，必须处于同一组（指定相同name），value表示单选框的值

- checkbox：多选，一般提交的数组会被组成数组（同样的键name）

  ​                    **默认值：checked**(单选多选都是)

- range：滑动

- button：按钮，value表示按钮上的文字，submit和reset都是普通按钮，

  ​				image是图片按钮（src指定路径）。

- file：文件域

- email：自动验证

- url：自动验证

- number：自动验证

- search：搜索（可以清空）

## select

列表框和下拉框

option：可选项，**默认值：selected**

```html
<p>国家:
    <select name="国家">
        <option value="China" selected>中国</option>
        <option value="US">美国</option>
        <option value="UK">英国</option>
    </select>
</p>
<!--
	select:列表框
	option:可选项
-->
```

## textarea

文本域：（文件域在input中）

- cols：列
- rows：行

```html
<p>反馈：
    <textarea name="textarea" id="" cols="30" rows="10">文本内容</textarea>
</p>
```

## lable

可以让文本锁定文本框，用for可以指向一个对应文本框的id

```html
<label for="mark">点击</label>
<input type="text" id="mark">
```

## 表单应用

默认值：

- 只读：readonly
- 禁用：disabled
- 隐藏：hidden (可用来传递默认值)

## 表单初级验证

常用方式：

- placeholder：提示信息(用于输入框中)

  ```html
  <input type="text" name="username" placeholder="请输入用户名">
  ```

- required：**默认值**，要求元素非空

  ```
  <input type="text" name="username" placeholder="请输入用户名" required>
  ```

- pattern：正则表达式