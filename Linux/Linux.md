# Anaconda

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

> 提示环境存放路径
>
> environment location: /usr/local/anaconda3/envs/buaa_test
>
> 添加环境变量
>
> export PATH=/root/anaconda3/bin:$PATH
>
> source ~/.bashrc



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

## tar命令

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

## zip unzip命令

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

## rz sz命令

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

**可以修改传输路径**

![文件传输](Linux.assets/文件传输.png)



# 连接服务器

## SSH连接

```bash
# 生成密钥对,(-t表示类型选项，采用rsa加密算法)
ssh-keygen -t rsa

# 要求设置私钥口令 passphrase，不设置则为空

# 在/home/当前用户目录下生成一个.ssh文件夹
# 其中包含 私钥文件 id_rsa 和公钥文件 id_rsa.pub

# 将公钥复制到远程主机的 ~/ .ssh/authorized_key目录下
ssh-copy-id -i .ssh/id_rsa.pub 用户名@ip

# 连接登录
ssh 用户名@ip
```



## Xshell连接云服务器

1. **腾讯云生成密钥**

   1. 下载密钥文件`ink.pem`

   2. 点击刚创建的SSH密钥，复制其中的**公钥**，然后放在同一个文件夹中

      > 公钥的名称和密钥一样，后缀为.pub，密钥没有文件名后缀

2. **绑定云主机**

3. **Xshell加载密钥**

   1. 点击XShell左上角的新建连接按钮，输入主机名和ip，点击连接
   2. 账号密码登录，输入密码
   3. SSH登录，选择下载的密钥(腾讯云生成的时候没有密码，不用输入)



# WSL

`Windows Subsystem for Linux（`简称WSL）是一个为在Windows 10上能够原生运行**Linux二进制可执行文件**（ELF格式）的兼容层

WSL不是虚拟机而是子系统，是Windows的一部分，并不像虚拟机一样与宿主系统隔离，**windows下的所有文件在Linux subsystem里都有映射的**，所以在Linux subsystem里运行一些危险指令也会影响到Windows

目标是使纯正的Ubuntu 14.04 "Trusty Tahr"映像能下载和解压到用户的本地计算机，并且映像内的工具和实用工具能在此子系统上原生运行。

> 它是由微软与Canonical公司合作开发

## 安装

1. **启用或关闭Windows功能**

   在搜索栏中搜索并打开“启用或关闭Windows功能”，勾选“适用于Linux的Windows子系统”项。只有开启这项设置才能正常安装WSL。重启即可，注意保存状态

2. **安装WSL**

   在微软应用商店搜索Linux，根据自己需要选择适合自己的发行版，这里选用 Ubuntu 18.04 LTS

## 账号

Ubuntu 18.04 LTS

```sh
#给root设置密码
su passwd root

#切换root
su root
```

## 查看文件

1. 在 Linux 查看windows其他分区（WSL可以将其它盘符挂载在`/mnt` 下），windows中C、D、E盘都对应在子系统中`/mnt`目录中

2. 在 Windows 下查看 WSL 文件位置

   wsl ubuntu 文件在本地磁盘的位置

   ```bash
   # 绝对路径
   C:\Users\用户\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu18.04onWindows_79rhkp1fndgsc\LocalState\rootfs
   ```

   





