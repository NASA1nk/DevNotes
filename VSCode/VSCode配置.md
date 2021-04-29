> VS Code官方文档

https://code.visualstudio.com/docs/languages/cpp

VSC只是一个纯文本**编辑器**(editor)，不是IDE(集成开发环境)，不含**编译器**(compiler)和许多其它功能，所以编译器要自己装好。

下载编译器：[MinGW-w64 - for 32 and 64 bit Windows](https://link.zhihu.com/?target=https%3A//sourceforge.net/projects/mingw-w64/files/) 往下稍微翻一下，选最新版本中的`x86_64-posix-seh`。

将bin文件夹的完整路径添加到环境变量中的PATH里去

```
Debian系Linux用
sudo apt update && sudo apt install build-essential
```



### 验证

按Win+R，运行cmd，输入gcc，应该会提示 *no input files* 而不是“不是内部命令或外部命令”或者“无法将 "gcc" 项识别为 cmdlet、函数、脚本文件或可运行程序的名称”。

如果是“不是内部命令或外部命令”，说明gcc在的文件夹没有在环境变量的Path中，要加进去才行。如果加了还是这样，重启。

输`gcc -v`可以显示出gcc的版本。如果显示出来的版本与你刚下的不同/更老，说明Path里原本有老版本的编译器，可能是安装其它IDE时装上的，最好去掉老的。

### 安装扩展(extension)

- C/C++：又名 cpptools，提供Debug和Format功能
- Code Runner：右键即可编译运行单文件，很方便；但无法Debug

其他可选扩展：

- Bracket Pair Colorizer 2：彩虹花括号
- One Dark Pro：大概是VS Code安装量最高的主题



**补充知识**

- 编译器是把源代码变成可执行文件的，编辑器是你打字的软件。记事本就是一个编辑器，VSC也是编辑器。**编辑器是无法编译运行程序的**，因为那是编译器的工作
- MinGW是gcc在Windows下的移植，gcc是世界上最流行的C/C++编译器组合。但gcc这个名字也指编译C语言的那个程序，g++才是C++编译器。即gcc程序和g++程序包含在gcc套件以及MinGW里，当只说gcc时要根据语境自己区分
- 其实MinGW和MinGW-w64只是名字像，它们是两个不同的项目。为了方便，本文中的MinGW指的其实都是MinGW-w64。MinGW还活着，但只能产生32位程序
- 现在MinGW-w64很久没有发布官方构建了，代码其实已经更新到了9.2.0，所以也可以考虑用基于它的TDM-GCC64。别下旧版，那是很久以前的，2020年发布了新版

# 快捷键

- `Ctrl+鼠标左键`，是文件、函数等跳转。
- `Alt + ←` ，是跳转后返回原处。
- `Ctrl + Shift + O`，列出函数名
- `Ctrl + P`，列出近期打开的文件名
- `Ctrl + Tab`, 可以列出最近打开的文件，在开发时，两个文件间切换时效率很高。

- `Alt+Shift+F`（或者用右键菜单）可以格式化代码

- `Ctrl+Shift+B`单纯编译，按F5为编译加调试。时不时用一下`Ctrl Shift B`，能尽早发现错误。

加断点在列号前面点一下，右键可以加条件断点。加在main函数就在一开始就停下来。开始调试后，按`f11`可以一步一步进行，箭头所指的那行代码就是**下一步要运行的代码**；`f5`是一直运行到下一个断点，右键某一行代码可以选择一直运行到指定的那一行。

左边有个调试栏，可以看到变量的值。自动栏没有的可以在Watch里手动添加，或在代码里选中右键有选项可以直接添加；小心不要添加有副作用的表达式。把鼠标放到变量上可以看到变量的值，但只能识别简单的表达式。栈帧对于观察递归很有用。栈溢出和段错误时还可以抓取“异常”，自动跳转到出错的行。

C语言的数组经过函数传递以后会退化为指针，直接添加表达式只能看到第一个元素。此时可以强制转换成指向固定大小的数组指针再解引：例如`int arr[10]`传进函数里后就变成了`int* arr`，在Watch里添加`*(int(*)[10])arr`，这样就能看到完整的数组了。但长度必须是写死的，自己小心越界。

**vscode不在程序末尾停止（和IDE不一样），可以在最后加一个断点，或者getchar()，或者`system("pause"); `**

### 多文件编译

进行少量的多文件编译，C语言直接用`gcc 源文件1.c 源文件2.c 头文件1.h`

大量的多文件编译，请学习如何写`makefile`或使用cmake。然后把tasks的命令改成调用make（或mingw32-make）等

想使用别人的库，比如ffmpeg，可能需要在命令中指定`-I`、`-l`（小写的L）、`-L`。具体参数阅读那个库的文档。还可能需要把路径添加到c_cpp_properties.json里来配置Intellisense。

VS Code输出中文很多人都遇到过乱码。这是因为VSC的源代码默认是UTF-8编码，cmd/PowerShell是GBK编码。使用VSC打开别人用Dev Cpp或CB编写的代码文件时需要手动选择用GBK打开



# c_cpp_properties.json文件配置

获取方法：

在cmd中输入下面的指令

```
gcc -v -E -x c++ -

C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++
C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/x86_64-w64-mingw32
C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/backward
C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include
C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/include-fixed
C:/Env/Compiler/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/8.1.0/../../../../x86_64-w64-mingw32/include
```



