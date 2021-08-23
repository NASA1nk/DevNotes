# Linux简介

1. Linux系统是一个多用户多任务的分时操作系统
2. Linux操作系统将所有的设备都看作文件，它将整个计算机的资源都整合成一个大的文件目录
3. Linux系统中用户是按组分类的，一个用户属于一个或多个组。文件所有者以外的用户又可以分为文件所有者的同组用户和其他用户。因此Linux系统按文件所有者、文件所有者同组用户和其他用户来规定了不同的文件访问权限

## 目录结构

/  			   根目录
├── bin   		存放用户二进制文件
├── boot  		存放内核引导配置文件
├── dev  		 存放设备文件
├── etc   		**存放系统配置文件**
├── home  		**用户主目录**
├── lib  		 动态共享库
├── lost+found    文件系统恢复时的恢复文件
├── media  	   可卸载存储介质挂载点
├── mnt   	   **文件系统临时挂载点**
├── opt   		附加的应用程序包
├── proc  		系统内存的映射目录，提供内核与进程信息
├── root  		root用户主目录
├── sbin  		存放系统二进制文件
├── srv   		存放服务相关数据
├── sys   		sys虚拟文件系统挂载点
├── tmp   		存放临时文件
├── usr  	 	存放用户应用程序
└── var  	 	存放邮件、系统日志等变化文件



## 修改root密码

1. 重启Linux系统主机

2. 在出现引导界面时，按下键盘上的`e`键进入内核编辑界面

3. 在`linux16`参数这行的最后面追加`rd.break`参数

4. 按下`Ctrl + X`组合键来运行修改过的内核程序 

5. ```bash
   mount -o remount,rw /sysroot
   chroot /sysroot
   passwd
   touch /.autorelabel
   exit
   reboot
   ```



# shell

- 内核
  - 系统软件，负责对硬件进行操作和管理
  - 用户无法和硬件和内核交流，需要通过应用程序或系统软件发出指令，指令会被传递和翻译给内核

- 命令解释器
  - shell是一个程序，是用户与Linux系统之间的可交互接口
  - 用户在命令行中输入命令，运行在后台的shell把命令翻译为指令代码发送给os

> 命令行接受用户输入并传递给shell，shell翻译给os

Linux的Shell有许多种，在`etc/shells`目录下指定了当前系统可用的shell

系统管理员可以为用户指定Shell。如果不指定Shell，Linux系统使用bash为默认的登录Shell（字段值为`/bin/bash`）

- sh(Bourne Shell)
- bash(Bourne Again Shell)
- csh(CShell)
- zsh(z-Shell)

## bash

- bash使用`$`作为提示符
- 在提示符之前还有一段信息：`用户名,主机名，当前目录`
- bash提供命令行补全（`tap`）
  - 按两次`tap`可以以列表的形式给出所有以键入字符开头的文件
- bash会自动记录历史命令
  - 用户执行的命令会在注销时自动记录到家目录下的`.bash_history`文件中
- 标准输入设备：键盘，鼠标
- 标准输出设备：屏幕（显示器）

### bash快捷键

- `ctrl+a`：光标移动到行首
- `ctrl+e`：光标移动到行尾
- `ctrl+u`：删除光标到行首之间的内容
- `ctrl+k`：删除光标到行尾之间的内容
- `ctrl+c`：终止进程
- `ctrl+z`：挂起进程（放入后台并暂停执行）
- `ctrl+w`：删除光标前一个单词（空格为分隔符）
- `alt+d`：删除光标后一个单词

> `jobs`命令可以查看挂起命令，`fg n`可以将挂起进程调入前台并执

### 交互式和非交互式

- **交互式模式**
  - shell与用户进行交互：shell等待用户的输入然后执行用户提交的命令

    > 登录、执行一些命令、签退（shell终止） 

- **非交互式模式**
  - shell不与用户进行交互：shell读取存放在文件中的命令然后执行，当shell读到文件的结尾时终止

### login和non-login

login shell与non-login shell的主要区别在于它们**启动时会读取不同的配置文件**，从而导致环境不一样

在终端桌面直接启动的shell窗口和在shell中使用`su`切换用户的窗口都属于non-login shell 

- **配置文件**
  - `/etc/profile`：系统的全局配置文件，为系统的每个用户设置环境信息（不建议修改）
  - `~/.bash_profile`、`~/.bash_login`、`~/.profile`：配置个人环境修改这三个配置文件

- **login shell**

  1. login shell启动时首先读取`/etc/profile`全局配置
  2. 然后依次查找`~/.bash_profile`、`~/.bash_login`、`~/.profile`三个配置文件，并且**只读取第一个找到的并且可读的文件**
  3. login shell退出时读取并执行`~/.bash_logout`中的命令

  > 登录终端输入账号和密码取得的bash就是login shell

- **non-login shell**
  - 进入了login shell后输入`bash`就会进入一个non-login shell
  - 交互式non-login shell启动时只读取`~/.bashrc`配置文件
  - 非交互式non-login shell不读取上述的所有配置文件，而是**查找环境变量**`BASH_ENV`，读取并执行`BASH_ENV`**指向的文件中的命令**

> 所以su切换用户是不会读取`/etc/profile`配置文件的，也就不会改变环境变量等

### .bashrc

> The individual per-interactive-shell startup file.

`~/.bashrc`配置文件用于交互式non-login shell

- `/etc/bashrc`：为每一个运行bash shell的用户执行该文件
- `~/.bashrc`：**专用于某个用户**的bash shell的个性化设置信息，当该用户登录时以及每次打开新的shell时读取该文件
  - 个性化设置如命令别名、路径、**环境变量**等

一般会在`~/.bash_profile`文件中显式调用`~/.bashrc`

1. 为了加载用户首选项，bash在每次启动时首先会去读取`~/.bash_profile`文件

2. 这样`~/.bashrc`配置文件中的内容也得到执行，个性化设置也就生效了

3. 修改`~/.bashrc`后会在下次启动终端时应用，也可以执行`source`让它立即生效

   ```bash
   source ~/.bashrc
   ```




## 命令别名alias

简化指令

```bash
# 查看系统当前所有别名
alias

# 定义别名
alias h5 = 'head -5'

# 取消别名
unalias h5
```



## 通配符

`*`，`？`，`[]`

- `*`
  - 匹配任意长度的字符串
  - `ls *.cpp`
- `?`
  - 匹配一个字符
  - `ls text?`
- `[]`
  - 匹配出现在方括号中的字符，可以使用`-`来指导字符集范围
  - `ls text[1A]`
  - `ls text[1-3]`

## 输出重定向

- 标准输出的文件描述符：`1`
- 错误输出的文件描述符：`2`
- 输出重定向符：`>`，`>>`

- 标准输出（`stdout`）：程序默认输出结果的地方（屏幕）

**输出重定向**

将程序的结果输出到文件中

- 文件不存在
  - 创建文件并写入内容
- 文件存在
  - `>`：覆盖内容
  - `>>`：追加内容

> shell的高级特性
>
> `>`其实是`1>`
>
> 每个程序在运行后，都会至少打开三个文件描述符，分别是
>
> - 0：标准输入
> - 1：标准输出
> - 2：标准错误

```bash
# 将ls结果重定向到ls.txt文件中
ls > ls.txt

# 将主机名追加到ls.txt文件中
hostname >> ls.txt

# 当abc不存在时，错误信息不会重定向到error.txt文件中
ls -l abc install.log > error.txt

# 当abc不存在时会报错，将错误信息重定向到error.txt文件中，但正确时信息不会重定向
ls -l abc install.log 2> error.txt

# 将正常信息和错误信息都重定向到error.txt文件中
# &1表示文件描述符1
ls -l abc install.log > all 2>&1
```

## 输入重定向

- 标准输入的文件描述符：`0`
- 输入重定向符：`<`

- 标准输入（`stdin`）：程序默认接受输入的地方（键盘）

**输入重定向**

- 让程序从文件中读取输入内容
- 立即文档（`<<`）
  - 从shell中接受输入并传递给程序
  - 代表输入结束的分隔符`EOF`

```bash
# 发送邮件，内容来自list.txt
mail -s text 123@gmial.com < list.txt
```



## 管道

`|`

- 管道可以将一条命令的输出作为另一条命令的输入



## 变量

- **定义变量**
  - `name=value`
  - value未指定则赋值为空字符串
- 调用变量
  - `$name`
- **使用范围**
  - 默认只在当前shell中有效
  - 子进程不会继承变量
    - 使用`export`可以将变量放入环境中，这样子进程会从父进程中获取变量

### 环境变量

`export`可以直接定义环境变量并赋值，也可以将普通的用户变量转换为环境变量

BASH预设了很多环境变量

- `HOSTNAME`：当前主机名称
- `PWD`：当前工作目录
- `HOME`：当前用户家目录
- `PATH`：命令搜索路径
  - 命令所在目录的集合

### PATH

- 在linux中输入命令的时候，命令的查找是根据**环境变量**中的**搜索路径**`PATH`来查找的

- 不可以直接对PATH进行赋新的值，否则会覆盖现有值

  - 需要在原有的基础上引入旧值，再添加新值

  - `PATH = $PATH:/root`

    > `PATH = /root`则以前的路径都被覆盖了

- 上述修改并没有通过写入文件的方式永久保存到环境变量，所以退出终端后重新登录就会复原

# 常用命令

命令的本质是可执行文件，可以在`usr/bin`目录下找到

## 用户和版本信息

### who

查看系统中的登录用户及工作的控制台

### whoami

查看当前登录的用户身份

### uname

`unix name`：显示系统信息

- `-a (--all)`：显示全部的信息
- `-r (--release)`：显示操作系统的发行编号（linux内核版本）
- `-m (--machine)`：显示电脑的处理器架构
- `-n (--nodename)`：显示在网络上的主机名称
- `-s (--sysname)`：显示操作系统名称
- `-v`：显示操作系统的版本和时间

## 查看目录和文件

### cd

`change directory`：切换当前工作目录

- `cd /`：跳转到根目录
  - 普通用户：根目录就是`home`目录
- `cd / cd ~`：跳转到当前用户的`home`目录
  - root用户：`cd ~`相当于`cd /root`
  - 普通用户：`cd ~`相当于`cd /home/用户名目录`
- `cd -`：返回**进入此目录之前所在目录**
- `cd ../` 返回上一级目录（`/`可省略，即`cd ..`）

> `~`表示为home目录（用户主目录） 
>
> `.`表示当前所在的目录
>
> `..`表示目前目录的上一级目录

### ls

`list files`：按英文字母顺序显示指定工作目录下之内容（文件和子目录)

- `-a`：列出所有目录和文件 （`.`开头的**隐藏文件**也会列出）
- `-l`：列出目录和文件的详细资料（文件名、权限、拥有者、大小等）
- `-d`：仅列出目录本身，而不列出目录的文件数据
- `-r`：将文件以**相反次序**列出
- `-t`：按文件建立时间顺序列出
- `-h`：将文件容量以易读的方式列出（GB，kB等）
- `-F`：在列出的文件名后加符号（可执行档则加`*`, 目录则加`/`）
- `-R`：连同子目录的内容一起列出（递归列出）

> 参数可以组合使用

### cat

`concatenate`：查看文件内容（从第一行开始）

> 连接文件并打印全部内容到标准输出设备上（屏幕）
>
> `tac`：从最后一行开始显示（倒着写的`cat`）

- `-n (--number)`：在每一行前显示行号（从1开始）
- `-b (--number-nonblank)`：在每一行前显示行号，空白行不编号
- `-s (--squeeze-blank)`：将连续两行以上的空白行替换为一行的空白行
- `-v (--show-nonprinting)`：查看文件中是否有`^M`（win中的回车）
- `-E (--show-ends)` : 在每行结束处显示`$`
- `-T (--show-tabs)`: 将TAB字符显示为`^I`

- `-A (--show-all)`：等价于`-vET`
- `-e`：等价于`-vE`
- `-t`：等价于`-vT`

> 在类Unix系统中，`/dev/null`称为空设备，是一个特殊的设备文件。它会丢弃一切写入其中的数据（但报告写入操作成功），读取它则会得到一个EOF

```bash
# 清空/etc/test.txt文档内容
cat /dev/null > /etc/test.txt
```

### more

一页一页的查看文件内容

- `-num`：一次显示的行数
- `+num`：从第num行开始显示
- `-p`：不以滚动的方式显示每一页，而是先清空屏幕再显示内容
- `-c`：不以滚动的方式显示每一页、先显示内容再清空屏幕
- `-s`：将连续两行以上的空白行替换为一行的空白行

**翻页操作**

- `space`：向下翻**一页**
- `Enter`：向下翻n行（默认**一行**）
- `b`：往回翻一页（只对文件有用）
- `q`：退出
- `/string`：在显示的内容中**向下**搜寻`string`关键字
- `=`：显示当前行的行号
- `:f`：显示文件名以及当前显示的行数
- `V`：调用vi编辑器
- `!命令`：调用Shell执行命令

### less

一页一页的查看文件内容

> 比`more`的功能更多
>
> - 使用光标在文件（前后左右）滚屏
> - 用行号或百分比作为书签浏览文件
> - 实现了复杂检索，高亮显示等操作
> - 阅读到文件结束不会退出

- `-m`：显示百分比
- `-N`：显示每行的行号
- `-g`：只标志最后搜索的关键词
- `-i`：忽略搜索时的大小写
- `-b <num>`：设置缓冲区的大小
- `-e`：当文件显示结束后自动退出
- `-f`：强制打开特殊文件（例如外围设备代号、目录和二进制文件）
- `-o <fileName>`：将less输出的内容在指定文件中保存起来
- `-s`：将连续两行以上的空白行替换为一行的空白行

**操作**

- `space`：向下翻**一页**
- `b`：向上翻**一页**
- `Enter`：向下翻**一行**
- `y`：向上翻一行
- `u`：向上翻半页
- `d`：向后翻半页
- `h`：显示帮助界面
- `/string`：在显示的内容中**向下**搜寻`string`关键字（第一个结果高亮显示）
  - `n`：向下搜索下一个字符
  - `N`：向上搜索上一个字符
- `q`：退出

> - `home`：跳到文件开始
> - `end`：跳到最后
> - `pagedown`：向下翻一页
> - `pageup`：向上翻一页

### head

显示文件前几行

- `-n num`：显示前num行（默认显示前十行）
- `-c num`：显示num字节

```bash
# 显示前20行
head -n 20 /etc/man.config
```

### tail

显示文件后几行

- `-n num`：显示后num行（默认显示最后十行）
- `-n +num`：显示第num行到末尾（默认显示最后十行）
- `-c num`：显示num字节
- `-f`：显示正在改变的日志文件（`ctr+c`结束）

> 重点用于追踪查看日志：`tail -f`

```bash
# 显示最后20行
tail -n 20 /etc/man.config

# 显示从第20行到文件末尾
tail -n +20 /etc/man.config

# 当将某些行添加到man.config文件时，tail命令会继续显示这些行，直到按下Ctrl+C停止
tail -f /etc/man.config
```

### grep

查找文件内容

使用单引号`''`查找包含空格的关键词

```bash
# 在day文件中查找包含un的行
grep un day
```

### nl

`number of lines`：将输出的文件内容自动的加上行号

> 默认空行不加行号
>
> 将指定的文件内容添加行号标注后写到标准输出（屏幕）

- `-b`：指定行号样式
  - `-b a`：不论是否为空行都同样列出行号（类似`cat -n`）
  - `-b t`：如果有空行则不列出行号（默认）
  - `-b n`：不打印任何行号
- `-n`：指定行号格式
  - `-n ln`：行号左对齐
  - `-n rn`：行号右对齐
  - `-n rz`：行号右对齐，空格用0填充
- `-w`：指定行号位数（默认六位）

## 查找文件find

在指定范围内查找文件

- 需要一个路径作为查找范围
  - 指定`/`则会查找整个文件系统
- 可以配合通配符使用
- 可以使用`-type`指定文件类型
  - b：块设备文件
  - c：字符设备文件
  - d：目录文件
  - f：普通文件
  - p：命令管道
  - l：符号链接

> 用户没有权限的目录会被跳过扫描

```bash
# -print表示将结果输出到标准输出（屏幕）
find /etc/ -name fileName -print

# 查看名为init.d的目录文件
find /etc/ -name init.d -type d -print
```

## 定位文件locate

`locate`命令自动建立了整个文件名数据库，通过检索数据库来确定文件的位置

- 使用`updatedb`更新文件名数据库（需要root权限）

> `find`需要文件位置的大概范围

```bash
locate *.doc
```



## 查找特定程序whereis

查找程序文件，并提供文件的二进制可执行文件，源代码文件和使用手册的存放位置

```bash
whereis find
```

## 查看历史命令history

默认记录1000条命令

`ctrl+r`开启搜索功能

```bash
# 执行第n条记录
!n
# 清空历史记录
history -c
```



> `etc/profile`定义了`HISTSIZE=1000`

## 打印echo

显示指定的一行字符串

- `-n`：不输出换行（默认输出后换行）
- `-e`：支持\后的转义字符
  - `\\`：反斜线
  - `\b`：退格（删除）
  - `\n`：换行
  - `\c`：不换行

## 清理屏幕clear

- `clear`
- `cls`
- `ctrl+l`

## 关机shutdown

可以用来关机，也可以用来重启

- `-h`：关机
- `-r`：重启
- `-n`：强行关闭所有执行程序后自行关机
- `-t`: 设定在**几秒钟之后**关机
- `-c`：取消目前已经进行中的关机指令

```bash
# 立即关机
shutdown -h now

# 在10分钟后关机
shutdown -h 10

# 重新启动相当于reboot
shutdown -r now

# 取消进行中的关机指令
shutdown –c
```



# 文件目录

Linux系统没有盘符的概念。已经建立文件系统的硬盘分区被挂载在某一个目录下

1. Linux首先建立一个根文件系统`/`
2. 然后在根文件系统下建立一系列空目录
3. 然后将其他硬盘分区的文件系统挂载到这些目录中



## 建立文件和目录

### mkdir

`make directory`：创建目录

### rmdir

`remove directory`：删除空目录

```bash
# 在工作目录下的A目录中删除子目录B
# 若B删除后A目录成为空目录，则删除A
rmdir -p A/B
```

### touch

创建一个空文件

- 更新文件的建立日期和时间

### rm

`remove`：删除目录或文件

- `-i`：删除前询问确认
- `-f`：直接强行删除，无需确认（即使属性是只读）
- `-r`：向下递归删除（不管有多少级目录）

删除文件可以直接使用`rm`命令，若删除目录则必须使用选项`-r`

```bash
# 删除当前目录下的所有文件及目录
rm -rf ./*
```



## 移动和重命名

### mv

- 为文件或目录重命名
- 将文件从一个目录移入另一个目录中（剪切）
  - 目标文件是目录，则源文件直接移动到该文件夹内，名字不变
  - 目标文件是文件，则源文件移动的同时还会重命名
  - 源文件为多个，则目标必须是目录，并且统一移动到目录下

`mv [options] 源文件或目录 目标文件或目录`

- `-b`：当目标文件存在时，先进行备份在覆盖

- `-f`：当目标文件存在时，强制覆盖（指定此参数后`i`参数将不再起作用）

- `-i`：当目标文件存在时，询问是否覆盖（默认选项）

- `-v`：显示过程

```bash
# 将文件test.txt重命名为ink.txt：
mv test.txt ink.txt

# 将/usr/ink中的所有文件移到当前目录(用.表示)中：
mv /usr/ink/* .

# 将当前目录的一个子目录里的文件移动到另一个子目录里
mv 文件名/*  另一个目录

# 移动当前文件夹下的所有文件到上一级目录
mv * ../另一个目录
```

## 文件和目录权限

Linux系统中每个文件都设有访问权限来决定用户是否能通过某种方式对文件进行读、写、执行等操作

使用`ls -l`查看文件的属性（包括权限）

- `r`：4（100）可读（read）
- `w`：2（010）可写（write）
- `x`：1（001）可执行（execute）

### chown

改变文件所有权

### chmod

改变文件的权限

用**数字和**改变权限（三个权限的位置不会改变，如果没有权限显示减号`-`）

- 7：可读可写可执行
- 5：可读可执行
- 4：只读

操作文件的**用户有3种不同类型**

- 文件所有者
- 群组用户
- 其他用户

最高位表示文件所有者的权限值，中间位表示群组用户的权限值，最低位则表示其他用户的权限值

> 不要用chmod 777 指令修改`usr`等文件的权限，系统会崩溃

```bash
# 可读可写可执行
# 三个7分别对应三种用户的权限值
chmod 777 dirName
```

# 磁盘管理

## 挂载

# 用户和用户组

## 用户间切换su

`switch user`：用于变更为其他使用者的身份

- 除root外，需要输入使用者的密码

`su`和`su -`的区别

- `su`是切换用户存取权限，但是**没有获得环境变量**，所以`PATH`没有被带入
- `su -`是完全切换用户，可以获得环境变量

> 执行sudo命令时，系统以root用户身份运行命令之前提示输入当前用户帐户的密码，它不会切换到root用户或需要单独的root用户密码

```bash
# 显示当前用户
whoami 

# 切换用户，如su root,exit退出
su 用户名

# 切换用户，改变环境变量
su - 用户名

# 使用root权限运行单个命令
sudo 命令
```

## passwd

更改使用者的密码

- `-S`：显示密码信息
- `-d`：删除密码

```bash
# 设置ink用户的密码
passwd ink	
```

## /etc/passwd

- 在`/etc/passwd`文件中每个用户都有一个对应的记录行，它记录了这个用户的一些基本属性
- 系统管理员经常修改这个文件的以完成对用户的管理工作
- 这个文件对所有用户都是可读的

记录行被冒号`:`分隔为7个字段，其格式和具体含义如下

**用户名**:**口令**:**用户标识号**:**组标识号**:**注释性描述**:**主目录**:**登录Shell**

1. **用户名(login_name)**：代表**用户账号**的字符串。通常长度不超过8个字符，由大小写字母和/或数字组成。**登录名中不能有冒号**（冒号在这里是分隔符）

   > 为了兼容起见，登录名中最好不要包含`.`，不要使用`-`和`+`开头

2. **口令(passwd)**：存放加密后的用户口令，这个字段存放的只是用户口令的**加密串**，不是明文，由于`/etc/passwd`文件对所有用户都可读，所以它一个安全隐患。

   > 现在许多Linux系统都使用了**shadow技术**，把真正的加密后的用户口令字存放到`/etc/shadow`文件中，而在`/etc/passwd`文件的口令字段中只存放一个特殊的字符，例如`x`或者`*`

3. **用户标识号(UID)**：系统内部用它来标识用户。一般情况下它与用户名是一一对应的。**如果几个用户名对应的用户标识号是一样的，系统内部将把它们视为同一个用户**，但是它们可以有不同的口令、不同的主目录以及不同的登录Shell等

   UID取值范围是0-65535

   - 0是超级用户root的标识号
   - 1-99由系统保留作为管理账号
   - 普通用户的标识号从100开始（在Linux系统中界限是500）

4. **组标识号(GID)**：用户所属的用户组，它对应着`/etc/group`文件中的一条记录

5. **注释性描述(users)**：记录用户的一些个人情况（例如用户的真实姓名、电话、地址等）

   > 这个字段并没有什么实际的用途。不同的Linux系统中格式没有统一。在许多Linux系统中这个字段存放的是一段任意的注释性描述文字，用做finger命令的输出

6. **主目录(home_directory)**：用户的起始工作目录，它是**用户在登录系统后所处的目录**

   > 在大多数系统中，用户的主目录都被组织在同一个特定的目录下，而用户主目录的名称就是该用户的登录名。各用户对自己的主目录有读、写、执行（搜索）权限，其他用户对此目录的访问权限则根据具体情况设置

7. **登录Shell(Shell)**：用户登录后要启动一个进程，**负责将用户的操作传给内核**，这个进程是用户登录到系统后运行的命令解释器或某个特定的程序（即Shell）



# 进程管理

## 监视进程ps

`process status`：显示当前系统上运行的所有进程的信息

> 执行`ps`命令的时刻的进程信息的`快照`（静态）

```bash
# 列出当前所有的正在内存当中的程序
ps aux

# 查找进程
ps -ef | grep 进程关键字

# 显示root进程用户信息
ps -u root
```



## 实时监控top

实时监控系统状态信息和进程所使用的资源

- 使用cpu最多的程序会排在最前面

> 默认10s更新一次

## 查看占用进程的文件lsof

查看某些文件正在被哪些进程使用

- 不带参数则会列出当前系统中所有打开文件的进程信息
- 查询占用特定文件的进程则需要提供文件名作为参数

## 向进程发送信息kill

`kill`命令只是向进程发送一个信号

- 9：kill杀死进程

```bash
kii -9 pid
```



# 网络配置

## netstat

用于显示系统的网络状态

- `-a/--all`：显示所有socket套接字，包括正在监听的（LISTEN）
- `-n/--numeric`：直接显示IP地址，而不通过域名服务器（可以加速操作）
- `-p/--programs`：显示正在使用Socket的进程标识符和程序名称
- `-l/--listening`：仅显示监听的服务器的socket
- `-t/--tcp`：显示TCP端口
- `-u/--udp`：显示UDP端口

> **windows**
>
> - 查看系统当前使用所有端口：`netstat -ano`
> - 查看已知的端口是否被占用：`netstat -ano |findstr 1081`

```bash
# -anp常用来筛选
# 查看已知的端口是否被占用
netstat -anp |grep 9100

# 查看服务器已使用的所有端口
netstat -nultp
```







# Linux编程

## vim编辑器

- 普通模式
  - 移动光标
  - 按`i`进入插入模式
  - 按`:`进入命令模式

- 命令模式
  - 按`esc`回到普通模式
- 插入模式
  - 按`esc`回到普通模式

> vim命令严格区分大小写

### 普通模式

输入`/`

- **搜索字符串**
  - `/string`：向前查找string（向文件尾）
  - `？string`：向后查找string（向文件头）
  
- **跳转搜索内容**
  - `n`：跳转到下一个匹配处
  - `N`：跳转到上一个匹配处

### 命令模式

按`:`

- **忽略大小写**
  - `:set ignorecase`

- **重新开启大小写敏感**
  - `:set noignorecase`

### 插入模式

- `a`：在光标后插入
- `i`：在光标位置插入
- `o`：在光标下一行插入（创建新的空白行）

### 移动光标

- `h`：向左移动一格
- `l`：向右移动一格
- `k`：向上移动一格
- `j`：向下移动一格
- `^`：移动到行首
- `$`：移动到行尾
- `w`：移动到下一个单词
- `b`：移动到上一个单词
- `gg`：移动到文件首行

> 可以在命令前加上数字表示重复多少次移动：`5w`

### 删除

- `x`：删除光标位置的字符
- `dd`：删除光标所在行
- `D`：删除光标位置到行尾之间的所有字符

> `ndd`：删除n行

### 复制粘贴

- `yy`：复制光标所在行
- `p`：在光标所在位置后粘贴最近复制或删除的内容
- `P`：在光标所在位置前粘贴最近复制或删除的内容

### 撤销

- `u`：撤销上一步操作
  - 可以多次使用：输入两个u则会撤销两步操作

## 正则表达式

### 位置匹配

- 匹配开头：`^`
- 匹配结尾：`$`

> 匹配空行：`^$`

### 字符集和单词

单词：两侧由非单词字符分割的字符串

非单词字符：字母，数字，下划线以外的字符

- `.`：匹配除换行符外任意一个字符
- `[]`：匹配方括号内指定的字符集
  - 无论字符集有多少，匹配时只能匹配其中一个（即一次）
  
  - 使用`-`限制字符集的范围
  
    > .at，[a-z]at，[a-zA-z]，[0-9]
- 分隔符
  - `\<`
  - `\>`

```bash
egrep "^a.t$" /usr/share/word.txt

egrep "[a-z]at" /usr/share/word.txt

egrep "\<[a-z]at\>" /usr/share/word.txt
```

### 字符类

预定义字符类来匹配特定字符

- `[[:alnum:]]`：文字，数字字符
- `[[:alpha:]]`：字母字符
- `[[:lower:]]`：小写字母
- `[[:upper:]]`：大写字母
- `[[:digit:]]`：小数
- `[[:space:]]`：空格
- `[[:punct:]]`：标点符号

> `[[:upper:]]`就相当于`[A-Z]`

```bash
# 匹配所有大写字母开头，t结尾的单词
egrep "^[[:upper:]]t$" word.txt
```

### 字符转义

匹配转义字符和正则本身使用的符号

- 匹配`.`：`\.`
- 匹配`[`：`\[`
- 匹配`\`：`\\`

### 重复

- `*`：表示一个字符重复0次或者多次
- `+`：表示一个字符重复1次或者多次
- `?`：表示一个重复0次或者1次
- `{n}`：指定重复n次
- `{n,}`：指定重复n次或者多次
- `{n,m}`：指定重复的次数不少于n次，不多于m次

```bash
# 以a开头，t结尾的单词
# .匹配一个字符，*值.匹配的字符可以任意次
^a.*t$

# 在hi后隔了一个或多个字符后是ink的单词
# .匹配一个字符，*值.匹配的字符至少一次
\<hi\>.+\<ink\>

# 不少于8位的数
\<[1-9][0-9]{7,}\>
```

### 子表达式

`()`：分组

```bash
# 匹配or重复2次或以上的单词
egrep "(or){2,}" word.txt

# 匹配r重复2次或以上的单词
egrep "or{2,}" word.txt
```

### 反义

`^`：用于匹配除了指定字符外的所有字符

- `[^y]`
- `[^aeiou]`

> `^[^y]`：匹配所有不以y开头的单词

### 分支

`|`：或

### 逆向引用



## shell编程



# Anaconda

**查看已经有的环境**

- `conda-env list`

**提示环境存放路径**

- `environment location: /usr/local/anaconda3/envs/buaa_test`

**添加到环境变量**

- `export PATH=/root/anaconda3/bin:$PATH`
- `source ~/.bashrc`

```bash
# 下载
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.2.0-Linux-x86_64.sh

# 安装
sh Anaconda3-5.2.0-Linux-x86_64.sh

# 创建环境
conda create --name env_name

# 启用环境
conda activate env_name
```



# 打包压缩

linux主要有三种压缩方式：

1. `gzip`：压缩这速度最快，压缩大文件的时候与其他的压缩方式相比更加明显，历史最久，应用最广泛的压缩方式
2. `bzip`：压缩形成的文件小，但是可用性不如gzip
3. `xz`：最新的压缩方式，可以自动提供最佳的压缩率

> 压缩速度：gz > bz2 > xz
> 压缩率：xz > bz2 > gz

Linux中	

- 打包文件一般是以`.tar`结尾的
- 压缩文件一般是以`.gz`（gzip）结尾的

一般情况下**打包和压缩是一起进行的**，打包并压缩后的文件的后缀名一般是`.tar.gz`

**打包跟压缩的区别**

- 打包是指将多个文件或者目录放在一起，形成一个总的包，这样便于保存和传输，但是**大小是没有变化的**
- 压缩是指将一个或者多个大文件或者目录通过压缩算法使文件的体积变小以达到压缩的目的，可以节省存储空间，**在压缩的时候通常是先打包再压缩**

## tar

- tar命令参数前面加不加`-`执行命令的结果是没有区别的，区别只要是在于linux风格方面
- tar命令会自己选择跟压缩方式对应的方式去解压



**常用参数**：

- `-z`（--gzip）：使用gzip工具（解）压缩，后缀为`.gz`
- `-j`（--bzip2）：使用bzip2工具（解）压缩，后缀为 `.bz2`
- `-J`：使用xz工具（解）压缩，后缀为 `.xz`

- `-c`（--create）：打包文件，后缀为`.tar`

- `-x`（--extract）：解压缩、提取打包的内容

- `-v`：显示压缩或者打包过程

- `-t`（--list）：查看压缩包内容

  > 不和`-c`，`-x`同时出现

- `p`  保留备份数据的原本权限与属性

  > 常用于备份重要的配置文件

- `-P`  保留绝对路径

  > 在压缩文件的时候使用了`-P`，那么在解压的时候也要加上`-P`

- `-f`（--file）：指定文件名（后面接压缩后的包名）

  > tar命令中`-f`是必选的，且放在所有参数的最后（右）

- `-C`：指定解压缩包内容和打包的内容存放的目录

  > tar  参数  被解压的文件名   -C 指定目录

- `--exclude`：压缩或打包时排除指定的文件

```bash
# 常用压缩参数组合：zcvf
tar -zcvf xxx.tar.gz filename1 filename2

# 常用解压参数组合：
# 后缀名为.tar.gz的压缩包用zxvf
tar -zxvf xxx.tar.gz dir_name

# 后缀名为.tar的压缩包用xvf
tar -xvf xxx.tar.gz dir_name
```



**增量备份**

`-g`：后接增量备份的快照文件（备份目录最好用相对路径）

## zip unzip

**安装**

```bash
# 在 Ubuntu 和 Debian 上安装解压缩
sudo apt install unzip

# 在 CentOS 和 Fedora 上安装解压缩
sudo yum install unzip
```



**zip常用参数**：

- `-m`：将文件压缩后，删除原文件
- `-o`：将压缩文件内的所有文件的最新变动时间设为压缩的时间
- `-q`：在压缩的时候不显示指令执行的过程（安静模式）
- `-r`：递归压缩，将自定**目录下**的所有子文件以及文件一起处理
- `-x`：压缩时排除指定的文件

**unzip常用参数**：

- `-c`：显示解压缩的结果，并没有解压压缩包

  > 显示每一个目录下的每一个文件的内容，同时对字符做适当的转换

- `-l`：显示压缩包内所包含的文件

- `-t`：检查压缩文件是否正确

  > OK表示正确

- `-v`：执行时显示压缩文件的详细信息

  > 使用`-v`显示的信息比使用`-l`显示的信息更加详细

- `-q`：执行时不显示任何信息（安静模式）

- `-d`：指定文件解压后存储的目录

- `-x`：解压缩时排除指定的文件

```bash
# 压缩成zip格式
zip -q -r filename.zip

# 解压zip格式的压缩包
unzip filename.zip -d dir_name
```



# 文件传输

- **Linux文件传输到Windows**
- **Windows文件传输到Linux**
- **Linux文件传输到Linux**

## rz sz

**安装**

```bash
# 查看是否安装lrzsz
rz

# CentOS安装
sudo yum -y install lrzsz

# Ubuntu下安装
sudo apt-get install lrzsz

# 确认是否正确安装
rpm -qa lrzsz
```

**传输**

```bash
# Windows向Linux传输文件，路径默认是linux服务器当前目录
rz

# Linux向Windows传输文件
sz filename
```

**修改传输路径**

![文件传输](Linux.assets/文件传输.png)





# SSH

`Secure Shell`（SSH）

目前较可靠的，专为远程登录会话和其他网络服务提供安全性的**协议**。通过 SSH Client 可以连接到安装运行了 SSH Server 的远程机器上

SSH 的连接分为两步：

- 客户端和服务端建立连接
- 用户身份鉴权

## SSH连接

**客户端和服务端建立连接**

1. 客户端联系服务端，双方沟通自己支持的SSH协议的版本，约定使用某个共同支持的版本
2. 服务端将自己的`Host Key`，加密方法和其他一些参数发给客户端
3. 客户端通过服务端发送的`Host Key`验证服务端身份，双方用服务端发来的参数和`Diffie-Hellman`算法生成`Session Key`
4. 加密通道建立完成

**Host Key**

Host Key由SSH自行生成，分为两种：

- Public Key
- Private Key

服务端拥有Public Key和Private Key，并将Public Key发送给客户端

如果客户端通过Host Key发现从来没有连接过这台服务器，会询问用户是否要继续连接，用户同意连接后客户端会在本地的`.ssh\known_hosts`文件记录这台服务器的信息，下次连接时客户端就不会再次询问用户

**证书**

仅靠服务端发送Host Key的方法无法防范中间人攻击，后来又出现了Public Key Certificates，由一个可靠的第三方机构给服务端签发证书从而确保了安全性

**Session Key**

Session Key用于连接之后通讯时**对消息进行加密和解密**

使用Session Key加密的机制被称作**对称加密**（Symmetric Encryption），也就是两端使用的相同的Key来加密和解密信息

> SSH传输信息的加密解密时并不是用生成的Public Key或Private Key，而是用Session Key



**Session Key生成**

1. 客户端和服务端使用沟通后确定的加密算法以及双方都知道的一个数字
2. 客户端和服务端各自生成只有自己才知道的private密码，并用它对数字进行加密生成**新的密码**
3. 客户端和服务端交换各自加密后的密码
4. 客户端和服务端分别将对方发来的密码再加上自己的private密码，从而得到相同的Session Key



**用户身份鉴权**

在客户端生成的Public Key和Private Key就是用来进行身份鉴权的，客户端需要将Public Key上传到服务器上（改名为`authorized_Keys`）

1. 客户端用Private Key生成签名向服务器发起登录请求
2. 服务端验证签名（检查自己有没有和这个签名匹配的Public Key）
3. 服务端生成一串随机字符串，用Public Key加密后发送给客户端
4. 客户端用对应的Private Key解密字符串，再使用MD5 hash 和Session Key加密该字符串，将加密后的字符串发送给服务端
5. 服务端使用同样的MD5 hash 和Session Key计算这串字符的加密结果，并和客户端发来的结果做比对，结果一样则允许登录
6. 然后双方将使用Session Key进行通讯

使用Public Key和Private Key的加密机制被称作**不对称加密**（Asymmetry Encryption），即使用不同的Key来对信息进行加密解密。

客户端使用Private Key可以解密服务端使用Public Key加密的信息，服务端使用Public Key 无法解密客户端使用Private Key发来的加密信息

> 身份鉴权除了使用Host Key登录，也可以使用密码登录



## SSH Server

**CentOS**

- OpenSSH Server安装完成后在`/etc/init.d`目录下会增加一个名为**sshd**的服务
- 配置信息保存目录：`/etc/ssh`
- sshd服务配置文件：`/etc/ssh/sshd_config`

> 通常Linux系统会默认安装openssh的客户端软件**openssh-client**，需要自己安装服务端**openssh-server**
>
> 如果云服务器sshd服务配置并没有开启公钥登录（`ssh name@remotehost`显示的不是云服务器相关信息而是输入密码），就需要登录到云服务器开启sshd服务的公钥登录配置。在`/etc/ssh/sshd_config`配置文件中找到PublicAuthentication项，删除注释`#`并修改值为`yes`。最后`service sshd restart`重启sshd服务

```bash
yum install openssh-server

# 查看服务
chkconfig --list sshd

# 手动启动sshd服务
/etc/init.d/sshd start
```



**Ubuntu**

```bash
sudo apt-get update

sudo apt-get install openssh-server

# 生成SSH钥匙后开启openssh服务
sudo /etc/init.d/ssh start

# 验证
ps -e | grep ssh
```



## SSH Client

**连接远程机器**

- `user`：远程机器上登录的用户名，如果不指定的话默认为当前用户
- `remotehost`：远程机器的地址，可以是 IP，域名或者是**别名**
- `port`：SSH Server 监听的端口，如果不指定的话就为默认值22

> 执行了 `ssh` 命令之后远程机器会询问密码。输入密码时屏幕上不会显示明文密码，也不会显示 `******`（隐藏密码长度）

```bash
ssh user@remotehost -p port
```



## SSH密钥

使用**ssh-keygen**工具在客户端生成SSH密钥

- `-t`表示类型选项，采用`rsa`加密算法
- 要求设置私钥口令`passphrase`，不设置则为空
- 要求设置保存位置，一般存放在默认路径，回车即可

> RSA密钥对也可以在服务端生成

```bash
ssh-keygen -t rsa
```

### L2L

会在`/home/当前用户`目录下生成`.ssh`文件夹

- **公钥**： `~/.ssh/id_rsa.pub`
- **私钥**： `~/.ssh/id_rsa`

将**公钥**`id_rsa.pub`写入到远程服务器的`~/.ssh/authorized_keys`文件中

> 默认22端口，`-p`可以省略
>
> Linux系统里缺省都包含一个名为ssh-copy-id的工具，其实就是一个shell脚本

```bash
# 将本地的ssh公钥文件安装到远程主机对应的账户下
# 输入yes和账户密码
ssh-copy-id -i ~/.ssh/id_rsa.pub user@remotehost -p port
```



### W2L

>  ssh会把你每个你访问过计算机的公钥(public key)都记录在~/.ssh/known_hosts

在**应用和功能**里的**管理可选功能**中**开启openss服务**

搜索**服务**，在服务里将`openssh Authentication Agent`设置为**自动启动**并启动

在远程服务器上新建 `.ssh` 目录，然后把**公钥**`id_rsa.pub` **追加**到远程主机的 `.ssh/authorized_keys` 中

> `mkdir -p`：递归创建目录，当上级目录不存在时会按目录层级自动创建目录

```bash
ssh user@remotehost -p port 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```



**配置别名**

在`.bashrc`中添加信息

> 保存后即可用 `nlsde` 登录

```bash
sudo vim ~/.bashrc
# 在最下面附加 
alias nlsde="ssh user@remote" 
# 立即更新
source ~/.bashrc
```

在 `~/.ssh/config`中添加信息

> 保存后即可用 `ssh nlsde` 登录

```bash
# 服务器名称
Host nlsde
	# 服务器IP
    HostName remote
    # 登录用户
    User user
    # 连接端口
    Port port
```



### know_hosts

ssh会把你每个你访问过计算机的公钥(public key)都记录在known_hosts。当下次访问相同计算机时，OpenSSH会核对公钥。如果公钥不同，OpenSSH会发出警告， 避免你受到DNS Hijack之类的攻击。

从上面的图中可以看出，known_hosts中的格式是

```
CopyIp或域名  主机名 host-key
```



## Xshell连接云服务器

1. **腾讯云生成密钥**

   1. 下载密钥文件`ink.pem`

   2. 点击刚创建的SSH密钥，复制其中的**公钥**，然后放在同一个文件夹中

      > 公钥的名称和密钥一样，后缀为`.pub`，密钥没有文件名后缀

2. **绑定云主机**

3. **Xshell加载密钥**

   1. 点击XShell左上角的新建连接按钮，输入主机名和ip，点击连接
   2. 账号密码登录，输入密码
   3. SSH登录，选择下载的密钥`ink.pem`(腾讯云生成的时候没有密码，不用输入)



# 防火墙

CentOS7.0默认使用`firewall`作为防火墙

## nmap

```bash
# 安装(非最新)
yum install nmap

# 无法更新
yum update nmap

# 先卸载
yum remove nmap

# 安装最新版本
rpm -vhU https://nmap.org/dist/nmap-7.70-1.x86_64.rpm
```

## 查看端口

```bash
# 查看主机当前开放的端口
nmap localhost    

# 查看主机端口（1024-65535）中开放的端口
nmap -p 1024-65535 localhost 

# 探测目标主机开放的端口
nmap -PS 192.168.21.163 

# 探测所列出的目标主机端口            
nmap -PS22,80,3306  192.168.21.163 

# 探测目标主机操作系统类型
nmap -O 192.168.21.163

# 探测目标主机操作系统类型
nmap -A 192.168.21.163 

# 更多nmap参数请查询帮助信息
nmap --help                             
```

### 操作端口

```bash
# 开启端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent

# 关闭端口
firewall-cmd --permanent --remove-port=9200/tcp

# 重启防火墙
systemctl restart firewalld.service
```





# WSL

`Windows Subsystem for Linux（`简称WSL）是一个为在Windows 10上能够原生运行**Linux二进制可执行文件**（ELF格式）的兼容层

WSL不是虚拟机而是子系统，是Windows的一部分，并不像虚拟机一样与宿主系统隔离，**windows下的所有文件在Linux subsystem里都有映射的**，所以在Linux subsystem里运行一些危险指令也会影响到Windows

目标是使纯正的Ubuntu 14.04 "Trusty Tahr"映像能下载和解压到用户的本地计算机，并且映像内的工具和实用工具能在此子系统上原生运行。

> 它是由微软与Canonical公司合作开发

## 安装

1. **启用适用于Linux的Windows子系统**

   1. 使用管理员身份打开PowerShell，执行以下命令

      ```bash
      dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
      ```

   2. 或者在搜索栏中搜索并打开**启用或关闭Windows功能**，勾选**适用于Linux的Windows子系统**项

   3. 重启

2. **检查运行WSL2的要求**

   安装WSL2，对不同架构的CPU有不同的Win10版本要求，需要确保Win10版本号为2004（内部版本19041或更高）即可

   `win+r`输入`winver`可快速查看Windows版本。如果Win10版本号低于2004，可使用Windows10易升工具手动升级。

   下载Windows10易升工具，下载后运行等待完成升级即可

   ```bash
   https://www.microsoft.com/zh-cn/software-download/windows10
   ```

3. **启用虚拟机功能**

   以管理员身份打开PowerShell，执行以下命令

   ```bash
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

4. **下载Linux内核更新包并运行**

   > WSL2需要更新其内核组件。有关信息，请访问 https://aka.ms/wsl2kernel

5. **将WSL2设置为默认版本**

   ```bash
   wsl --set-default-version 2
   ```

6. 在微软应用商店搜索Linux，选择合适的发行版，这里选用Ubuntu 18.04 LTS

7. 启动Ubuntu 18.04 LTS，创建用户名及密码

8. 验证：查看WSL版本，确保WSL的版本为 2.0

   ```bash
   $ wsl -l -v
   ```
   
9. 设置WSL的默认版本

   ```bash
   wsl --set-version Ubuntu-18.04 2
   ```



## 账号

**Ubuntu 18.04 LTS**

```sh
#给root设置密码
su passwd root

#切换root
su root
```

## 查看文件

1. 在Linux查看windows其他分区（WSL可以将其它盘符挂载在`/mnt`下），

2. windows中C、D、E盘都对应在子系统中`/mnt`目录中

3. 在Windows下查看WSL文件位置

   1. wsl ubuntu 文件在本地磁盘的位置

   ```bash
   # 绝对路径
   C:\Users\用户\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\rootfs
   ```

## 安装git

```bash
#确保系统和apt包列表完全更新
sudo apt-get update -y
sudo apt-get upgrade -y

# 安装
sudo apt-get install git

# 验证
git --version

# 个人信息
git config --global user.name "ink"
git config --global user.email "541640794@qq.com"

# 查看(q+enter退出)
git config --list
```

## oh-my-zsh

- Linux发行版的默认命令解释器是Bash

- Zsh是另一个常用的命令解释器，相比于默认的Bash，Zsh有更多的自定义选项，并支持扩展，因此Zsh可以实现更强大的命令补全，命令高亮等一系列功能

- 默认的Zsh配置比较麻烦，在GitHub上有一个配置文件oh-my-zsh，是目前为止最流行的Zsh配置

### 下载字体

安装额外的字体来支持oh-my-zsh显示特殊的符号

- 在PowerShell中安装Powerline字体集合

```bash
git clone https://github.com/powerline/fonts.git
cd fonts
.\install.ps1
```

### 安装zsh

```bash
sudo apt update
sudo apt install git zsh -y

#查看是否已安装了zsh
zsh --version
```

### 安装oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 配置zsh

将主题设置为`agnoster`

```bash
# 配置 zsh
vim ~/.zshrc
# 修改ZSH_THEME
```

打开WindowsTerminal的JSON配置文件，在`schemes`中添加一个主题（主题名随意） 这里为`inswsl2`，并把字体改为一个Powerline字体

```json
"schemes": [
    {
        "name" : "inkwsl2",
        "background" : "#002B36",
        "black" : "#002B36",
        "blue" : "#268BD2",
        "brightBlack" : "#657B83",
        "brightBlue" : "#839496",
        "brightCyan" : "#D33682",
        "brightGreen" : "#B58900",
        "brightPurple" : "#EEE8D5",
        "brightRed" : "#CB4B16",
        "brightWhite" : "#FDF6E3",
        "brightYellow" : "#586E75",
        "cyan" : "#2AA198",
        "foreground" : "#93A1A1",
        "green" : "#859900",
        "purple" : "#6C71C4",
        "red" : "#DC322F",
        "white" : "#93A1A1",
        "yellow" : "#B58900"
    }
],
```

然后在该JSON文件中把wsl终端的主题设置为该`inkwsl2`主题，并把字体改为喜欢的一个 Powerline字体

```json
            {
                "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
                "hidden": false,
                "name": "Ubuntu-18.04",
                "colorScheme": "inkwsl2",
                "source": "Windows.Terminal.Wsl",
                "fontFace": "DejaVu Sans Mono for Powerline"
            },
```

再把命令行的机器名称去掉，并调整用户名的背景色

- 编辑agnoster主题文件

```bash
vi ~/.oh-my-zsh/themes/agnoster.zsh-theme

# 把 92 行修改为
prompt_segment green black "%(!.%{%F{yellow}%}.)%n"
```



# MobaXterm

- 支持各种连接 SSH，X11，RDP，VNC，FTP，MOSH
- 支持 Unix 命令(bash，ls，cat，sed，grep，awk，rsync，…)
- 连接 SSH 终端后支持 SFTP 传输文件
- 各种丰富的插件(git/dig/aria2…)
- 可运行 Windows 或软件

**复制粘贴**

在菜单栏点击 「settings」 --> 「Configuration」，在弹出的对话框中选择 「terminal」，将 「paste using right-click」 勾上



# WindowsTerminal

**设置默认Ubuntu**

点击标签右边的下拉三角-选择设置-打开JSON 配置文件-在`profiles`-`list`中找到Ubuntu的guid复制-粘贴到文件开头的 `defaultProfile` 的值



