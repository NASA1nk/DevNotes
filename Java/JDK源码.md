# 集合

## ArrayList

底层基于数组`Object[] elementData`实现

### JDK7

饿汉式

- **直接创建一个初始容量为10的数组**

> 搜索类快捷键：`ctrl+n`
>
> 搜索类中方法快捷键：`ctrl+F12`

````java
// 空参构造器：创建一个初始容量为10的Object数组
ArrayList list = new Arraylist();

// elementData[0] = new Integer(123)
list.add(123);

// 当添加导致容量不够时,默认扩容为原来容量的1.5倍,再将原数组数据复制到新数组中
````

 ![JDK7饿汉](JDK源码.assets/JDK7饿汉.png)

### JDK8

懒汉式

- **一开始创建一个长度为0的数组，当添加第一个元素时再创建一个始容量为10的数组**
- 延迟数组的创建时间，节省内存

```java
// 空参构造器：创建一个空的Object[] elementData
// 并没有创建一个长度为10的Object[] elementData
ArrayList list = new Arraylist();

// 创建一个长度为10的Object[] elementData
// elementData[0] = new Integer(123)
list.add(123);

// 当添加导致容量不够时,默认扩容为原来容量的1.5倍,再将原数组数据复制到新数组中
```

 ![JDK8初始化](JDK源码.assets/JDK8初始化.png)

 ![JDK8懒汉式](JDK源码.assets/JDK8懒汉式.png)

### 扩容

**目的**

- 提高容量以便至少满足最少`minCapacity`大小的容量

> `oldCapacity`为旧容量，`newCapacity`为新容量，`minCapaciyt`为这次扩容最小需要的容量，`MAX_ARRAY_SIZE`是`Integer.MAX_VALUE - 8`

**步骤**

1. 将新容量更新为旧容量的1.5倍（预计要扩容到的容量）
   1. 并不是扩容到`minCapacity + 1`，这是为了避免频繁扩容，所以预先申请1.5倍的容量，采用了空间换时间的思想
2. 检查新容量是否大于最小需要容量，如果小于最小需要容量，那么就把最小需要容量当作数组的新容量
3. 检查新容量是否大于`MAX_ARRAY_SIZE`
   1. 如果大于`MAX_ARRAY_SIZE`，就扩容到int的最大值`Integer.MAX_VALUE`

> 因为数组理论上的最大长度就是`Integer.MAX_VALUE`，`MAX_ARRAY_SIZE`是个别JVM设计上的问题，但并不是说一定因为个别JVM就一定不让扩容到最大长度

 ![JDK7扩容](JDK源码.assets/JDK7扩容.png)

```java
// 减8是因为有些JVM需要用数组中的8个字节空间去保存header words，如果分配超过MAX_ARRAY_SIZE，可能会OOM
private static final int MAX_ARRAY_SIZE = Integer.MAX_VALUE - 8;

private static int hugeCapacity(int minCapacity) {
    if (minCapacity < 0)
        throw new OutOfMemoryError();
    return (minCapacity > MAX_ARRAY_SIZE) ? Integer.MAX_VALUE : MAX_ARRAY_SIZE;
}
```

### 更新

1. 插入操作需要先检查**是否需要扩容**
2. 插入和删除操作的移位操作都是利用**复制数组**完成

`public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)`

```java
// 将index及其之后的所有元素都向后移一位
System.arraycopy(elementData, index, elementData, index + 1, size - index);

// 将index+1及之后的元素向前移动一位，覆盖被删除值
System.arraycopy(elementData, index+1, elementData, index, numMoved);
```

## LinkedList

底层使用**双向链表**存储

- 存储元素过程中无需像`ArrayList`那样进行扩容

```java
// 内部声明了Node（双向链表）类型的first和last属性，默认为NULL
LinkedList list = new LinkedList();

// 将123封装到Node中（相当于创建了Node对象）
list.add(123);
```

 ![LinkedList底层存储](JDK源码.assets/LinkedList底层存储.png)

 ![Node内部类](JDK源码.assets/Node内部类.png)

### 插入

**在链表尾部插入元素**

1. 创建节点，并指定节点前驱为链表尾节点`last`，后继引用为`null`
2. 将`last`引用指向新节点
3. 判断尾节点是否为空
   1. 尾节点为空表示当前链表还没有节点
4. 让原尾节点后继引用`next`指向新的尾节点`newNode`

 ![LinkedListadd](JDK源码.assets/LinkedListadd.png)

 ![LinkedListlinklast](JDK源码.assets/LinkedListlinklast.png)



**在指定位置插入元素**

1. 判断index是否是链表尾部位置，如果是，直接将元素节点插入链表尾部即可
2. 如果不是，调用`linkBefore(E e, Node<E> succ)`将元素节点插入到`succ`之前的位置
   1. 初始化节点`newNode`，并指明前驱`pred`和后继`succ`
      1. `pred`是`succ`之前的前驱
   2. 将`succ`的前驱引用`prev`指向新节点`newNode`
   3. 判断尾节点是否为空
      1. 尾节点为空表示当前链表还没有节点
   4. 将`pred`的后继引用指向新节点`newNode`

> 就是链表插入操作

 ![LinkedList指定插入](JDK源码.assets/LinkedList指定插入.png)

![linkBefore](JDK源码.assets/linkBefore.png)



## HashMap

HashMap继承了`AbstractMap`，实现了`Map`、`Cloneable`和`Serializable`接口

- `public class HashMap<K,V> extends AbstractMap<K,V> implements Map<K,V>, Cloneable, Serializable` 

> HashMap继承`AbstractMap`的作用是：`AbstractMap`提供Map接口的骨干实现，以最大限度地减少实现此接口所需的工作
>
> Hashtable继承的是`Dictionary`抽象类，实现了`Map`、`Cloneable`和`Serializable`接口
>
> Hashtable直接使用`key`的hashcode值，HashMap的key的hashcode值是另外计算的，HashMap独立了hash算法，并且算法是通过key，value多次算出来的，减少了重复性



### JDK7

底层结构：**数组+链表**

1. 底层数组是`Entry[]`
   1. `Entry`是HashMap中的一个**内部类**
   2. 实例化对象后，底层创建了**长度为16**的一维数组`Entry[]`
   
2. 使用链表解决哈希冲突

> 当hash冲突严重时，在桶上形成的链表会变的越来越长，这样在查询时的效率就会越来越低（时间复杂度为 `o(n)`）

### JDK8

底层结构：**数组+链表+红黑树**

1. 底层数组是`Node[]`（`Node<K,V>[] table`）
   1. 实例化对象后，底层**并不直接创建**了长度为16的一维数组
   2. 调用`put()`方法后，底层才创建**长度为16**的一维数组`Node[]`

#### 红黑树

当满足两个条件时，执行**链表转红黑树**操作（树化）

1. 数组的某个位置上以链表形式存在的**数据个数 > 8**（默认阈值为 8）
2. 当前**数组长度 > 64**

> 此位置上所有的**数据改为使用红黑树存储**，以此来加快搜索速度
>
> 如果不满足条件，则对数据扩容

#### 存储过程

调用`key`所在类的`hascode()`方法计算`key`的hashcode值，通过**散列函数**找到`key`在`Entry`数组中的存放位置

- 如果此位置没有数据，直接添加`key:value`
- 如果此位置有数据，逐一比较`key`和已经存在的数据的hashcode值
  - 如果`key`和已经存在数据的hashcode值都不同，则**以链表的方式**添加`key:value`
  - 如果`key`和已经存在的某个数据的hashcode值相同，则再调用`equals()`方法比较
    - 如果返回`false`，则**以链表的方式**添加`key:value`
    - 如果返回`true`，则执行覆盖操作
      - 将要添加的`value`**替换已经存在的相同数据**的`value`值

**索引计算**

`tab[i = (n - 1) & hash]`

当HashMap长度为$2^n$时，模运算`%`可以变换为按位与`&`运算：`X % length = X & (length - 1)`

- 位运算`&`是要比模运算`%`效率高出很多
- 所以要求HashMap的容量必须为$2^n$

 ![put方法中的hash](JDK源码.assets/put方法中的hash.png)



#### 常量

- `DEFAULT_INITIAL_CAPACITY`：HashMap的默认容量（16）
- `MAXIMUM_CAPACITY`：HashMap支持的最大容量（2<sup>30</sup>）
- `DEFAULT_LOAD_FACTOR`：HashMap的默认负载因子（0.75）
- `TREEIFY_THRESHOLD`：Bucket中存储的`Node`个数大于该默认值时转化为红黑树（8）
- `UNTREEIFY_THRESHOLD`：Bucket中红黑树存储的`Node`个数小于该默认值时转化为链表（6）
- `MIN_TREEIFY_CAPACITY`：Bucket中的`Node`被树化时最小的hash表容量（64）
- `entrySet`：HashMap存储具体元素的集合
- `size`：HashMap存储的键值对的数量
- `modCount`：HashMap扩容和结构改变的次数
- `loadFactor`：填充因子，默认为`DEFAULT_LOAD_FACTOR`
- `threshold`：HashMap扩容的临界值（**容量*负载因子**：16*0.75 = 12）

> 根据统计学的结果，hash冲突是符合泊松分布的，而冲突概率最小的是在7-8之间，都小于百万分之一了，所以`HashMap.loadFactor`选取只要在7-8之间的任意值即可

##### Bucket

`Node`数组中可以**存放元素的位置**称之为桶（Bucket）

- 每个Bucket都有一个对应的索引
  - 可以根据索引快速的查找到Bucket中存储的元素

- 每个Bucket中存储一个`Node`对象，每一个`Node`对象可以带一个引用变量（用于指向下一个元素）
  - 所以在一个Bucket中可能是一个`Node`链


- 当Bucket中存储的`Node`个数大到需要转化红黑树存储时，如果HashMap的容量小于`MIN_TREEIFY_CAPACITY`，执行`resize()`扩容而不转化为红黑树

> `MIN_TREEIFY_CAPACITY`的值至少是`TREEIFY_THRESHOLD`的4倍

##### 负载因子

`threshold`

- 按照其他语言的参考及研究经验，会考虑将负载因子设置为0.7~0.75，此时**平均检索长度接近于常数**

负载因子的大小决定了HashMap的**数据密度**

- 负载因子越大，密度越大，**发生碰撞的几率越高**，数组中的链表越容易长，造成查询或插入时的比较次数增多，性能会下降

- 负载因子越小，**越容易触发扩容**，数据密度也越小，意味着发生碰撞的几率越小，数组中的链表也就越短，查询和插入时比较的次数也越小，性能会更高
  - 但是会浪费一定的内存空间。而且**经常扩容也会影响性能**，建议初始化预设大一点的空间

> 当超出`threshold`值时，如果要存放的位置非空，则默认扩容为原来容量的2倍
>

 ![HashMap重要常量](JDK源码.assets/HashMap重要常量.png)



#### 构造函数

- `tableSizeFor`函数：将输入的任意值转化为大于等于此值的$2^n$

- HashMap没有在构造函数中进行数组空间的分配，而是在第一次使用`put`函数存储数据时分配空间

![HashMap构造函数](JDK源码.assets/HashMap构造函数.png) 



#### 查找

1. 根据键（key）定位所在的桶（Bucket）的位置
   1. `(first = tab[(n - 1) & hash]) != null`
2. 再对链表或红黑树进行查找
   1. 如果`first`是`TreeNode`，调用红黑树的查找方法
      1. `first instanceof TreeNode`
   2. 否则对链表查找

![HashMapget](JDK源码.assets/HashMapget.png)



#### 插入

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
               boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    // 把当前的底层Node数组table赋给tab，判断HashMap的Node数组table是否为空
    if ((tab = table) == null || (n = tab.length) == 0)
        // 如果是首次put，使用resize()创建一个Node<K,V>数组
        n = (tab = resize()).length;
    // 根据key的hashcode值找到要存储的位置，查看是否有数据
    if ((p = tab[i = (n - 1) & hash]) == null)
        // 如果没有数据直接插入一个数据节点
        tab[i] = newNode(hash, key, value, null);
    else {
        // 如果有数据，链表数据的头节点已经被赋给p
        Node<K,V> e; K k;
        // 先判断插入key的hashcode值和头节点p的hashcode值是否一样
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            // hashcode值相等且equals()返回true，则直接覆盖
            e = p;
        // 判断当前Node是否为红黑树的TreeNode
        else if (p instanceof TreeNode)
            // 存入红黑树中
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        // 判断当前Node是否为单向链表的Node
        else {
            // 如果和头节点的hashcode值不相等，再依次和所有节点数据比较
            for (int binCount = 0; ; ++binCount) {
                // 链表只有一个节点
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    // 判断当前链表的大小是否大于预设的阈值，大于就要转换为红黑树
                    if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                        treeifyBin(tab, hash);
                    break;
                }
                // 比较链表其余节点，上面判断已经赋给了e = p.next
                // 找到key相同时直接退出遍历
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    break;
                p = e;
            }
        }
        // e不为空说明key存在，替换value即可
        if (e != null) { 
            // existing mapping for key
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    ++modCount;
    // 检查是否需要扩容
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}
```

#### 扩容

在HashMap中

- `Node<K,V>[] table`的长度都是$2^n$
- 阈值`threshold` =  HashMap容量`capacity` * 负载因子`loadFactor`
- 当HashMap中的键值对数量`size`超过阈值时，进行扩容

HashMap的扩容机制与其他变长集合的机制不太一样HashMap按当前`capacity`的2倍进行扩容，阈值`threshold`也变为原来的2倍

- 如果计算过程中，阈值溢出归零，则按阈值公式重新计算

- 扩容之后，要重新计算键值对的位置，并把它们移动到合适的位置上去

`resize()`

- 原`table`为`null`
  - 开辟默认大小`DEFAULT_INITIAL_CAPACITY = 16`的空间
  - 设置默认阈值`threshold`：16*0.75 = 12
- 原`table`不为null
  - 如果原本长度`oldCap`已经等于HashMap支持的最大容量`MAXIMUM_CAPACITY`，则直接返回
  - 否则开辟原来空间的2倍空间：`newCap = oldCap << 1`，阈值也设置为2倍
    -  可能会大于HashMap支持的最大容量`MAXIMUM_CAPACITY`

> 分配空间之后将原数组中的元素拷贝到新数组中，然后将table的引用指向新数组，原数组则等待GC进行处理

```java
final Node<K,V>[] resize() {
    Node<K,V>[] oldTab = table;
    // 首次进入oldCap，oldThr均为0
    int oldCap = (oldTab == null) ? 0 : oldTab.length;
    int oldThr = threshold;
    int newCap, newThr = 0;
    // table数组是有长度的，则进行扩容处理
    if (oldCap > 0) {
        if (oldCap >= MAXIMUM_CAPACITY) {
            threshold = Integer.MAX_VALUE;
            return oldTab;
        }
        else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
                 oldCap >= DEFAULT_INITIAL_CAPACITY)
            newThr = oldThr << 1; // double threshold
    }
    else if (oldThr > 0) // initial capacity was placed in threshold
        // 初始化时指定了threshold
        newCap = oldThr;
    else {               
        // zero initial threshold signifies using defaults
        // 使用默认threshold，首次进入执行，newCap = 16
        newCap = DEFAULT_INITIAL_CAPACITY;
        // newThr = 16*0.75 = 12
        newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
    }
    if (newThr == 0) {
        float ft = (float)newCap * loadFactor;
        newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
                  (int)ft : Integer.MAX_VALUE);
    }
    // threshold = 12
    threshold = newThr;
    @SuppressWarnings({"rawtypes","unchecked"})
    // newCap = 16,创建好了长度为16的数组
    Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
    table = newTab;
    // 拷贝
    if (oldTab != null) {
        for (int j = 0; j < oldCap; ++j) {
            Node<K,V> e;
            if ((e = oldTab[j]) != null) {
                oldTab[j] = null;
                if (e.next == null)
                    newTab[e.hash & (newCap - 1)] = e;
                else if (e instanceof TreeNode)
                    ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
                else { // preserve order
                    Node<K,V> loHead = null, loTail = null;
                    Node<K,V> hiHead = null, hiTail = null;
                    Node<K,V> next;
                    do {
                        next = e.next;
                        if ((e.hash & oldCap) == 0) {
                            if (loTail == null)
                                loHead = e;
                            else
                                loTail.next = e;
                            loTail = e;
                        }
                        else {
                            if (hiTail == null)
                                hiHead = e;
                            else
                                hiTail.next = e;
                            hiTail = e;
                        }
                    } while ((e = next) != null);
                    if (loTail != null) {
                        loTail.next = null;
                        newTab[j] = loHead;
                    }
                    if (hiTail != null) {
                        hiTail.next = null;
                        newTab[j + oldCap] = hiHead;
                    }
                }
            }
        }
    }
    return newTab;
}
```

#### 创建

使用已存在的Map对象`map1`来构建一个新的Map对象`map2`时会进行的操作

`Map<Integer,Integer> map2 = new HashMap<Integer,Integer>(map1);`

1. 首先对table进行检查
   1. 如果table为`null`，则算出`threshold`，为第一次调用`putVal`方法时为table分配空间
   2. 如果table不为`null`，检查是否需要扩容
2. 最后将需要添加的数据集合使用`putVal`方法的加入到数组table中

```java
public HashMap(Map<? extends K, ? extends V> m) {
    this.loadFactor = DEFAULT_LOAD_FACTOR;
    putMapEntries(m, false);
}

final void putMapEntries(Map<? extends K, ? extends V> m, boolean evict) {
    int s = m.size();
    if (s > 0) {
        if (table == null) { // pre-size
            float ft = ((float)s / loadFactor) + 1.0F;
            int t = ((ft < (float)MAXIMUM_CAPACITY) ?
                     (int)ft : MAXIMUM_CAPACITY);
            if (t > threshold)
                threshold = tableSizeFor(t);
        }
        else if (s > threshold)
            // 如果table不为空，且添加的map的长度大于阈值，则进行扩容
            resize();
        for (Map.Entry<? extends K, ? extends V> e : m.entrySet()) {
            K key = e.getKey();
            V value = e.getValue();
            putVal(hash(key), key, value, false, evict);
        }
    }
}
```



## ConcurrentHashMap

JDK1.5中引入了`concurrent`包，`ConcurrentHashMap`是线程安全的

- `ConCurrentHashMap`不允许存储`null`值的`key`或者`value`

### Segment

`ConcurrentHashMap`引入了**分段锁**的概念

- 把一个大的`HashMap`拆分成n个小的`Segment`，根据`key.hashCode()`来决定把`key`放到哪个`Segment`中
  - 部分锁，只锁对应的`Segment`
- 默认把`segments`初始化为长度为16的数组
- JDK1.8之后`ConcurrentHashMap`启用了一种全新的方式实现（CAS算法）

### JDK7

底层结构：**数组+链表**

- `Segment`是ConcurrentHashMap的一个内部类
  - 和HashMap中的`Entry`作用一样，是存放数据的桶Bucket

```java
final Segment<K,V>[] segments;
transient Set<K> keySet;
transient Set<Map.Entry<K,V>> entrySet;
```

`Segment`

- `value`，链表都是`volatile`关键词修饰的，保证了获取时的可见性
  - 虽然`value`是用`volatile`关键词修饰的，但是并不能保证并发的原子性，所以`put`操作时仍然需要加锁
- ConcurrentHashMap支持`Segment`数组数量的线程并发
  - 每当一个线程占用锁访问一个`Segment`时，不会影响到其他的`Segment`

```java
static final class Segment<K,V> extends ReentrantLock implements Serializable {
    
private static final long serialVersionUID = 2249069246763182397L;

transient volatile HashEntry<K,V>[] table;

transient int count;

transient int modCount;

transient int threshold;

final float loadFactor;
}
```

#### 插入

1. 通过key定位到`Segment`
2. 在对应的`Segment`中进行具体的`put`
   1. 尝试获取锁，如果获取失败说明有其他线程存在竞争，利用 `scanAndLockForPut()` **自旋获取锁**
   2. 如果重试的次数达到了`MAX_SCAN_RETRIES` 则改为**阻塞锁获取**，保证能获取成功
   3. 最后会解除在1中所获取当前`Segment`的锁

### JDK8

> JDK7的查询遍历链表效率太低

抛弃了原有的`Segment`分段锁

- 改用`CAS + synchronized`来保证并发安全性
- 引入红黑树

#### 插入

1. 根据`key`计算hash值
2. 判断是否需要进行初始化
3. 根据hash值定位`Node`，如果为空表示当前位置可以写入数据
   1. 利用CAS尝试写入，**失败则自旋保证成功**
4. 判断是否需要进行扩容
5. 如果都不满足，利用`synchronized`锁写入数据
6. 如果元素数量大于 `TREEIFY_THRESHOLD` 则要转换为红黑树



#### CAS

`Compare And Swap`

- 属于原子操作的一种，能够保证**一次读写操作是原子的**
- CAS 通过**将内存中的值与期望值进行比较**，只有在两者相等时才会对内存中的值进行修改

> CAS是支撑JUC的基础，能够在保证性能的同时提供并发场景下的线程安全性

CAS机制虽然无需加锁、安全且高效，但也存在一些缺点

- 循环检查的时间可能较长
  - 但可以限制循环检查的次数
- 只能对一个共享变量执行原子操作
- 存在ABA问题

> ABA问题：指在CAS两次检查操作期间，目标变量的值由A变为B，又变回A，但是CAS看不到这中间的变换，对它来说目标变量的值并没有发生变化，一直是A，所以CAS操作会继续更新目标变量的值
>
> 大部分时候该问题并不会对结果产生实质性影响

