# Dos命令

```bash
#盘符切换	D:
#查看当前目录文件	dir
#切换目录	 cd (change directory), 跨盘符需要加路径/ (cd /d f:\ink)
#返回上一级	cd ..
#退出终端	 exit
#清空窗口	 cls (clear screen)		
#查看ip	   ifconfig
#ping		ping www.baidu.com  可以得到其ip地址
#创建文件夹	 md ink (mkdir-make directory)
#删除文件夹	 rd ink (remove directory)
#创建文件	 cd> ink.txt
#删除文件	 del ink.txt
```

# Java

## 版本

跨平台运行（**JVM**）

- **Java SE** ：标准版	（桌面程序，控制台开发）
- **Java EE** ：企业级开发	（web端，服务器开发）

## JDK	JRE	JVM

- **JDK**：Java Development Kit	开发者工具（jdk包含了jre）

- **JRE**：Java Runtime Environment	运行时环境

- **JVM**：Java Virtual Machine	JAVA虚拟机

## Java开发环境

`JDK`：Java developmen kit	开发工具包

- 卸载JDK
  1. **查找jdk位置**：在环境变量中找到JAVA_HOME。
  2. **删除对应目录下文件**，然后删除JAVA_HOME,最后删除**PATH**中关于java的目录
  3. **验证**：`java -version`
- 安装JDK
  1. **下载**：直接搜索jdk8（可专门设置env文件夹存放）
  2. **配置环境变量**：在path中添加jdk\bin路径即可

> jdk11已经不用配置jre了
>
> bin目录下存放可执行程序exe，如java.exe,javac.exe

## 第一个程序

- **文件名**和**类名**保持**一致**

- **首字母大写**

进入`cmd`运行

```bash
javac HelloWorld.java	#编译	生成.class文件
java HelloWorld			#运行	不带class后缀
```

## 集成开发环境

IDE： `Integrated Development Environment`。一般包括编辑器，编译器，调试器和图形界面

### idea

1. 在**File**中new一个**Empty Project**，再new一个**module**

   ![Module](Java.assets/Module.png)

2. 查看项目结构Project Structure（也可以在File中查看）

   ![项目结构](Java.assets/项目结构.png)

3. 修改SDK（对应的Project Language Level 也要修改）

   ![修改sdk](Java.assets/修改sdk.png)

4. 在`src`目录下编写代码中

   ![hello](Java.assets/hello.png)

5. 快捷键

   - **psvm**：public static void main(String[] args)
   - **sout**：System.out.println()

   ```java
   public class hello {
       public static void main(String[] args) {
           System.out.println();
       }
   }
   ```

6. 运行

   ![运行程序](Java.assets/运行程序.png)

# 基础语法

## 注释

`Comments`

- 单行注释：line comment（快捷键`ctrl+/`）

  ```java
  //
  ```

- 多行注释：Block comment（快捷键`ctrl+shift+/`）

  ```java
  /**/
  ```

- 文档注释：**JavaDoc**（快捷键`/**+空格`）

  ```java
  /**
   * 
   */
  ```

> 搜	有趣的代码注释

### 修改注释

- 修改样式

  ![修改注释](Java.assets/修改注释.png)

- 修改字体颜色

  ![修改注释样式](Java.assets/修改注释样式.png)

## 标识符

Java所有的组成部分都需要起名，如类名，变量名，方法名...这些名字被称为**标识符**，不可以用**关键字**起名字。

> 关键字：public，static，class，void等

标识符

- 首字母只能是**字母**，**$**，**_**

- **大小写敏感**

> 标识符可以用中文（不推荐）String 工作 = "摸鱼"；

## 数据类型