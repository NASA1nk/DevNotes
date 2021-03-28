# Dos命令

```bash
#盘符切换	D:
#查看当前目录文件	dir
#切换目录	 cd(change directory), 跨盘符需要加路径/(cd /d f:\ink),返回上一级（cd ..）
#退出终端	 exit
#清空窗口	 cls(clear screen)		
#查看ip	   ifconfig
#ping		ping www.baidu.com  可以得到其ip地址
#创建文件夹	 md ink(mkdir-make directory)
#删除文件夹	 rd ink(remove directory)
#创建文件	 cd> ink.txt
#删除文件	 del ink.txt
```



# Java

## 版本

跨平台运行（**JVM**）

**Java SE** ：标准版	（桌面程序，控制台开发）

**Java EE** ：企业级开发	（web端，服务器开发）



## JDK	JRE	JVM

**JDK**：Java Development Kit	开发者工具（jdk包含了jre）

**JRE**：Java Runtime Environment	运行时环境

**JVM**：Java Virtual Machine	JAVA虚拟机



## Java开发环境

### 卸载JDK

**查找jdk位置**：在环境变量中找到JAVA_HOME。

**删除对应目录下文件**，然后删除JAVA_HOME,最后删除PATH中关于java的目录

**验证**：java -version



### 安装

**下载**：直接搜索jdk8（可专门设置env文件夹存放）

**配置环境变量**：

 	1. 我的电脑-->属性-->高级系统设置
 	2. 环境变-->系统变量-->新建-->**JAVA_HOME**（安装路径）
 	3. PATH变量-->新建-->**%JAVA_HOME%\bin**（%%表示引用）
 	4. PATH变量-->新建-->**%JAVA_HOME%\jre\bin**

```bash
#可以直接在path中添加jdk\bin路径即可，不写JAVA_HOME
#jdk11已经不用配置jre了
#bin目录存放可执行程序exe，如java.exe,javac.exe
```



## 第一个程序

**文件和类名必须保持一致，首字母大写**

```bash
javac HelloWorld.java	#编译生成.class文件
java HelloWorld			#运行时不带class后缀
```



## 开发软件IDEA



