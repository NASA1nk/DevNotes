# const

const 关键字可以限定一个变量的值不允许改变

> const不能定义真正意义上的常量，它只是告诉编译器，该变量不能出现在赋值符号的左边
>
> const修饰的变量是只读的，本质还是变量

> 在clang编译器上，用指针修改不会报错但是并不会修改其值，而在gcc上就会修改它的值
>
> c primer plus301页 c标准规定，使用非const标识符，修改const数据的结果是未定义的。所以才会有刚开始clang和gcc的区别

const int 类型的 i 的地址是不能赋值给指向 int 类型地址的指针 p 的（否则 p 能修改i的值）

```c
//不合法
const int i=10;
p = &i;
```

可以通过**强制类型转换**进行赋值

> const修饰的局部变量仍然是在栈上分配，可以通过指针修改其值。
>
> const将具有全局生命周期的变量存储在只读存储区（全局生命周期的变量除了全局变量还有static关键字修饰的变量），所以不能通过指针修改他们的值

```c
//合法，但不同的编译器结果不同
p= (int *) &i;
*p=20;
```

const的两种写法

- const int
- int const

```c
//均会报错，所以两种写法相等
const int i=10;
i++;
int const i=10;
i++;
```



# 指针

指针是一种**对象类型**，它引用函数或另一种类型的对象，可以添加**限定符**`const`。指针亦可以不引用任何内容，这通过一个特定的**空指针值**`NULL`指示。

成员访问运算符`*`：指针解引用

根据*和p的位置关系有不同的修饰

## const int* p

**p是指向（const int）的非const指针**

const修饰的是整个`*p`（即int），而不是p。所以这里的`*p`是不能被赋值的，也就是说不能通过`*p`来修改值。

指针变量p并没有用 const 关键字进行修饰，能被赋值**重新指向另一内存地址**（从而改变了值）

```c
const int * p = &n; 
*p = 2; // 错误：不能通过*p修改n的值
p = &m; // 正确： p自身可修改
```

## int* const p

**p 是一个指向（非 const 的 int） 的 const 指针**

p 因为有了 const 的修饰，所以只是一个指针常量，它只能永远指向初始化时的内存地址

```c
int * const p = &n; 
*p = 2; // 正确：通过p修改 n
p = &m; // 错误：p自身不能修改
```

## int * const * p = &n

指向 （ 指向（非 const 的 int）的 const 指针) 的 非 const 指针



# typedef

typedef为C语言的关键字，作用是为一种数据类型定义一个**别名**。这里的数据类型包括内部数据类型（int,char等）和自定义的数据类型（struct等）。

## 结构体

在C中，struct不能包含函数

```c
//正常的结构体
struct Node{

};
struct Node n1,n2;

//用typedef后声明变量的时候不需要在前面加struct
typedef struct Node{

}Node;
Node n1,n2;
```

## 结构体指针

```c
//Bitree不是结构体指针变量
//而是typedef给结构体指针的别名(Bitree~struct Treenode *)
typedef struct TreeNode{
	TNType  _value;
	struct TreeNode* _left;
	struct TreeNode* _right;
}TreeNode, * Bitree;
// 相当于定义了两次
typedef struct TreeNode{
	TNType  _value;
	struct TreeNode* _left;
	struct TreeNode* _right;
};
//typedef struct TreeNode TreeNode;
//typedef struct TreeNode* Bitree;
```



# ifndef

```c
#ifndef <标识> 	// if not define 
#define <标识> 	// then define 
#endif
```

当第一次包含标识时，由于没有定义标识，条件为真，这样就会包含（执行）#ifndef 标识和#endif之间的代码，当第二次包含标识时前面一次已经定义了标识，条件为假，#ifndef 和#endif之间的代码也就不会再次被包含，这样就避免了重定义。

## 标识

每个头文件的这个“标识”都应该是唯一的。

标识的命名规则一般是**头文件名全大写，前后加下划线，并把文件名中的“.”也变成下划线**。`stdio.h`就是`_STDIO_H_` 

# 读取输入

- gets：读入一行，并将**换行符**转换为字符串结束符
- scanf("%s",s)读入时，遇到**空白字符**（包括空格，制表符，换行符）时停止输入。

输入"test\nabcd"

- 执行gets后，**\n不会留在缓冲区中**，即这时调用getchar得到的字符是'a'
- 执行scanf后，**\n会留在缓冲区**，这时调用getchar得到的字符是'\n'