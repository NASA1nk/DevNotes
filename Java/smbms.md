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

   1. jsp
   2. Servlet
   3. mysql驱动

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
       <groupId>mysql</groupId>
       <artifactId>mysql-connector-java</artifactId>
       <version>5.1.47</version>
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
6. 创建工具类层：`com.ink.util`

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

2. 在`dao`目录下创建操作数据库的公共类`BaseDao.java`

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

3. 在filter目录下创建字符编码过滤器`CharacterEncodingFilter.java`并在`web.xml`中注册

   ```java
   public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
       servletRequest.setCharacterEncoding("utf-8");
       servletResponse.setCharacterEncoding("utf-8");
       filterChain.doFilter(servletRequest,servletResponse);
   }
   ```

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

存放在webapp目录下

> 不是`resource`目录



## 登录功能

![登录功能流程图](smbms.assets/登录功能流程图.png)

### 设置欢迎页

```xml
<!--    设置欢迎页-->
    <welcome-file-list>
        <welcome-file>login.jsp</welcome-file>
    </welcome-file-list>
```

### DAO层

在`com.ink.dao`目录下创建`user`目录

在`user`目录下创建`UserDao.java`作为获取登录用户信息的接口

```java
package com.ink.dao.user;

import com.ink.pojo.User;

import java.sql.Connection;

public interface UserDao {
//    得到登录的用户
    public User getLoginUser(Connection connection, String userCode) throws Exception;
}
```

在`user`目录下创建`UserDaoImpl.java`作为获取登录用户信息接口的实现类

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

在`com.ink.Service`目录下创建`user`目录

> 业务层都会调用DAO层，所以要引入DAO层

在`user`目录下创建`UserService.java`作为处理用户登录的接口

```java
package com.ink.service.user;

import com.ink.pojo.User;

public interface UserService {
//    处理用户登录
    public User login(String userCode,String password);
}
```

在`user`目录下创建`UserServiceImpl.java`作为处理用户登录接口的实现类

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

