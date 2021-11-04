# SMBMS

## 搭建项目

1. 创建Maven模板项目

2. 删除`pom.xml`无用信息，只保留gav和打包方式

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   
   <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
     <modelVersion>4.0.0</modelVersion>
   
     <groupId>com.ink</groupId>
     <artifactId>smbms</artifactId>
     <version>1.0-SNAPSHOT</version>
     <packaging>war</packaging>
   </project>
   ```

3. 修改`web.xml`

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
            version="5.0">
   
   </web-app>
   ```

4. 创建`java`目录和`resource`目录并标记为对应文件夹

5. 配置tomcat，路径设置为`/smbms`

6. 测试是否正常运行

7. 导入项目中需要的jar包

   1. `jsp`
   2. `jstl`
   3. `standard`
   4. `Servlet`
   5. mysql驱动
      1. `mysql-connector-java`
   
   > Tomcat10对应的jstl和standard包不一样
   
   ```xml
     <dependencies>
       <dependency>
         <groupId>jakarta.servlet.jsp</groupId>
         <artifactId>jakarta.servlet.jsp-api</artifactId>
         <version>3.0.0</version>
         <scope>provided</scope>
       </dependency>
       <dependency>
         <groupId>jakarta.servlet</groupId>
         <artifactId>jakarta.servlet-api</artifactId>
         <version>5.0.0</version>
         <scope>provided</scope>
       </dependency>
       <dependency>
         <groupId>javax.servlet.jsp.jstl</groupId>
         <artifactId>jstl</artifactId>
         <version>1.2</version>
       </dependency>
       <dependency>
         <groupId>taglibs</groupId>
         <artifactId>standard</artifactId>
         <version>1.1.2</version>
       </dependency>
       <dependency>
         <groupId>mysql</groupId>
         <artifactId>mysql-connector-java</artifactId>
         <version>5.1.47</version>
       </dependency>
       <dependency>
         <groupId>junit</groupId>
         <artifactId>junit</artifactId>
         <version>4.12</version>
       </dependency>
     </dependencies>
   
   ```

### 创建项目结构

创建package：`com.ink`

1. 创建实体类层：`com.ink.pojo`
2. 创建DAO层：`com.ink.dao`
3. 创建Service层：`com.ink.service`
4. 创建Servlet层：`com.ink.servlet`
5. 创建过滤器层：`com.ink.filter`
6. 创建工具类：`com.ink.util`

 ![init项目结构](smbms.assets/init项目结构.png)

### 创建数据库实体类

在`pojo`目录下创建对应数据库表的实体类

> orm映射

使用idea一键生成

1. `File-Project Structure-Modules`，点击加号，选择JPA

   ![选择创建实体类](smbms.assets/选择创建实体类.png)

2. `View-Tool Windows`，点击`Persistence`

    ![persistence](smbms.assets/persistence.png)

3. 选择`Generate Persistence Mapping-By Database Schema`

    ![persistencemapping](smbms.assets/persistencemapping.png)

4. 选择数据库，选择实体类生成的项目路径（包），勾选要生成实体的表和字段

    ![生成实体类](smbms.assets/生成实体类.png)



### 创建基础公共类

1. 在`resource`目录下创建数据库配置文件`db.properties`

2. 在`com.ink.dao`目录下创建操作数据库的公共类`BaseDao.java`

   1. 封装复用的数据库操作
      1. 数据库连接
      2. 数据库查询
      3. 数据库关闭

   ```java
   package com.ink.dao;
   
   import java.io.IOException;
   import java.io.InputStream;
   import java.sql.*;
   import java.util.Properties;
   
   //操作数据库的公共类
   public class BaseDao {
       private static String driver;
       private static String url;
       private static String user;
       private static String password;
   
   //    静态代码块,在类加载的时候执行,完成初始化
       static{
   //        初始化连接参数,从配置文件里获得
           Properties properties = new Properties();
           String configFile = "db.properties";
           InputStream is = BaseDao.class.getClassLoader().getResourceAsStream(configFile);
           try {
               properties.load(is);
           } catch (IOException e) {
               e.printStackTrace();
           }
           driver = properties.getProperty("driver");
           url = properties.getProperty("url");
           user = properties.getProperty("user");
           password = properties.getProperty("password");
       }
   
   
   //    获取数据库连接
       public static Connection getConnection(){
           Connection connection = null;
           try {
               Class.forName(driver);
               connection = DriverManager.getConnection(url, user, password);
           } catch (Exception e) {
               e.printStackTrace();
           }
           return connection;
       }
   
   //    查询公共类
   //    重载
       public static ResultSet execute(Connection connection,String sql,Object[] params,PreparedStatement preparedStatement,ResultSet resultSet) throws Exception{
           preparedStatement = connection.prepareStatement(sql);
           for(int i = 0; i < params.length; i++){
               preparedStatement.setObject(i+1, params[i]);
           }
           resultSet = preparedStatement.executeQuery();
           return resultSet;
       }
   
   //    增删改公共类
       public static int execute(Connection connection,String sql,Object[] params,PreparedStatement preparedStatement) throws Exception{
           preparedStatement = connection.prepareStatement(sql);
           for(int i = 0; i < params.length; i++){
               preparedStatement.setObject(i+1, params[i]);
           }
           int updateRows = preparedStatement.executeUpdate();
           return updateRows;
       }
   
   //    释放资源
       public static boolean closeResource(Connection connection,PreparedStatement preparedStatement,ResultSet resultSet){
           boolean flag = true;
           if(resultSet != null){
               try {
                   resultSet.close();
   //                GC回收
                   resultSet = null;
               } catch (SQLException e) {
                   e.printStackTrace();
   //                没有释放成功
                   flag = false;
               }
           }
           if(preparedStatement != null){
               try {
                   preparedStatement.close();
                   preparedStatement = null;
               } catch (SQLException e) {
                   e.printStackTrace();
                   flag = false;
               }
           }
           if(connection != null){
               try {
                   connection.close();
                   connection = null;
               } catch (SQLException e) {
                   e.printStackTrace();
                   flag = false;
               }
           }
           return flag;
       }
   }
   ```

3. 在`com.ink.filter`目录下创建`CharacterEncodingFilter.java`实现字符编码过滤功能

   ```java
   public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
       servletRequest.setCharacterEncoding("utf-8");
       servletResponse.setCharacterEncoding("utf-8");
       filterChain.doFilter(servletRequest,servletResponse);
   }
   ```

   在`web.xml`中注册

   ```xml
   <!--    字符编码过滤器-->
       <filter>
           <filter-name>CharacterEncodingFilter</filter-name>
           <filter-class>com.ink.filter.CharacterEncodingFilter</filter-class>
       </filter>
       <filter-mapping>
           <filter-name>CharacterEncodingFilter</filter-name>
           <url-pattern>/*</url-pattern>
       </filter-mapping>
   ```

### 导入静态资源

存放在`webapp`目录下

> 不是`resource`目录

### 设置欢迎页

`web.xml`

```xml
<!--    设置欢迎页-->
    <welcome-file-list>
        <welcome-file>login.jsp</welcome-file>
    </welcome-file-list>
```

## 登录

**项目编写逻辑：从底层向上写**

1. DAO层
2. Service层
3. Servlet层

![登录功能流程图](smbms.assets/登录功能流程图.png)

### DAO层

数据访问层：封装对数据库的访问

在`com.ink.dao`目录下创建`user`目录

在`com.ink.dao.user`目录下创建`UserDao.java`作为获取登录用户信息的接口

```java
package com.ink.dao.user;

import com.ink.pojo.User;

import java.sql.Connection;

public interface UserDao {
//    得到登录的用户
    public User getLoginUser(Connection connection, String userCode) throws Exception;
}
```

在`com.ink.dao.user`目录下创建`UserDaoImpl.java`作为获取登录用户信息接口的实现类

```java
package com.ink.dao.user;

import com.ink.dao.BaseDao;
import com.ink.pojo.User;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

//UserDao实现类
public class UserDaoiml implements UserDao{
    @Override
    public User getLoginUser(Connection connection, String userCode) throws Exception {
//        BaseDao中写好了查询的方法
        PreparedStatement pstm = null;
        ResultSet rs = null;
        User user = null;
        if(connection != null){
            String sql = "select * from smbms_user where userCode=?";
            Object[] params = {userCode};
            rs = BaseDao.execute(connection,pstm,rs,sql,params);
            if(rs.next()){
                user = new User();
                user.setId(rs.getInt("id"));
                user.setUserCode(rs.getString("userCode"));
                user.setUserName(rs.getString("userName"));
                user.setUserPassword(rs.getString("userPassword"));
                user.setGender(rs.getInt("gender"));
                user.setBirthday(rs.getDate("birthday"));
                user.setPhone(rs.getString("phone"));
                user.setAddress(rs.getString("address"));
                user.setUserRole(rs.getInt("userRole"));
                user.setCreatedBy(rs.getInt("createdBy"));
                user.setCreationDate(rs.getTimestamp("creationDate"));
                user.setModifyBy(rs.getInt("modifyBy"));
                user.setModifyDate(rs.getTimestamp("modifyDate"));
            }
//                connection不用关
            BaseDao.closeResource(null, pstm, rs);
        }
        return user;
    }
}
```

### Service层

业务层：调用数据访问层代码

在`com.ink.service`目录下创建`user`目录

在`com.ink.service.user`目录下创建`UserService.java`作为处理用户登录的接口

```java
package com.ink.service.user;

import com.ink.pojo.User;

public interface UserService {
//    处理用户登录
    public User login(String userCode,String password);
}
```

在`com.ink.service.user`目录下创建`UserServiceImpl.java`作为处理用户登录接口的实现类

- 业务层都会调用DAO层，所以要引入DAO层（创建对象）
- 父类引用指向子类对象：`userDao = new UserDaoImpl();`
- 使用`userDao`对象来调用DAO层的方法

```java
package com.ink.service.user;

import com.ink.dao.BaseDao;
import com.ink.dao.user.UserDao;
import com.ink.dao.user.UserDaoImpl;
import com.ink.pojo.User;
import org.junit.Test;

import java.sql.Connection;

public class UserServiceImpl implements UserService{
//    引入DAO层，用于调用
    private UserDao userDao;
    public UserServiceImpl(){
        userDao = new UserDaoImpl();
    }

    @Override
    public User login(String userCode, String password) {
        Connection connection = null;
        User user = null;
        try {
//            通过业务层调用对应的DAO层操作
            connection = BaseDao.getConnection();
            user = userDao.getLoginUser(connection,userCode);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
//          关闭connection
            BaseDao.closeResource(connection,null,null);
        }
        return user;
    }

//    直接测试
    @Test
   public void test() {
      UserServiceImpl userService = new UserServiceImpl();
      String userCode = "admin";
      String userPassword = "12345678";
      User admin = userService.login(userCode, userPassword);
      System.out.println(admin.getUserPassword());

   }
}
```

### Servlet层

控制层：调用Service层代码

在`com.ink.servlet`目录下创建`user`目录

在`com.ink.servlet.user`目录下创建`LoginServlet.java`实现用户登录功能

- `UserService userService = new UserServiceImpl();`

```java
package com.ink.servlet.user;

import com.ink.pojo.User;
import com.ink.service.user.UserService;
import com.ink.service.user.UserServiceImpl;
import com.ink.util.Constants;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

//控制层，调用业务层代码
public class LoginServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        获取前端请求的用户名和密码
        String userCode = req.getParameter("userCode");
        String password = req.getParameter("password");
//        调用业务层，和数据库中的数据进行对比
        UserService userService = new UserServiceImpl();
        User user = userService.login(userCode, password);
        if(user != null){
//            用户存在，将用户信息存入Session，然后跳转首页
//            常量抽取出来放在工具包util的类中
            req.getSession().setAttribute(Constants.USER_SESSION,user);
            resp.sendRedirect("jsp/frame.jsp");
        }
        else{
//            用户不存在，转发到登录页，并提示错误
//            设置error信息
            req.setAttribute("error","用户名或密码错误");
            req.getRequestDispatcher("login.jsp").forward(req,resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
```

在`com.ink.servlet.user`目录下创建`LogoutServlet.java`控制用户登录的注销功能

```java
package com.ink.servlet.user;

import com.ink.util.Constants;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

public class LogoutServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        清除session的用户数据
        req.getSession().removeAttribute(Constants.USER_SESSION);
//        返回登录页面
        resp.sendRedirect(req.getContextPath()+"/login.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
```

在`web.xml`中注册

```xml
<servlet>
    <servlet-name>LoginServlet</servlet-name>
    <servlet-class>com.ink.servlet.user.LoginServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>LoginServlet</servlet-name>
    <url-pattern>/login.do</url-pattern>
</servlet-mapping>
<servlet>
    <servlet-name>LogoutServlet</servlet-name>
    <servlet-class>com.ink.servlet.user.LogoutServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>LogoutServlet</servlet-name>
    <url-pattern>/jsp/logout.do</url-pattern>
</servlet-mapping>
```

### 权限验证

使用拦截器防止未登录用户访问主页

在`com.ink.filter`目录下创建`LoginFilter.java`实现权限验证功能

- 传递请求：`filterChain.doFilter(servletRequest,servletResponse);`

```java
package com.ink.filter;

import com.ink.pojo.User;
import com.ink.util.Constants;
import jakarta.servlet.*;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

public class LoginFilter implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        Filter.super.init(filterConfig);
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest req = (HttpServletRequest) servletRequest;
        HttpServletResponse resp = (HttpServletResponse) servletResponse;
//        从session中获取用户
        User user = (User) req.getSession().getAttribute(Constants.USER_SESSION);
        if(user == null){
//            用户未登录或者已经注销了
            resp.sendRedirect(req.getContextPath()+"error.jsp");
        }
        else{
            filterChain.doFilter(servletRequest,servletResponse);
        }
    }

    @Override
    public void destroy() {
        Filter.super.destroy();
    }
}
```

在`web.xml`中注册

```xml
<filter>
    <filter-name>LoginFilter</filter-name>
    <filter-class>com.ink.filter.LoginFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoginFilter</filter-name>
    <url-pattern>/jsp/*</url-pattern>
</filter-mapping>
```

## 密码修改

### DAO层

修改`com.ink.dao.user`目录下的`UserDao.java`接口

- 增加修改密码功能对应的方法

```java
//    修改当前用户密码
    public int updatePwd(Connection connection, int id, int password)throws SQLException, Exception;
```

修改`com.ink.dao.user`目录下的`UserDaoImpl.java`实现类

- 重写对应的方法

```java
    @Override
    public int updatePwd(Connection connection, int id, String password) throws SQLException, Exception {
        System.out.println("UserDao" + password);
        PreparedStatement pstm = null;
        int execute = 0;
        if(connection != null){
            String sql = "update smbms_user set userPassword = ? where id = ?";
            Object[] param = {password, id};
            execute = BaseDao.execute(connection,pstm,sql,param);
            BaseDao.closeResource(null,pstm,null);
        }
        return execute;
    }
```

### Service层

修改`com.ink.service.user`目录下的`Userservice.java`接口

- 增加修改密码功能对应的方法

```java
//    修改当前用户密码
    public boolean updatePwd(int id,String password) throws SQLException;
```

修改`com.ink.service.user`目录下的`UserServiceImpl.java`实现类

- 重写对应的方法

```java
    @Override
    public boolean updatePwd(int id, String password) throws SQLException {
        System.out.println("UserService" + password);

        Connection connection = BaseDao.getConnection();
        boolean flag = false;
        try {
            int execute = userDao.updatePwd(connection, id, password);
            if(execute > 0){
                flag = true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            BaseDao.closeResource(connection,null,null);
        }
        return flag;
    }
```

### Servlet层

#### 修改新密码

业务实现

1. 在用户登录时，已经将用户的信息存入了Session
   1. `req.getSession().setAttribute(Constants.USER_SESSION,user);`
2. 可以使用Session中的`Constants.USER_SESSION`获取user信息
3. 去数据库中修改密码

在`com.ink.servlet.user`目录下创建`UserServlet.java`实现修改密码功能

```java
package com.ink.servlet.user;

import com.ink.pojo.User;
import com.ink.service.user.UserService;
import com.ink.service.user.UserServiceImpl;
import com.ink.util.Constants;
import com.mysql.jdbc.StringUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.SQLException;

public class UserServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        先不要强制类型转换，等用的时候再转换
        Object o = req.getSession().getAttribute(Constants.USER_SESSION);
        String newpassword = req.getParameter("newpassword");

        System.out.println("UserServlet" + newpassword);

        boolean flag = false;
//        如果用户存在且新密码不为空
//        o != null && newpassword != null && newpassword.length() != 0
//        StringUtils，jdbc的工具类
        if(o != null && !StringUtils.isNullOrEmpty(newpassword)){
//            调用service层代码
            UserService userService = new UserServiceImpl();
            try {
                flag = userService.updatePwd(((User)o).getId() , newpassword);
            } catch (SQLException e) {
                e.printStackTrace();
            }
            if(flag){
                req.setAttribute("message","密码修改成功，请重新登录");
//                移除当前Session，重新登录
                req.getSession().removeAttribute(Constants.USER_SESSION);
            }
            else{
                req.setAttribute("message","密码修改失败");
            }
        }
        else{
            req.setAttribute("message","新密码存在问题");
        }
        resp.sendRedirect(req.getContextPath()+"/error.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }
}
```

在`web.xml`中注册

```xml
<servlet>
    <servlet-name>UserServlet</servlet-name>
    <servlet-class>com.ink.servlet.user.UserServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>UserServlet</servlet-name>
    <url-pattern>/jsp/user.do</url-pattern>
</servlet-mapping>
```

#### Servlet复用

如何实现Servlet复用？

- 根据前端页面不同的操作，将对应的操作的值当成参数传给后端

  ```javascript
  <input type="hidden" name="method" value="savepwd">
  ```

- 不同的业务抽取出不同的方法，然后根据值调用不同的方法

  ```java
  package com.ink.servlet.user;
  
  import com.ink.pojo.User;
  import com.ink.service.user.UserService;
  import com.ink.service.user.UserServiceImpl;
  import com.ink.util.Constants;
  import com.mysql.jdbc.StringUtils;
  import jakarta.servlet.ServletException;
  import jakarta.servlet.http.HttpServlet;
  import jakarta.servlet.http.HttpServletRequest;
  import jakarta.servlet.http.HttpServletResponse;
  
  import java.io.IOException;
  import java.sql.SQLException;
  
  public class UserServlet extends HttpServlet {
      @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
  //        实现Servlet复用
          String method = req.getParameter("method");
          if(method != null && ("savepwd").equals(method)){
              this.updatePwd(req,resp);
          }
      }
  
      @Override
      protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
          doGet(req, resp);
      }
  
  //    具体的修改密码的方法
      public void updatePwd(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
  //        先不要强制类型转换，等用的时候再转换
          Object o = req.getSession().getAttribute(Constants.USER_SESSION);
          String newpassword = req.getParameter("newpassword");
  
          boolean flag = false;
  //        如果用户存在且新密码不为空
  //        o != null && newpassword != null && newpassword.length() != 0
  //        StringUtils，jdbc的工具类
          if(o != null && !StringUtils.isNullOrEmpty(newpassword)){
  //            调用service层代码
              UserService userService = new UserServiceImpl();
              try {
                  flag = userService.updatePwd(((User)o).getId(),newpassword);
              } catch (SQLException e) {
                  e.printStackTrace();
              }
              if(flag){
                  req.setAttribute("message","密码修改成功，请重新登录");
  //                移除当前Session，重新登录
                  req.getSession().removeAttribute(Constants.USER_SESSION);
              }
              else{
                  req.setAttribute("message","密码修改失败");
              }
          }
          else{
              req.setAttribute("message","新密码存在问题");
          }
          req.getRequestDispatcher("/error.jsp").forward(req,resp);
      }
  }
  ```

#### 验证旧密码

当旧密码输入框失去焦点时（即输入旧密码结束，开始输入新密码），使用Ajax向后端发送请求验证，通过回调函数对应处理

> 旧密码一般还是要验证数据库的。因为还有app等多端，或者多台设备登录同一个账号，只要有一处修改了密码，其他端的Session和数据库中的密码肯定都不一致了

```javascript
oldpassword.on("blur",function(){
   $.ajax({
      type:"GET",
      url:path+"/jsp/user.do",
      data:{method:"pwdmodify",oldpassword:oldpassword.val()},
         success:function(data){
         if(data.result == "true"){//旧密码正确
            validateTip(oldpassword.next(),{"color":"green"},imgYes,true);
         }else if(data.result == "false"){//旧密码输入不正确
            validateTip(oldpassword.next(),{"color":"red"},imgNo + " 原密码输入不正确",false);
         }else if(data.result == "sessionerror"){//当前用户session过期，请重新登录
            validateTip(oldpassword.next(),{"color":"red"},imgNo + " 当前用户session过期，请重新登录",false);
         }else if(data.result == "error"){//旧密码输入为空
            validateTip(oldpassword.next(),{"color":"red"},imgNo + " 请输入旧密码",false);
         }
      },
      error:function(data){
         //请求出错
         validateTip(oldpassword.next(),{"color":"red"},imgNo + " 请求错误",false);
      }
   });
```

在`pom.xml`中导入fastjson依赖

```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/fastjson -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.78</version>
</dependency>
```

在`web.xml`中设置Session过期时间

```xml
<!--    设置Session过期时间-->
    <session-config>
        <session-timeout>30</session-timeout>
    </session-config>
```

在`com.ink.servlet.user`目录下的`UserServlet.java`增加验证旧密码的复用功能

- 返回数据需要转化为json格式

> 返回数据为json键值对格式，所以使用map可以很方便的对应起来

```java
package com.ink.servlet.user;

import com.alibaba.fastjson.JSONArray;
import com.ink.pojo.User;
import com.ink.service.user.UserService;
import com.ink.service.user.UserServiceImpl;
import com.ink.util.Constants;
import com.mysql.jdbc.StringUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import javax.jms.Session;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.util.HashMap;

public class UserServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        实现Servlet复用
        String method = req.getParameter("method");
        if(method != null && ("savepwd").equals(method)){
            this.updatePwd(req,resp);
        }
        else if(method != null && ("pwdmodify").equals(method)){
            this.pwdModify(req,resp);
        }
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }

//    具体的修改密码的方法
    public void updatePwd(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        先不要强制类型转换，等用的时候再转换
        Object o = req.getSession().getAttribute(Constants.USER_SESSION);
        String newpassword = req.getParameter("newpassword");

        boolean flag = false;
//        如果用户存在且新密码不为空
//        o != null && newpassword != null && newpassword.length() != 0
//        StringUtils，jdbc的工具类
        if(o != null && !StringUtils.isNullOrEmpty(newpassword)){
//            调用service层代码
            UserService userService = new UserServiceImpl();
            try {
                flag = userService.updatePwd(((User)o).getId(),newpassword);
            } catch (SQLException e) {
                e.printStackTrace();
            }
            if(flag){
                req.setAttribute("message","密码修改成功，请重新登录");
//                移除当前Session，重新登录
                req.getSession().removeAttribute(Constants.USER_SESSION);
            }
            else{
                req.setAttribute("message","密码修改失败");
            }
        }
        else{
            req.setAttribute("message","新密码存在问题");
        }
        resp.sendRedirect(req.getContextPath()+"/error.jsp");
    }

//    具体的验证旧密码的方法
    public void pwdModify(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        Object o = req.getSession().getAttribute(Constants.USER_SESSION);
        String oldpassword = req.getParameter("oldpassword");

        HashMap<String,String> resultMap = new HashMap<>();
//        session失效
        if(o == null){
//            Session过期或失效
            resultMap.put("result","sessionerror");
        }
        else if(StringUtils.isNullOrEmpty(oldpassword)){
            resultMap.put("result","error");
        }
        else{
//            从Session中获取密码并比较
            String userPassword = ((User)o).getUserPassword();
            if(oldpassword.equals(userPassword)){
                resultMap.put("result","true");
            }
            else{
                resultMap.put("result","false");
            }
        }
        try {
//        设置响应json数据
            resp.setContentType("application/json");
//        获取输出流
            PrintWriter writer = resp.getWriter();
//        JSONArray，阿里巴巴的json工具类，用于转换格式
            writer.write(JSONArray.toJSONString(resultMap));
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## 用户管理

![用户管理流程](smbms.assets/用户管理流程.png)

### 查询用户

使用拼接sql实现

- 根据用户名查询用户
- 根据用户角色查询用户
- 根据用户名和用户角色查询用户

#### DAO层

修改`com.ink.dao.user`目录下的`UserDao.java`接口

- 增加查询用户功能对应的方法

```java
//    根据用户名或者角色查询用户总数
    public int getUserCount(Connection connection,String userName ,int userRole)throws SQLException, Exception;
```

修改`com.ink.dao.user`目录下的`UserDaoImpl.java`实现类

- 重写对应的方法

> SQL参数问题
>
> 1. 使用`list`根据判断依次存放参数
> 2. 最后将`list`转换为`Object`数组传递给SQL

```java
    @Override
    public int getUserCount(Connection connection, String userName, int userRole) throws SQLException, Exception {
        PreparedStatement pstm = null;
        ResultSet rs = null;
        int count = 0;
        if(connection != null){
            StringBuilder sql = new StringBuilder();
            sql.append("select count(1) as count from smbms_user u,smbms_role r where u.userRole = r.id");
//            因为不确定2个参数的情况，要用list存放参数
            ArrayList<Object> list = new ArrayList<>();
//            用用户名查询
            if(!StringUtils.isNullOrEmpty(userName)){
//                like模糊查询
                sql.append("and u.userName like ?");
//                传递的用户名需要有占位符
                list.add("%"+userName+"%");
            }
            if(userRole > 0){
                sql.append("and u.userRole = ?");
                list.add(userRole);
            }
//            将list转换为数组
            Object[] params = list.toArray();

//            调试
            System.out.println("UserDao->getUserCount："+sql.toString());
            rs = BaseDao.execute(connection, pstm, rs, sql.toString(), params);
            if(rs.next()){
                count = rs.getInt("count");
            }
            BaseDao.closeResource(null,pstm,rs);
        }
        return count;
    }
```

#### Service层

修改`com.ink.service.user`目录下的`Userservice.java`接口

- 增加查询用户功能对应的方法

```java
//    查询用户数量
    public int getUserCount(String userName, int userRole);
```

修改`com.ink.service.user`目录下的`UserServiceImpl.java`实现类

- 重写对应的方法

```java
@Override
public int getUserCount(String userName, int userRole) {
    Connection connection = null;
    int count = 0;
    try {
        connection = BaseDao.getConnection();
        count = userDao.getUserCount(connection, userName, userRole);
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        BaseDao.closeResource(connection,null,null);
    }
    return count;
}
```

**测试**

- 直接在`UserServiceImpl.java`中测试

```java
   //    直接测试
   @Test
public void test() {
   UserServiceImpl userService = new UserServiceImpl();
       int userCount = userService.getUserCount(null, 1);
       int userCount2 = userService.getUserCount("张", 3);
       System.out.println(userCount);
       System.out.println(userCount2);
   }
```

### 分页

在`com.ink.util`目录下创建用于分页的工具类`PageSupport.java`

- 一系列的`set()`方法用于设置内部值，需要在内部判断参数是否合理

```java
package com.ink.util;

public class PageSupport {
// 当前页码（来自于用户输入）
   private int currentPageNo = 1;
   
// 总数量（表）
   private int totalCount = 0;
   
// 页面大小
   private int pageSize = 0;
   
// 总页数（totalCount/pageSize（+1））
   private int totalPageCount = 1;

   public int getCurrentPageNo() {
      return currentPageNo;
   }

// 面向对象：封装
// 在set()方法中检测设置的值的合法性
// 减少业务代码
   public void setCurrentPageNo(int currentPageNo) {
      if(currentPageNo > 0){
         this.currentPageNo = currentPageNo;
      }
   }

   public int getTotalCount() {
      return totalCount;
   }

   public void setTotalCount(int totalCount) {
      if(totalCount > 0){
         this.totalCount = totalCount;
//       设置总页数
         this.setTotalPageCountByRs();
      }
   }
   public int getPageSize() {
      return pageSize;
   }

   public void setPageSize(int pageSize) {
      if(pageSize > 0){
         this.pageSize = pageSize;
      }
   }

   public int getTotalPageCount() {
      return totalPageCount;
   }

   public void setTotalPageCount(int totalPageCount) {
      this.totalPageCount = totalPageCount;
   }
   
   public void setTotalPageCountByRs(){
      if(this.totalCount % this.pageSize == 0){
         this.totalPageCount = this.totalCount / this.pageSize;
      }else if(this.totalCount % this.pageSize > 0){
         this.totalPageCount = this.totalCount / this.pageSize + 1;
      }else{
         this.totalPageCount = 0;
      }
   } 
}
```

### 获取用户列表

#### DAO层

修改`com.ink.dao.user`目录下的`UserDao.java`接口

- 增加查询用户列表功能对应的方法

```java
//    通过条件查询用户列表（分页功能）
    public List<User> getUserList(Connection connection, String userName, int userRole, int currentPageNo, int pageSize)throws Exception;
```

修改`com.ink.dao.user`目录下的`UserDaoImpl.java`实现类

- 重写对应的方法

> 分页功能
>
> - 当前页 = (当前页-1) * 页面大小
>
> `limit n,m`
>
> - 指定返回从n开始的m col（闭区间[n,n+m]）

```java
    @Override
    public List<User> getUserList(Connection connection, String userName, int userRole, int currentPageNo, int pageSize) throws Exception {
        PreparedStatement pstm = null;
        ResultSet rs = null;
//        接收查询返回的用户列表
        List<User> userList = new ArrayList<User>();

        if(connection != null){
            StringBuffer sql = new StringBuffer();
            sql.append("select u.*, r.roleName as userRoleName from smbms_user u,smbms_role r where u.userRole = r.id");
//            用list存放查询参数
            List<Object> list = new ArrayList<Object>();
            if(!StringUtils.isNullOrEmpty(userName)){
                sql.append(" and u.userName like ?");
                list.add("%"+userName+"%");
            }
            if(userRole > 0){
                sql.append(" and u.userRole = ?");
                list.add(userRole);
            }
//            实现分页查询
            sql.append(" order by creationDate DESC limit ?,?");
//            当前页
            currentPageNo = (currentPageNo - 1) * pageSize;
            list.add(currentPageNo);
            list.add(pageSize);
            Object[] params = list.toArray();
            System.out.println("sql：" + sql.toString());
            rs = BaseDao.execute(connection, pstm, rs, sql.toString(), params);
            while(rs.next()){
                User _user = new User();
                _user.setId(rs.getInt("id"));
                _user.setUserCode(rs.getString("userCode"));
                _user.setUserName(rs.getString("userName"));
                _user.setGender(rs.getInt("gender"));
                _user.setBirthday(rs.getDate("birthday"));
                _user.setPhone(rs.getString("phone"));
                _user.setUserRole(rs.getInt("userRole"));
                _user.setUserRoleName(rs.getString("userRoleName"));
                userList.add(_user);
            }
            BaseDao.closeResource(null, pstm, rs);
        }
        return userList;
    }
```

#### Service层

修改`com.ink.service.user`目录下的`UserService.java`接口

- 增加查询用户列表功能对应的方法

```java
//    根据条件查询用户列表（分页）
    public List<User> getUserList(String queryUserName, int queryUserRole, int currentPageNo, int pageSize);
```

修改`com.ink.service.user`目录下的`UserServiceImpl.java`实现类

- 重写对应的方法

```java
@Override
public List<User> getUserList(String queryUserName, int queryUserRole, int currentPageNo, int pageSize) {
    Connection connection = null;
    List<User> userList = null;

        System.out.println("queryUserName：" + queryUserName);
        System.out.println("queryUserRole：" + queryUserRole);
        System.out.println("currentPageNo：" + currentPageNo);
        System.out.println("pageSize：" + pageSize);
    
    try {
        connection = BaseDao.getConnection();
        userList = userDao.getUserList(connection,queryUserName,queryUserRole,currentPageNo,pageSize);
    } catch (Exception e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }finally{
        BaseDao.closeResource(connection, null, null);
    }
    return userList;
}
```



### 获取角色列表

#### 建包规范

1. 一般pojo目录下的实体类对应数据库的表
2. 然后在DAO包，Service包，Servlet包下应该分别对pojo目录下的实体类建立对应的包来，也正好对应实体类对应的表

前面的功能是针对用户，基本上都是操作`User`表，所以在`user`包下。所以针对角色就应该在`DAO`包，`Service`包，`Servlet`包下建立`role`包

#### DAO层

在`com.ink.dao.role`目录下创建`RoleDao.java`做为获取角色列表的接口

```java
package com.ink.dao.role;

import com.ink.pojo.Role;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import java.util.List;

public interface RoleDao {
//    获取角色列表
    public List<Role> getRoleList(Connection connection) throws SQLException;
}
```

在`com.ink.dao.role`目录下创建`RoleDaoImpl.java`做为获取角色列表的接口的实现类

```java
package com.ink.dao.role;

import com.ink.dao.BaseDao;
import com.ink.pojo.Role;
import org.junit.Test;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class RoleDaoImpl implements RoleDao{
    @Override
    public List<Role> getRoleList(Connection connection) throws Exception {
        PreparedStatement pstm = null;
        ResultSet rs = null;
        List<Role> roleList = new ArrayList<Role>();
        if (connection != null) {
            String sql = "select * from smbms_role";
            Object[] params = {};
            rs = BaseDao.execute(connection, pstm, rs, sql, params);
            while (rs.next()) {
                Role _role = new Role();
                _role.setId(rs.getInt("id"));
                _role.setRoleCode(rs.getString("roleCode"));
                _role.setRoleName(rs.getString("roleName"));
                roleList.add(_role);
            }
            BaseDao.closeResource(null, pstm, rs);
        }
        return roleList;
    }

    @Test
    public void test() throws Exception {
        RoleDao roleDao = new RoleDaoImpl();
        Connection connection = BaseDao.getConnection();
        List<Role> roleList = roleDao.getRoleList(connection);
        for(Role t: roleList){
            System.out.println(t.toString());
        }
    }
}
```

#### Service层

在`com.ink.service.role`目录下创建`RoleService.java`作为获取角色列表的接口

```java
package com.ink.service.role;

import com.ink.pojo.Role;

import java.sql.Connection;
import java.util.List;

public interface RoleService {
    //    获取角色列表
    public List<Role> getRoleList();
}
```

在`com.ink.service.role`目录下创建`RoleServiceImpl.java`做为获取角色列表的接口的实现类

```java
package com.ink.service.role;

import com.ink.dao.BaseDao;
import com.ink.dao.role.RoleDao;
import com.ink.dao.role.RoleDaoImpl;
import com.ink.pojo.Role;

import java.sql.Connection;
import java.util.List;

public class RoleServiceImpl implements RoleService{

//    引入DAO
    private RoleDao roleDao;
    public RoleServiceImpl() {
        roleDao = new RoleDaoImpl();
    }

    @Override
    public List<Role> getRoleList() {
        Connection connection = null;
        List<Role> roleList = null;
        try {
            connection = BaseDao.getConnection();
            roleList = roleDao.getRoleList(connection);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            BaseDao.closeResource(connection,null,null);
        }
        return roleList;
    }
}
```

## Servlet层

