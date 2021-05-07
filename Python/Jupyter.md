# Jupyter

可以直接通过浏览器运行代码，同时在代码块下方展示运行结果

> Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果

组成部分

- 网页应用

  基于网页形式的、结合了编写说明文档、数学公式、交互计算和其他富媒体形式的工具。

  **网页应用是可以实现各种功能的工具。**

- 文档

  Jupyter Notebook中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是**以文档的形式体现**的

  这些文档是保存为后缀名为`.ipynb`的`JSON`格式文件。也可以导出为HTML、LaTeX、PDF等格式



# 安装

> 前提：安装python

## anaconda安装

> Anaconda自动安装了Jupter Notebook及其他工具，还有python中超过180个科学包及其依赖项

```bash
conda install jupyter notebook
```

## pip安装

1. 把pip升级到最新版本

   - Python 3.x

   ```bash
   pip3 install --upgrade pip
   ```

   - Python 2.x

   ```bash
   pip install --upgrade pip
   ```

2. 安装Jupyter Notebook

   - Python 3.x

   ```bash
   pip3 install jupyter
   ```

   - Python 2.x

   ```bash
   pip install jupyter
   ```

# 运行

在终端中输入，默认启动端口：8888

```bash
# 默认启动
jupyter notebook

# 指定端口号启动
jupyter notebook --port <port_number>

# 启动服务器但不打开浏览器
jupyter notebook --no-browser
```

- 执行命令之后终端中将会显示一系列notebook的服务器信息，同时浏览器将会自动启动Jupyter Notebook，没有启动自己输入http://localhost:8888
- 如果**同时**启动了多个Jupyter Notebook，由于默认端口"8888"被占用，因此地址栏中的数字将从"8888"起，每多启动一个Jupyter Notebook数字就加1
- 在Jupyter Notebook的所有操作，都要保持终端**不要关闭**

# 修改配置文件

进入Notebook主页面

**修改Jupyter Notebook的文件存放路径**

1. 创建目录后复制目录路径

2. 获取配置文件所在路径

   ```bash
   jupyter notebook --generate-config
   ```

   这条命令可以用于查看配置文件所在的路径，但主要用途是**是否将这个路径下的配置文件替换为默认配置文件**

   > 若文件已经存在或被修改，使用这个命令之后会出现询问"用默认配置文件覆盖此路径下的文件吗？"，按"y"则完成覆盖（之前所做的修改都将失效）
   >
   > 如果只是为了查询路径，那么一定要输入"N"

   

   一般情况下，配置文件所在路径和配置文件名如下：

   - Windows：`C:\Users\user_name\.jupyter\`
   - Linux/macOS：`/Users/user_name/.jupyter/` 或 `~/.jupyter/`
   - 配置文件名：`jupyter_notebook_config.py`

   > **.**开头的目录都是隐藏文件，通过`ls -a`命令查看

3. 修改配置文件

   1. 打开配置文件

      ```bash
      vim ~/.jupyter/jupyter_notebook_config.py
      ```

   2. 查找关键词

      输入`/c.NotebookApp.notebook_dir`（`/`符号和关键字`c.NotebookApp.notebook_dir`），再回车，光标切换到文中被关键词首字母

   3. 编辑配置文件

      光标定位在第二个单引号上（光标定位在哪个字符，就在这个字符前开始输入），把复制的路径粘贴在此处

   4. 取消注释

      把该行首的`#`删除。

      > 因为配置文件是Python的可执行文件，在Python中`#`表示注释，编译过程中不会执行该行命令，所以为了使修改生效，需要删除`#`

4. 验证

   在终端中输入命令`jupyter notebook`重新打开Jupyter Notebook



# 使用

现有的文件可以通过勾选文件的方式，对选中文件进行复制、重命名、移动、下载、查看、编辑和删除

也可以根据需要，在“New”下拉列表中选择想要创建文件的**环境**



> 右上角`new`中的python版本和anaconda的版本有关，下载python3就是python3
>
> 新建python3后右上角会显示python3

## Files

![file主页面](Jupyter.assets/file主页面.png)

### 笔记本

![笔记本](Jupyter.assets/笔记本.png)

**笔记本重命名**

- 在左上方“Jupyter”的图标旁有程序默认的标题“Untitled”，点击“Untitled”然后在弹出的对话框中输入自拟的标题，点击“Rename”即可
- 在“Files”界面勾选需要重命名的文件，点击“Rename”然后直接输入自拟的标题即可

 

**笔记本的两种模式**

1. **命令模式**

   按`esc`进入命令模式

   将**键盘命令**与Jupyter Notebook**笔记本命令**相结合，可以通过不同键的组合运行笔记本的命令

   命令模式下**单元格边框为灰色，左侧边框线为蓝色粗线条**

   ![命令模式](Jupyter.assets/命令模式.png)

2. **编辑模式**
   按`enter`或`return`键进入编辑模式

   编辑模式使用户可以在单元格内编辑代码或文档

   编辑模式下**单元格边框和左侧边框线均为绿色**

   ![编辑模式](Jupyter.assets/编辑模式.png)

### 单元格

中间部分称为**单元格**

- 退出本单元格（退出编辑）：`esc`
- 单元格中换行：`enter`
- 执行单元格
  - 执行本单元格：`ctrl+enter`
  - 执行本单元格并向下建立一个新的单元格：`shift+enter`
  - 点击**运行**按钮
- 选中单元格操作
  - 在上方加一个空白单元格：`a`
  - 在上方加一个空白单元格：`b`
  - 删除本单元格：`dd`
- 标记：修改为标记格式，前面`In`消失，可以输入代码注释，运行即可



## Running

`Running`页面主要展示的是当前正在运行当中的终端和`ipynb`格式的笔记本

若想要关闭已经打开的终端和`ipynb`格式的笔记本，仅仅关闭其页面是无法彻底退出程序的，需要在`Running`页面点击其对应的`Shutdown`

## Conda

Conda页面主要是Jupyter Notebook与Conda关联之后对**Conda环境和包**进行直接操作和管理的页面工具

![conda](Jupyter.assets/conda.png)

## Nbextension

Nbextensions页面提供了多个Jupyter Notebook的插件

主要使用的插件有nb_conda，nb_present，Table of Contents(2)（为Markdown文档提供目录导航）

# 加载网站源代码

在Jupyter Notebook中直接加载指定网站的源代码到笔记本中

执行命令

```bash
# URL为指定网站的地址
%load URL
```



# 加载本地Python文件

在Jupyter Notebook中加载本地的Python文件并执行文件代码

执行命令

- 第一次执行是将本地的Python文件内容加载到单元格内。Jupyter Notebook会自动将`%load`命令注释掉（#），以便在执行已加载的文件代码时不重复执行该命令
- 第二次执行是执行已加载文件的代码

```bash
%load Python文件的绝对路径
```



# 直接运行本地Python文件

不想在Jupyter Notebook的单元格中加载本地Python文件，想要直接运行本地Python文件

执行命令：

```bash
%run Python文件的绝对路径

# 执行Python 3.x版本的代码
!python3 Python文件的绝对路径

# 执行Python 2.x版本的代码
!python Python文件的绝对路径
```

> `!python3`和`!python`属于 `!shell命令` 语法，即在Jupyter Notebook中执行shell命令的语法（在单元格中用英文感叹号`!`后接shell命令即可执行shell命令）
>
> 执行过程中将不显示本地Python文件的内容，直接显示运行结果



# 获取当前位置

在Jupyter Notebook中获取当前Jupyter Notebook中创建的**笔记本所在位置**的**绝对路径**

执行命令：

```bash
%pwd

!pwd
```

# 关闭笔记本和终端

想要退出终端或笔记本时，**关闭页面**是无法结束程序运行的

需要通过以下步骤将其完全关闭

1. 关闭笔记本（无法关闭终端）
   1. 进入`Files`页面
   2. 勾选想要关闭的`ipynb`笔记本
      - 正在运行的笔记本图标为绿色，后边标有`Running`
      - 已经关闭的笔记本图标为灰色
   3. 点击上方的黄色的“Shutdown”按钮
   4.  成功关闭笔记本
2. 关闭笔记本和终端
   1. 进入`Running`页面
      1. 第一栏是`Terminals`，即所有正在运行的终端
      2. 第二栏是`Notebooks`，即所有正在运行的`ipynb`笔记本
   2. 点击想要关闭的笔记本或终端的`Shutdown`按钮
   3. 成功关闭笔记本或终端



# 退出Jupyter Notebook

仅通过关闭网页是无法退出Jupyter Notebook的，因为打开Jupyter Notebook其实是启动了它的服务器

想要彻底退出Jupyter Notebook需要关闭它的服务器

需要在它启动的终端上按：

- Mac：`control c`
- Windows：`ctrl c`

> 终端上会提示："Shutdown this notebook server (y/[n])?" 
>
> 输入`y`即可关闭服务器，退出Jupyter Notebook