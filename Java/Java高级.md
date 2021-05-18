# 多线程

# 常用类

## String类

**不可变的字符序列**

Java程序中所有的**字符串**的字面值都是`String`类的一个实例

- `String`是一个`final`类，它无法被继承
- `String`对象的字符内容存储在一个字符数组`value[]`中（`private final`类型的数组）
- `String`实现了`Serializable`接口，表示字符串是可以序列化的（IO流）
- `String`实现了`Comparable`接口，表示字符串是可以比较大小
- 字符串是**常量**，创建后**不能更改**
  - 当对字符串重新**赋值**时，需要重新指定内存区域
  - 当对字符串进行**拼接**时，需要重新指定内存区域
  - 当对字符串进行**替换**时，需要重新指定内存区域

> 方法区中包含字符串常量池，常量池不会存储相同内容的字符串

![String](Java高级.assets/String.png)



### 字符串修改

**值传递**：引用数据类型传递的是地址值

- `str`将自己指向的地址传递给了`change`方法。`str`有不可变性，所以`str`不会变
- `ch`指向堆中的一片区域，可以在方法中改变

```java
package com.ink.String;

public class Test {
    String str = new String("good");
    char[] ch = {'t','e','s','t'};
    public void change(String str,char[] ch){
        str = "ok";
        ch[0] = 'b';
    }
    public static void main(String[] args) {
        Test ex = new Test();
        ex.change(ex.str,ex.ch);
        System.out.println(ex.str + "and" + ex.ch);
    }
}
```

![String修改](Java高级.assets/String修改.png)

> 如果将 `str = "ok";`改为`this. str = "ok";`就会一起改变！



### 字符串实例化方法

- **字面量定义**

  - 字符串常量**存储在常量池**中共享

- **`new`+构造器**

  - 字符串**非常量对象存储在堆中**，保存堆空间地址，由**堆中的对象指向常量池**

    > 相当于创建了两个对象，一个是堆中的`new`结构，一个是`char[]`对应的常量池中的数据

```java
package com.ink.String;

import java.util.Arrays;

public class Astring {
    // 常量池声明
    String str = "abc";
    
    //  this.value = new char[0];
    String s1 = new String();
    
    // this.value = original.value;
    String s2 = new String(String original);
    
    // this.value = ArrayscopyOf(value,value.length);
    String s3 = new String(char[] s);
    
    String s4 = new String(char[] s, int startIndex, int count);

}
```



### 字符串比较

- `==`：比较字符串的**地址值**
- `equals`：比较字符串的**内容**，`String`类重写了`equals`方法



### 字符串拼接

- **字面量**值拼接

  常量和常量的拼接结果在常量池中

- 存在**变量**参与拼接

  只要存在一个变量，结果就在堆中

  > `final`定义的变量是常量！拼接结果在常量池中

```java
package com.ink.String;

public class Astring {
    public static void main(String[] args) {
        String s1 = "abc";
        String s2 = "def";
        String s3 = "abcdef";
        String s4 = s1 + "def";
        String s5 = "abc" + s2;
        String s6 = "abc" + "def";
        System.out.println(s3 == s4);
        System.out.println(s3 == s5);
        System.out.println(s3 == s6);
        System.out.println(s4 == s6);
        String s7 = s5.intern();
        System.out.println(s3 == s7);
    }
}
```

![String拼接](Java高级.assets/String拼接.png)

如果拼接结果调用`intern()`方法，**返回值在常量池中**

```java
// true
String s7 = s5.intern();
System.out.println(s3 == s7);
```



### 常用方法

- `int length()`：返回字符串长度
- `char charAt(int index)`：返回索引处的字符
- `boolean isEmpty()`：判断字符串是否为空
- `String toLowerCase()`：将字符串中所有字符转换为小写
- `String toUpperCase()`：将字符串中所有字符转换为大写
- `String trim()`：返回字符串的副本，忽略**所有前导空格和尾部空格**（中间的空格不变）
- `boolean equals(Object obj)`：比较字符串内容是否相同
- `boolean equalsIgnoreCase(Object obj)`：忽略大小写，比较字符串内容是否相同
- `String concat(String str)`：将字符串连接到此字符串的尾部，**等价于"+"**
- `int compareTo(String anotherString)`：比较两个字符串的大小（`Comparable`接口中的抽象方法）
- `String substring(int beginIndex)`：从此字符串的beginIndex开始，返回一个新字符串
- `String substring(int beginIndex,int endIndex)`：从此字符串的beginIndex开始，endIndex结束，返回一个新字符串
- `boolean contains(CharSequence s)`：当且仅当此字符串包含指定的char值序列时，返回true
- `String replace(char oldChar,char newChar)`：用新的字符替换字符串中**所有的旧字符**，返回新的字符串
- `String replace(CharSequence target,CharSequence replacement)`：用指定的字面值替换字符串中所有匹配字面值的子字符串，返回新的字符串
- `String split(String regex)`：根据给定的**正则表达式**的匹配拆分字符串



### 类型转换

String类和**其他结构**之间的转换

> 只有子父类**继承关系**的类型才可以强制类型转换



**String转换为基本数据类型（包装类）**

调用包装类的**静态方法**：`Integer.parseInt(str)`



**基本数据类型（包装类）转换为String**

调用String重载的`valueOf()`方法：`String.valueOf(num)`

也可以直接**拼接**：`num + ""`

> 拼接的字符串在堆中（有变量），不在常量池中



**String转换为字符数组（char[]）**

> String的底层就是一个char[]

调用String的`toCharArray()`方法



**字符数组（char[]）转换为String**

调用String的**构造器**即可：`new String(char[])`



**String转换为字节数组（byte[]）**

调用String的`getBytes()`方法（默认的字符编码集）

`getBytes(charsetName)`：指定字符编码集

> UTF-8下，一个汉字三个字节
>
> GBK下，一个汉字两个字节



**字节数组（byte[]）转换为String**

调用String的**构造器**即可：`new String(byte[])`



## StringBuffer类

- **可变的字符序列**
- **线程安全的**
- **效率低**

`StringBuffer`对象的字符内容存储在一个字符数组`value[]`中（没有`final`修饰，可变）



### StringBuffer源码

1. **无参构造**

   无参的构造器会初始化**长度为16**的char数组

   ![StringBuffer源码](Java高级.assets/StringBuffer源码.png)

2. **有参构造**

   有参的构造器会初始化**长度为参数长度+16**的char数组

   ![StringBuffer有参构造](Java高级.assets/StringBuffer有参构造.png)

3. **字符串长度**

   `.length()`方法还是返回**实际长度**（`.append()`就+1），而不是`value.length`

   ![StringBuffer.length6](Java高级.assets/StringBuffer.length.png)

4. **数组扩容**

   1. 调用的是超类的`append()`方法

      ![append()](Java高级.assets/append().png)

   2. 超类的`append()`方法

      判断已有长度和添加的长度和是否超过数组长度

      ![超类append](Java高级.assets/超类append.png)

   3. 如果超过数组长度，调用`copyOf()`方法**复制数据**

      ![ensureCapacityInternal](Java高级.assets/ensureCapacityInternal.png)

   4. 在创建新的数组时候扩容

      默认情况是`(old.length << 1)+2`

      > 会有**特殊情况**，比如扩容后还是不够，或者超过最大长度...

      ![newCapacity](Java高级.assets/newCapacity.png)

   

   

   

### StringBuffer方法

查看StringBuffer的所有方法

**快捷键**：ctrl+F12

![StringBuffer方法](Java高级.assets/StringBuffer方法.png)



- `StringBuidler append(obj)`：字符串拼接
- `StringBuffer delete(int start,int end)`：删除指定位置内容
- `StringBuffer replace(int start,int end,String str)`：把**[start,end)**位置的内容替换为str
- `StringBuffer insert(int offset,obj)`：字符插入
- `StringBuffer reverse()`：反转字符串

调用`append()`和`insert()`时，如果原来的数组长度不够，可以扩容

> `append(null)`会将null转换为**"null"字符串**添加进去
>
> 如果将null作为构造器参数，则会抛**空指针异常**



**这些方法支持方法链操作**

**方法链**

可以...一直调用（**返回this**）

![方法链](Java高级.assets/方法链.png)



## StringBuidler类

- **可变的字符序列**
- **线程不安全的，效率高**

> JDK5.0新增
>
> 不涉及线程的时候（不考虑线程安全时），优先使用

`StringBuidler`对象的字符内容存储在一个字符数组`value[]`中（没有`final`修饰，可变）



**效率**：**StringBuidler > StringBuidler > String**



## System类

`java.lang.System`

> JDK8之前日期和时间的API

日期方法：返回**时间戳**

`public static long currentTimeMillis()`

返回**当前时间**和1970年1月1日0时0分0秒之间的时间差（以**毫秒**为单位）



## Date类

`java.util.Date`

> JDK8之前的日期时间API
>
> 还有一个`java.sql.Date`类，对应**数据库**中的日期类型变量



### Date构造器

- `Date()`：无参构造器创建一个对应**当前时间**的Date对象

- `Date(long date)`：有参构造器创建一个对应**指定时间**（毫秒数）的Date对象

  > `@Deprecated` ：注解，过时，但还能用

```java
package com.ink.Date;

import java.util.Date;

public class DateTest {
    public static void main(String[] args) {
        Date date1 = new Date();
        System.out.println(date1);
        System.out.println(date1.getTime());
        Date date2 = new Date(1618391227838l);
        System.out.println(date2);
    }
}
```

![Date类](Java高级.assets/Date类.png)



### Date方法

- `getTime()`：返回**当前时间**和1970年1月1日0时0分0秒之间的时间差（以**毫秒**为单位）

- `toString()`

  把Date对象转换为dow month day hour:minute:second zzz year格式

  - dow：day of week
  - zzz：时间标准

  > `Date`类重写了`toString()`方法



## SimpleDateFormat类

`java.text.SimpleDateFormat`

> JDK8之前的日期时间API
>
> Date类的API不易于国际化，大部分都废弃不用了，

`SimpleDateFormat`类是一个用**和语言环境无关的方式**来**格式化和解析**日期的类（对`java.util.Date`类进行操作）

- 无参构造
- 有参构造：`pattern`规定生成日期格式

 

### 日期格式化

**日期 -> 文本（字符串）**

`format()`方法

```java
package com.ink.Date;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.SimpleTimeZone;

public class DateTest {
    public static void main(String[] args) {
        Date date1 = new Date();
        System.out.println(date1);
        // 默认构造器
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat();
        String format = simpleDateFormat.format(date1);
        System.out.println(format);
    }
}
```

![SimpleDateFormat](Java高级.assets/SimpleDateFormat.png)



### 日期解析

**文本（字符串） -> 日期**

> 字符串要求：年-月-日 a/pm hour:minute
>
> 格式化输出的字符串就是默认的形式

`parse()`方法

```java
// 输出Wed Apr 14 17:33:00 CST 2021
String str = "2021/4/14 下午5:33";
try {
    Date parse = simpleDateFormat.parse(str);
    System.out.println(parse);
}catch (ParseException e){
    System.out.println("exception");
}
```



## Calendar类

`Calendar`（日历类）是一个**抽象类**，主要用于完成日期字段之间相互操作的功能。 

![Calendar](Java高级.assets/Calendar.png)

**抽象类不可以实例化**

- 调用它的**子类**：`GregorianCalendar`

- 调用它的**静态方法**：`Calendar.getInstance()`

  调用静态方法返回子类`GregorianCalendar`对象

  ![GregorianCalendar](Java高级.assets/GregorianCalendar.png)



### Calendar方法

一个`Calendar`的实例是系统时间的抽象表示，通过get(int field)方法来取得想要的时间信息，比如YEAR，MONTH，DAT_OF_WEEK，HOUR_OF_DAY，MINUTE，SECOND

> 查看API文档，`Calendar`类中定义了很多常量属性



**对Calendar对象操作**

- `get()`：获得对象本身属性
  - 月份从0开始
  - 星期从周日开始（为1）
- `set()`：void方法，直接修改对象本身属性
- `add()`：void方法，直接修改对象本身属性（减就是加负数）

```java
package com.ink.Date;

import java.util.Calendar;

public class CalendarTest {
    public static void main(String[] args) {
        Calendar instance = Calendar.getInstance();
        System.out.println(instance.getClass());
        int days = instance.get(Calendar.DAY_OF_YEAR);
        System.out.println(days);
        System.out.println(instance.get(Calendar.DAY_OF_YEAR));
        instance.set(Calendar.DAY_OF_YEAR,22);
        System.out.println(instance.get(Calendar.DAY_OF_YEAR));
        instance.add(Calendar.DAY_OF_YEAR,3);
        System.out.println(instance.get(Calendar.DAY_OF_YEAR));
    }
}
```

![Calendar对象操作](Java高级.assets/Calendar对象操作.png)



**Calendar和Date转换操作**

- `getTime()`：由`Calendar`类返回`Date`对象
- `setTime()`：由`Date`类返回`Calendar`子类对象

```java
package com.ink.Date;

import java.util.Calendar;
import java.util.Date;

public class CalendarTest {
    public static void main(String[] args) {
        Calendar instance = Calendar.getInstance();
        Date time = instance.getTime();
        System.out.println(time);
        Date date = new Date();
        instance.setTime(date);
        int days = instance.get(Calendar.DAY_OF_YEAR);
        System.out.println(days);
    }
}
```

![Calendar和Date](Java高级.assets/Calendar和Date.png)



## java.time

`Calendar`类和`Date`类缺点：

- **可变性**：日期应该是不可变的
- **偏移性**：`Date`的年份从1900年开始，月份从0开始（正常表示需要**减去偏移量**）
- **格式化**：格式化只对`Date`有用（`SimpleDateFormat`），对`Calendar`无用
- **线程不安全**
- **无法处理闰秒**

> 对日期和时间的操作一直比较复杂



 JDK8吸收了Joda-Time（jar包），创建了新的API——`java.time`

包含常用包：

- `java.time.format`
- `java.time.temporal`
- `java.time.zone`
- `java.time.chrono`

包含常用类：

- `LocalDate`
- `LocalTime`
- `LocalDateTime`
- `ZonedDateTime`
- `Duration`

```java
package com.ink.Date;


import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class Time {
    public static void main(String[] args) {
        LocalDate now = LocalDate.now();
        LocalTime now1  = LocalTime.now();
        LocalDateTime now2 = LocalDateTime.now();
        System.out.println(now);
        System.out.println(now1);
        System.out.println(now2);
    }
}
```

![time](Java高级.assets/time.png)



## Instant类

时间线上的一个**瞬间时间点**，可能被用来记录程序中的事件事件戳（面向机器）

返回**当前时间**和1970年1月1日0时0分0秒之间的时间差（以**毫秒**为单位）

> 精度可以达到纳秒



## DateTimeFormatter类

`java.time.format.DateTimeFormatter`类，提供三种格式化方法

- **预定义的标准格式**

  > ISO_LOCAL_DATE，ISO_LOCAL_TIME等

- **本地化相关格式**

- **自定义格式**

  `ofPattern()`方法



# 比较器

比较**对象**，实际是比较**对象的属性**

**对象排序**的两种方式（**接口**）

- 自然排序：`java.lang.Comparable`
- 定制排序：`java.util.Comparator`

**对比**：

`Comparable`方式是让对象所属的类去实现接口（作为实现类），对象在任何位置都可以比较大小

`Comparator`方式是临时创建实现类去比较，



## Comparable接口

`java.lang.Comparable`

**`String`，包装类排序**

已经实现了`Comparable`接口，重写了`compareTo(obj)`方法（从小到大排序）

![String比较](Java高级.assets/String比较.png)

![compareTo](Java高级.assets/compareTo.png)

重写`compareTo(obj)`方法规则：

- 当前对象this大于形参obj，返回正整数
- 当前对象this小于形参obj，返回负整数
- 当前对象this等于形参obj，返回0



**自定义类排序**

让它实现`Comparable`接口，重写了`compareTo(obj)`方法，指明排序规则

```java
package com.ink.Compare;

public class Goods implements Comparable{
    private String name;
    private double price;

    public Goods() {
    }

    public Goods(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "name='" + name + '\'' +
                ", price=" + price + '\n';
    }

    // 按照商品价格从低到高排序
    @Override
    public int compareTo(Object o) {
        if(o instanceof Goods){
            Goods goods = (Goods) o;
            if(this.price > goods.price){
                return 1;
            }else if(this.price < goods.price){
                return -1;
            }else{
                // name是String,已经重写了compareTo()方法
                return this.name.compareTo(goods.name);
            }
        }
        // return Double.compare(this.price,goods.price)
        throw new RuntimeException("传入的数据类型不一致");
    }
}
```

```java
package com.ink.Compare;

import java.util.Arrays;

public class Compare {
    public static void main(String[] args) {
        Goods[] arr = new Goods[6];
        arr[0] = new Goods("12",62);
        arr[1] = new Goods("232",24);
        arr[2] = new Goods("1100",24);
        arr[3] = new Goods("230923",37);
        arr[4] = new Goods("12983138930",37);
        arr[5] = new Goods("92",37);
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

![自定义排序结果](Java高级.assets/自定义排序.png)

如果想要利用`String`重写的`compareTo()`方法，但是要从高到低排序

```java
return -this.name.compareTo(goods.name);
```



## Comparator接口

`java.util.Comparator`

- 元素的类型没有实现`java.lang.Comparable`接口且不方便修改代码
- 元素的类型实现了`java.lang.Comparable`接口的排序规则，但是不适合当前操作

可以使用`Comparator`的对象来排序，重写接口中的`compare()`抽象方法

![Comparator](Java高级.assets/Comparator.png)

> `<T>`：泛型



重写`compare(Object o1,Object o2)`方法规则

- o1大于o2，返回正整数
- o1小于o2，返回负整数
- o1等于o2，返回0

![sort](Java高级.assets/sort.png)

使用**匿名内部类**直接在`Arrays.sort()`中重写

> 看上去`new`一个接口，实际上是匿名实现类

```java
package com.ink.Compare;

import java.util.Arrays;
import java.util.Comparator;

public class Compare {
    public static void main(String[] args) {
        String[] arr = new String[]{"A","B","C","D","E"};
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return -o1.compareTo(o2);
            }
        });
        // 输出E,D,C,B,A
        System.out.println(Arrays.toString(arr));
    }
}
```



# 枚举类

类的对象只有**有限个，确定的**（星期，性别，季节）。当需要定义**一组常量**时，建议使用枚举类

如果枚举类中**只有一个对象**，可以作为**单例模式**的实现方式

> 单例模式



## 自定义枚举类

> JDK5.0之前

1. 类的对象的属性都设置为`private final`，final常量需要赋值
   - 显式赋值
   - **构造器赋值**
   - 代码块赋值
2. 私有化类的构造器（否则被外部调用无法确定对象个数）
3. 提供当前枚举类的对象，声明为`public static final`
4. 获取枚举类对象的属性（`get()`方法）
5. 重写`toString()`方法

```java
package com.ink.Enumm;

import javax.swing.*;

public class SeasonTest {
    public static void main(String[] args) {
        Season spring = Season.SPRING;
        // 输出: Season{seasonName='春天', seasonDesc='1'}
        System.out.println(spring);
    }
}
// 自定义枚举类
class Season{
    private final String seasonName;
    private final String seasonDesc;
    private Season(String seasonName,String seasonDesc){
        this.seasonName = seasonName;
        this.seasonDesc = seasonDesc;
    }
    public static final Season SPRING = new Season("春天","1");
    public static final Season SUMMER = new Season("夏天","2");
    public static final Season AUTUMN = new Season("秋天","3");
    public static final Season WINTER = new Season("冬天","4");

    public String getSeasonName() {
        return seasonName;
    }

    public String getSeasonDesc() {
        return seasonDesc;
    }

    @Override
    public String toString() {
        return "Season{" +
                "seasonName='" + seasonName + '\'' +
                ", seasonDesc='" + seasonDesc + '\'' +
                '}';
    }
}
```



## enum关键字

> JDK5.0引入

使用`enum`关键字（不再是`class`）**定义枚举类**（不再需要复杂的声明）

定义的枚举类默认继承`java.lang.Enum`类，默认使用`Enum`类中的`toString()`方法



1. 先写枚举类对象，多个对象用**逗号**隔开，最后一个用分号
2. 私有化类的构造器（否则被外部调用无法确定对象个数）
3. 获取枚举类对象的属性（`get()`方法）

```java
package com.ink.Enumm;

public class EnumTest {
    public static void main(String[] args) {
        Season summer = Season.SUMMER;
        System.out.println(summer);
        System.out.println(Season.class.getSuperclass());
    }
}

enum Season{
    SPRING("春天","1"),
    SUMMER("夏天","2"),
    AUTUMN("秋天","3"),
    WINTER("冬天","4");

    private final String seasonName;
    private final String seasonDesc;

    private Season(String seasonName,String seasonDesc){
        this.seasonName = seasonName;
        this.seasonDesc = seasonDesc;
    }

    public String getSeasonName() {
        return seasonName;
    }

    public String getSeasonDesc() {
        return seasonDesc;
    }
}
```

![enum](Java高级.assets/enum.png)



**enum枚举类实现接口**

**每一个枚举类对象都可以实现接口**

```java
package com.ink.Enumm;

public class EnumTest {
    public static void main(String[] args) {
        Season spring = Season.SPRING;
        spring.show();
        Season summer = Season.SUMMER;
        summer.show();
    }
}
interface Info{
    void show();
}
enum Season implements Info{

    SPRING("春天","1"){
        @Override
        public void show() {
            System.out.println("这是春天");
        }
    },
    SUMMER("夏天","2"){
        @Override
        public void show() {
            System.out.println("这是夏天");
        }
    },
    AUTUMN("秋天","3"){
        @Override
        public void show() {
            System.out.println("这是秋天");
        }
    },
    WINTER("冬天","4"){
        @Override
        public void show() {
            System.out.println("这是冬天");
        }
    };

    private final String seasonName;
    private final String seasonDesc;

    private Season(String seasonName,String seasonDesc){
        this.seasonName = seasonName;
        this.seasonDesc = seasonDesc;
    }

    public String getSeasonName() {
        return seasonName;
    }

    public String getSeasonDesc() {
        return seasonDesc;
    }
}
```

![枚举类对象实现接口](Java高级.assets/枚举类对象实现接口.png)



## Enum类常用方法

- `values()`：返回枚举类型的**对象数组**

  ![values](Java高级.assets/values.png)

- `valueOf(String str)`：将字符串转换为对应的枚举类对象，**要求字符串必须是枚举类对象的"名字"**

  > 如果找不到枚举类对象，会抛异常

  ![valueOf](Java高级.assets/valueOf.png)

- `toString()`：返回当前枚举类对象**常量的名字**



# 注解

> JDK5.0开始 Java增加了对**元数据**（MetaData）的支持，也就是**注解**（Annotation）
>
> JavaSE的注解使用比较简单，而在JavaEE中注解很重要，比如用来配置应用程序的切面，XML配置等
>
> **框架 = 注解+反射+设计模式**

`Annotation`是代码中的特殊标记，这些标记可以在编译，加载，运行时**被读取并执行**相应处理。

`Annotation`可以像修饰符一样被修饰**包，类，构造器，方法，成员变量，参数，局部变量**。这些信息保存在`Annotation`的`"name = value"`对中

## 常用注解

**生成文档**

- `@author`：多个作者之间使用,分割
- `@version`：标明该类模块的版本
- `@see`：参考转向
- `@since`：从哪个版本开始增加的
- `@param`：对方法中某参数的说明，如果没有参数就不能写
- `@return`：对方法返回值的说明，如果方法的返回值类型是void就不能写
- `@exception`：对方法可能抛出的异常进行说明，如果方法没有用throws显式抛出的异常就不能写

> `@param`，`@return`和`@exception`这三个标记都是只用于方法的。



**在编译时进行格式检查**

> JDK内置的三个基本注解

`@Override`：表明重写父类或接口的方法, 该注解只能用于方法（编译时**校验**是否重写）

`@Deprecated`：表示所修饰的元素(类, 方法等)已过时（过时还是可以用的）

`@SuppressWarnings`：抑制编译器**警告**（含有成员）



**跟踪代码依赖性，实现替代配置文件功能**

Servlet3.0提供了注解(annotation)，使得不再需要在web.xml文件中进行Servlet的部署



**spring框架中关于事务的管理**



## 自定义注解

`@interface`

- 使用`@interface`关键字自定义Annotation类型（加上`@`）

- 自定义注解自动继承了`java.lang.annotation.Annotation`接口

- Annotation的**成员变量**以**无参数方法**的形式来声明，其方法名和返回值定义了该成员的名字和类型，称为**配置参数**
- 成员变量的类型只能是八种基本数据类型、String类型、Class类型、enum类型、Annotation类型和以上所有类型的数组。
- 可以在定义成员变量时使用`default`关键字**指定初始值**
- 如果只有一个参数成员，建议使用参数名为`value`（`String value()`）
- 如果定义的注解含有配置参数，那么**使用时必须指定参数值**（除非它有默认值）。格式是`value=参数值`，如果只有一个参数成员，且名称为value，可以省略`value=`
- **没有成员变量**的Annotation称为**标记**（如`@Override`），**包含成员变量**的Annotation称为**元数据**Annotation

> 自定义注解必须配上注解的**信息处理流程**才有意义
>
> 自定义注解通常会指明两个元注解`@Retention`和`@Target`



**自定义注解**

`New`-`Java Class`选择Annotation

```java
package com.ink.annotationtest;

public @interface myannotation {
    // 默认值hello
    String value() default "hello";
}

```

**使用注解**

```java
package com.ink.annotationtest;

public class annotationtest {
    public static void main(String[] args) {

    }
}
// 自定义注解使用
@myannotation(value = "hi")
class test{
    private String name;
    private int age;
	@myannotation
    public test(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```



## 元注解

`meta-annotation`

JDK 的元注解用于修饰其他注解

JDK5.0提供了4个标准的元注解类型

- `@Retention`
- `@Target`
- `@Documented`
- `@Inherited`

![元注解](Java高级.assets/元注解.png)

> 元数据
>
> `String name = "ink";`，`String` 和`name` 用来修饰`ink`



**@Retention**

用于修饰一个注解, 指定被修饰的注解的**生命周期**

`@Rentention`包含一个成员变量`RetentionPolicy`（枚举类），使用`@Rentention`时必须为该成员变量指定值

- `SOURCE`：在源文件中保留），编译器会丢弃这种注解，编译后的`.class`文件不会保留这个注解（反编译看不到）
- `CLASS`：在`.class`文件中保留，当运行Java 程序时, JVM会丢弃注解（**默认值**）
- `RUNTIME`：在运行时保留，当运行Java 程序时, JVM 会保留注解在内存中，程序可以通过**反射**读取该注解

**@Target**

用于修饰一个注解，指定被修饰的注解能**修饰哪些元素**

`@Target` 也包含一个成员变量`ElementType`（枚举类）

- `CONSTRUCTOR`：用于描述是否能修饰构造器
- `FIELD`：用于描述域
- `TYPE`：用于描述类，接口（包括注解类型），或enum声明
- `METHOD`：用于描述方法
- `PACKAGE`：用于描述包

**@Documented**

用于修饰一个注解，指定被修饰的注解将被javadoc工具**保留提取成文档**

被`@Documented`修饰的注解必须设置`@Retention`值为`RUNTIME`

> 默认情况下，javadoc是不包括注解的

**@Inherited**

用于修饰一个注解，指定被修饰的注解将具有继承性。如果某个类使用了被`@Inherited`修饰的注解，则其子类将自动具有该注解



## 可重复注解

> JDK8新特性

JDK8前：是声明一个**注解数组**

JDK8后：使用`@Repeatable`修饰重复使用的注解。`@Repeatable`中成员值为**注解数组**，保持两者的`@Retention`，`@Target`和`@Inherited`相同：



## 类型注解

> JDK8新特性

JDK8前：注解只能是在**声明**的地方所使用

JDK8后：注解可以应用在**任何地方**

在`@Target`中的`ElementType`表明可以修饰的元素

- `TYPE_PARAMETER`：表示该注解能写在**类型变量的声明语句**中（如：泛型声明）
- `TYPE_USE`：表示该注解能写在使用类型的**任何语句**中



# 集合

为了方便对多个对象的操作，就要使用**容器**对对象进行**存储**（**内存**层面）。集合可以**动态**地把多个**对象的引用**放入容器中

数组在存储方面的**弊端**

- 初始化以后长度不可变，不便于扩展
- 提供的属性和方法少，不便于进行增删改等操作，且效率不高（也可以用`Object`类的方法）
- 无法直接获取实际存储元素的个数
- 存储的数据是有序的、可重复的



**Java集合类**可以用于存储数量不等的多个对象，还可用于保存具有**映射关系**的关联数组

Java集合分为`Collection`和`Map`两种体系（接口）

- `Collection`接口：**单列集合**，存储一个个对象
  - `List`接口：元素**有序**、**可重复**的集合（动态数组）
    - `Vector`
    - `Arraylist`
    - `LinkedList`
  - `Set`接口：元素**无序**、**不可重复**的集合
    - `HashSet`
    - `LinkedHashSet`
    - `TreeSet`
- `Map`接口：**双列集合**，存储具有**映射**关系key-value对
  - `HashMap`
  - `LinkedHashMap`



## Collection接口

- `Collection`接口是`List`、`Set` 和`Queue`接口的**父接口**，该接口里定义的方法既可用于操作`Set`集合，也可用于操作`List`和`Queue`集合
- JDK不提供`Collection`接口的任何**直接实现**，而是提供更具体的子接口实现（`Set`和`List`）
- JDK5之前Java集合会丢失容器中对象的**数据类型**，把所有对象都当成Object类型处理
- JDK5增加了**泛型**以后Java集合可以记住容器中对象的数据类型

**Abstract Methods**

- 添加元素
  - `add(Objectobj)`
  - `addAll(Collectioncoll)`
- 获取有效元素的个数
  - `int size()`
- 清空集合
  - `void clear()`
- 判断集合是否为空
  - `boolean isEmpty()`
- 判断集合是否包含某个元素
  - `boolean contains(Objectobj)`：通过元素的`equals`方法来判断是否是同一个对象
  - `boolean containsAll(Collection c)`：调用元素的`equals`方法来比较两个集合的每一个元素
- 删除
  - `boolean remove(Object obj)` ：通过元素的`equals`方法判断是否是要删除的那个元素，只会删除匹配的第一个元素
  - `boolean removeAll(Collection coll)`：取当前集合的差集
- 取两个集合的交集
  - `boolean retainAll(Collection c)`：把交集的结果存在当前集合中，不影响c
- 判断集合是否相等
  - `boolean equals(Object obj)`
- 转成对象数组
  - `Object[] toArray()`
- 获取集合对象的哈希值
  - `hashCode()`
- 遍历
  - `iterator()`：返回迭代器对象，用于集合遍历



## Map接口

`ArrayList`**是一个采用类型参数的泛型类**

`<>`指定数组列表保存的元素**对象类型**·

