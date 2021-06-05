# ES6规范

**let**

- ES6前`var`，`if`和`for`中都没有块级作用域的概念，使用`var`声明的变量就是全局变量
- ES6后`let`拥有了块级作用域

> ES6之前所以很多时候需要使用function的作用域，比如闭包



**const**

- const定义的常量必须赋值
- 不能改变`const`常量指向的对象，但可以改变对象的属性

> 开发中优先使用`const`，只有需要改变一个标识符的时候才使用`let`

 

**对象字面值的增强写法**

- 属性的增强写法
- 函数的增强写法

```javascript
const name = "ink";
const age = 24;
// ES6以前
const user = {
  name: name,
  age: age
}
// ES6:属性的增强写法
const user = {
	name,
    age
}

// ES6以前
const obj = {
  run: function(){
     console.log("奔跑");
  }
}
// ES6:函数的增强写法
const obj = {
  run(){
     console.log("奔跑");
  },
  eat(){
      
  }
}
```



**箭头函数**



**字符串**

使用``包裹的字符串可以换行

# Vue.js

**渐进式**JavaScript框架：将Vue作为应用的一部分**嵌入其中**

> 尤雨溪
>
> Vue被设计为可以自底向上逐层应用
>
> `Soc`：Separation of concerns 关注点分离原则

**Vue生态**

- 网络通信：Axios
- 页面跳转：Vue-router
- 状态管理：Vuex
- Vue-UI：ICE，Element-UI

**虚拟DOM**

预先通过JavaScript进行各种计算，把最终的DOM计算出来并优化的技术。这个DOM操作属于**预处理操作**，没有真正的操作DOM。



## MVVM模式

**软件架构设计模式**

- Model：模型层（JavaScript对象）
- View：视图层（DOM）
- **ViewModel**：双向数据绑定（核心中间件）
  - DOM Listeners
  - Data Bindings



**MVVM架构不允许数据和视图直接通信，必须通过ViewModel来通信**

- **ViewModel能观察数据变化，对视图对应的内容进行更新**
- **ViewModel能监听视图变化，通知数据发生改变**



**Vue.js是ViewModel层的实现者**

**Vue特点**：

1. **低耦合（视图和数据）**

   View可以独立于model变化和修改。一个ViewModel可以绑定到不同的View上

   - 当View变化的时候Model可以不变
   - 当Model变化的时候View可以不变

2. **可复用组件**

   可以把视图逻辑放在一个ViewModel里面，让很多View复用这个视图逻辑

3. **前端路由技术**

4. **状态管理**

5. **虚拟DOM**

6. **可测试**



## 安装Vue.js

**CDN引入**

- 开发版本
- 生产版本

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```



**下载和引用**

导入后会暴露一个全局的变量`Vue()`

- [开发版本](https://cn.vuejs.org/js/vue.js)：包含完整的警告和调试模式
- [生产版本](https://cn.vuejs.org/js/vue.min.js)：删除了警告，33.30KB min+gzip

```html
<body>
  <script src="vue.js"></script>
</body>
```

打开控制台查看到以下信息即成功

![vue引入](Vue.js.assets/vue引入.png)



**NPM安装**

在用Vue构建大型应用时推荐使用NPM安装。

NPM能很好地和诸如webpack模块打包器配合使用。同时Vue也提供配套工具来开发单文件组件

```shell
npm install vue
```



## Vue源码

选择Tags下版本下载

版本：

- debug：开发
- release：发布

![Vue稳定版本](Vue.js.assets/Vue稳定版本.png)



## Idea开发

2. 安装Vue插件

3. 设置Vue文件模板

   file->setting->editor->file and code Templates，选择Vue Single File Component

   > 如果安装完vue插件后，右键new发现没有Vue component选项，需要自己新建模板
   >
   > https://blog.csdn.net/weixin_38556197/article/details/113838663
   
   ![Vue模板](Vue.js.assets/Vue模板.png)



## 代码规范

eslint

缩进：2个空格

> CLI：`.editorconfig`

![缩进](Vue.js.assets/缩进.png)





# Vue基础

**Vue有7个属性，8个方法，7个指令**（787原则）

**Vue属性**

- `el`：string或HTML Element，挂载Vue对象要管理的元素（指示Vue编译器解析）
- `data`：object或Function，Vue实例对应的数据对象（**组件中必须是函数Function**）
- `template`：模板，会替换页面元素（包括占位符）
- `methods`： {key: Function}，定义Vue的一些方法，可以在其他地方调用（包括指令）
- `render`：真正的Virtual Dom
- `computed`：计算属性
- `watch`：监听data中数据的变化



## Vue实例

每个Vue应用都是通过用`Vue({})`函数创建一个新的**Vue实例**开始，所有的Vue组件都是Vue实例

### 声明式编程

1. **导入Vue**
2. **new一个Vue对象**
3. **Vue对象绑定元素**
4. **存放数据**

> vue()函数传入的是一个对象{}
>
> 在文档中经常会使用 `vm` (ViewModel ) 这个变量名表示Vue实例
>
> 不再HTML直接交互，Vue应用会将其挂载到一个DOM元素上对其进行完全控制
>
> JavaScript是命令式编程
>
> 1. 创建div元素，设置id属性
> 2. 定义一个变量叫message
> 3. 将message变量放在div元素中显示
> 4. 修改message数据
> 5. 将修改的元素替换到div

```htmL
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
<!--view层 模板-->
<div id="app">
  {{message}}
</div>

<!--导入Vue.js-->
<script src="vue.js"></script>
<script>
  // var 没有作用域
  const vm = new Vue({
    // 元素element,json对象,逗号隔开
    el: "#app",
    // 对象:键值对
    // model层 数据
    data: {
      message:"Hello Vue!"
    }
  })
</script>
</body>
</html>
```



### 双向绑定

修改**Vue对象**就可以修改内容

> Vue不改变DOM

![hellovue](Vue.js.assets/hellovue.png)





## Vue模板

> 生成在user组下

```html
<div id="app">
  {{message}}
</div>

<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      message: 'hello vue'
    },
  });
</script>
```

![Vue模板](Vue.js.assets/Vue模板-1622732216210.png)

![HTML区域模板](Vue.js.assets/HTML区域模板.png)



## 插值操作

将**值**插到模板的**内容**中

### 文本

**Mustache语法**

数据绑定最常见的形式就是使用Mustache语法 (**双大括号**) 的文本插值

Mustache语法`{{}}`中也**可以是简单的表达式**

> 用于内容



**`v-once`指令**

 执行**一次性地插值**，当数据改变时**插值处的内容不会更新**

```html
<body>
<div id="app">
  <h2 v-once> {{message}}</h2>
</div>

<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      message: 'hello vue'
    },
  });
</script>
</body>
```

****

**`v-text`指令**

`v-text`会覆盖dom元素中的数据，相当于JavaScript的`innerText()`方法



**`v-pre`指令**

直接输出`{{message}}`这样的字符串，而不是被`{{}}`语法转化的message的变量值



### HTML

 **`v-html`指令**

`{{}}`将数据解释为**普通文本**而非HTML代码

```html
<body>
<div id="app">
  <h2>不使用v-html</h2>
  <h2>{{url}}</h2>
  <h2>使用v-html，直接插入html</h2>
  <h2 v-html="url"></h2>

</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: "#app",
    data: {
      message:"你好啊",
      url: "<a href='http://www.baidu.com'>百度一下</a>"
    }
  })
</script>
</body>
```



### v-cloak

有时候因为加载延时问题造成数据没有及时刷新，这时页面会显示从`{{message}}`到message变量的变化。使用`v-cloak`指令可以在没加载之前不显示数据

- 在vue解析之前，div属性中有`v-cloak`这个标签
- 在vue解析完成之后，v-cloak标签被移除

> 一开始有一个css属性`display:none`，加载完之后css属性变成`display:block`从而显示元素

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>v-cloak指令的使用</title>
  <style>
    [v-cloak]{
      display: none;
    }
  </style>
</head>

<body>
<div id="app" v-cloak>
  <h2>{{message}}</h2>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
<script>
  //在vue解析前，div中有一个属性cloak
  //在vue解析之后，div中没有一个属性v-cloak
  setTimeout(() => {
    const app = new Vue({
      el: "#app",
      data: {
        message: "你好啊"
      }
    })
  }, 1000);
</script>
</body>
</html>
```



### Attribute

Mustache语法不能作用在HTML标签的属性`attribute`上

在HTML标签中使用 `v-bind`（简写`:`）绑定HTML标签的属性

> `v-bind:标签属性="变量值"`
>
> 对于布尔`attribute` ，只要存在就意味着值为 `true`

```html
<body>
<div id="app">
  <!-- 将span标签的title属性和Vue实例的message的值绑定 -->
  <span v-bind:title="message">     
        鼠标悬停几秒钟查看此处动态绑定的提示信息！   
    </span>
  <!-- 缩写 -->
  <span :title="message">     
        鼠标悬停几秒钟查看此处动态绑定的提示信息！   
    </span>
</div>
<script src="vue.js"></script>
<script>
  const vm = new Vue({
    el: "#app",
    data: {
      message:"Hello Vue!"
    }
  })
</script>
</body>
```



**JavaScript表达式**



## 动态绑定

`v-bind`（简写 `:`）

- 动态绑定属性（**响应式**的更新HTML**标签中的属性**）。当表达式的值改变时，将其产生的连带影响**响应式**地作用于绑定的DOM元素

-  `v-bind` 用于绑定`class`和`style`时，Vue做了专门的增强。表达式结果的类型除了字符串之外，还可以是**对象或数组**




### 参数

指令能够接收一个**参数**（HTML标签属性），在指令后以**冒号**表示

> 参数：`src`，`v-bind` 指令将该元素的 `src` 属性与 Vue对象的`url` 值绑定

```html
<body>
<div id="app">
  <image v-bind:src="url"></image>
  <a :href="link">点击跳转</a>
  <a href=""></a>
</div>

<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      url: 'https://img2.baidu.com/it/u=3228549874,2173006364&fm=26&fmt=auto&gp=0.jpg',
      link: 'http://www.baidu.com'
    },
  });
</script>
</body>
```

### 修饰符

修饰符是以 `.` 指明的**特殊后缀**，用于指出一个指令应该以**特殊方式绑定**



### 绑定class

可以对Dom元素的`class`属性进行动态绑定（用来选择Dom是否有指定的`class`属性）

**对象语法**

- 传入`class`属性**对象**并使用**布尔值选择**来动态地切换`class`属性
  - `<h2 :class="{类名1: boolean,类名2: boolean}">`
- 当对象中属性很多时也可以使用**方法调用**
  - `<h1 :class="getClasses()">class属性绑定</h1>`
- 动态绑定的`class`属性可以与普通的`class`属性共存
- 可以绑定计算属性（返回对象）

```html
<!DOCTYPE html>
<html lang="en" xmlns:v-bind="">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
  <style>
    .active{
      color: red;
    }
  </style>
</head>
<body>
<div id="app">
  <image v-bind:src="url"></image>
  <a :href="link">点击跳转</a>
  <h1 v-bind:class="{active: isActive, line: isLine}">class属性绑定</h1>
  <h1 class="title" :class="getClasses()">class属性绑定</h1>

</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      url: 'https://img2.baidu.com/it/u=3228549874,2173006364&fm=26&fmt=auto&gp=0.jpg',
      link: 'http://www.baidu.com',
      isActive: true,
      isLine: true
    },
    methods: {
      getClasses(){
        return {active: this.isActive, line: this.isLine}
      }
    }
  });
</script>
</body>
</html>
```



**数组语法**

`class`属性可以是一个数组，会依次解析成对应的`class`，数组也可以由方法返回

-  加上单引号表示字符串（写死）
-  不加单引号的表示变量

```html
<body>
<div id="app">
  <!-- 加上单引号表示字符串 -->
  <h2 class="title" :class="['active','line']">{{message}}</h2>
  <!-- 不加表示变量 -->
  <h2 class="title" :class="[active,line]">{{message}}</h2>
  <!-- 方法返回数组 -->
  <h2 class="title" :class="getClasses()">{{message}}</h2>

</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data:{
      message: '你好啊',
      active: 'ink',
      line: 'yinke'
    },
    methods: {
      getClasses(){
        return [this.active,this.line]
      }
    },
  })
</script>
</body>
```

### 绑定style

绑定CSS内联样式：`<h2 :style="{key(属性名):value(属性值)}">`

- 对象语法
- 数组语法

> 组件化开发中可复用组件的使用，动态绑定样式属性
>
> 驼峰命名法
>
> 数字和字符串连接成字符串

```html
<body>
<div id="app">
  <!-- 加单引号表示字符串 -->
  <h2 :style="{fontSize: '50px'}">{{message}}</h2>
  <!-- 不加单引号表示变量 -->
  <h2 :style="{fontSize: fontSize}">{{message}}</h2>
  <!-- 连接 -->
  <h2 :style="{fontSize: fontSizenopx + 'px'}">{{message}}</h2>
  <!-- 方法 -->
  <h2 :style="getStyle1()">{{message}}</h2>
  
  <!-- 数组语法:对象数组 -->
  <h2 :style="[baseStyle1,baseStyle2]">{{message}}</h2>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el:"#app",
    data:{
      message: '你好啊',
      fontSize: '50px',
      fontSizenopx: 100,
      baseStyle1: {backgroundColor: 'red'},
      baseStyle2: {fontSize: '100px'}
    },
    methods: {
      getStyle1(){
        return {fontSize: this.fontSize}
      },
      getStyle2(){
        return [this.baseStyle]
      }
    },
  })
</script>
</body>
```



## 事件监听

`v-on` （简写 `@`）

可以监听DOM事件并绑定在事件触发时要运行的`methods`中的方法

> `v-on`指令可以绑定HTML所有的事件

```html
<body>
<div id="app">
  <!-- 通过方法响应点击事件 -->
  <button v-on:click="sayhi">点击</button>
  <!-- 简写 -->
  <button @click="sayhi">点击</button>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: "#app",
    data: {
      message: "hi ink"
    },
    // 方法也是K-V键值对
    methods: {
      // sayhi: function ()
      sayhi(){
        alert(this.message);
      }
    }
  })
</script>
</body>
```

![Vue事件](Vue.js.assets/Vue事件.png)



### 参数

- 事件调用的方法不需要传递参数，方法后的`()`可以不添加
- 事件调用的方法需要传递参数，但方法后没加`()`，默认将原生事件`event`对象当成参数传递
- 事件调用的方法需要传递参数，而且还需要`event`对象，可以通过`$event`获取`event`对象

```html
<body>
<div id="app">
  <!-- 不传参 -->
  <button @click="btnClick1">按钮1</button>
  <button @click="btnClick1()">按钮1</button>
  <!-- 事件调用方法需要传参，但省略了小括号 -->
  <button @click="btnClick2(123)">按钮3</button>
  <button @click="btnClick2()">按钮4</button>
  <button @click="btnClick2">按钮5</button>
  <!-- 事件调用方法需要传入event和其他参数 -->
  <button @click="btnClick3($event,123)">按钮6</button>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    methods: {
      btnClick1(){
        console.log("点击");
      },
      btnClick2(value){
        console.log(value);
      },
      btnClick3(event,value){
        console.log(event+" "+value);
      }
    }
  })
</script>
</body>
```

![事件监听方法参数](Vue.js.assets/事件监听方法参数.png)

### 修饰符

方法只有纯粹的数据逻辑，不会去处理DOM事件细节

> 事件冒泡

Vue为`v-on` 指令提供了**事件修饰符**（点开头的指令后缀表示）

- `.stop`：调用`event.stopPropagation()`，阻止事件冒泡
- `.prevent`：调用`event.preventDefault()`，阻止默认事件
- `.{keyCode}` ：只有当事件是**键盘特定键**触发时才触发回调
- `.enter`：监听键盘**回车键**敲击事件
- `.native`：监听**组件**根元素的原生事件
- `.once`：只触发一次回调
- `.capture`
- `.self`
- `.passive`

> 使用修饰符时，顺序很重要。相应的代码会以同样的顺序产生

```html
<!-- 阻止单击事件继续传播 -->
<a @click.stop="doThis"></a>

<!-- 提交事件不再重载页面 -->
<form @submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a @click.stop.prevent="doThat"></a>

<!-- 只有修饰符 -->
<form @submit.prevent></form>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->
<div @click.capture="doThis">...</div>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div @click.self="doThat">...</div>

<!-- 监听键盘的事件 -->
<input type="text" @keyup="keyup">

<!-- 监听键盘回车键的事件 -->
<input type="text" @keyup.enter="keyup">
```



## 条件渲染

根据表达式的值在DOM中**渲染或销毁**元素或组件

- `v-if`
  - 单独使用`v-if`，变量为布尔值
- `v-else-if`
- `v-else`

> ===：JavaScript中先判断**类型**是否一致，再比较值

```html
<body>
<div id="app">
  <h2 v-if="isFlag">isFlag为true显示这个</h2>
  <h2 v-show="isShow">isShow为true是显示这个</h2>
  <div v-if="age<18">小于18岁未成年</div>
  <div v-else-if="age<60">大于18岁小于60岁正值壮年</div>
  <div v-else="">大于60岁,暮年</div>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: "#app",
    data: {
      isFlag: true,
      isShow: false,
      age: 52
    }
  })
</script>
</body>
```

![判断结构](Vue.js.assets/判断结构.png)



**条件很多时建议使用计算属性** 

```html
<body>
<div id="app">
  <!-- 计算属性 -->  
  <div>{{show}}</div>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      age: 52
    },
    computed: {
      show(){
        let showm = ''
        if(this.age <18){
          showm = '小于18岁未成年'
        }
        else if(this.age <60){
          showm = '大于18岁小于60岁正值壮年'
        }
        else{
          showm = '大于60岁暮年'
        }
        return showm
      }
    }
  })
</script>
</body>
```



### 包裹渲染

`v-if` 是一个指令，只能将它添加到一个元素上

如果想切换多个元素，可以把一个 `template` 元素当做不可见的**包裹元素**，并在上面使用 `v-if`。最终的渲染结果将不包含 `template` 元素

```html
<template v-if="ok">
    <h1>Title</h1>  
    <p>Paragraph 1</p>  
    <p>Paragraph 2</p> 
</template>
```



### v-show

决定一个元素是否渲染

- 带有 `v-show` 的元素**始终会被渲染并保留在DOM中**
- `v-show` 只是切换元素的CSS属性（`display`）
- `v-show` 不支持 `template` 元素，也不支持 `v-else`

**区别**：

- `v-if` 是**真正的条件渲染**，它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建
- `v-if` 是**惰性的**：如果在初始渲染时条件为假，则什么也不做，直到条件第一次变为真时，才会开始渲染条件块
- `v-show`不管初始条件是什么，**元素总是会被渲染**，并且只是简单地基于CSS进行切
- `v-if` 有更高的切换开销，而 `v-show` 有更高的初始渲染开销。如果需要非常频繁地切换，使用 `v-show` 较好。如果在运行时条件很少改变，使用 `v-if` 较好

> `v-if`当条件为false时，不会有对应的元素在DOM中，`v-show`当条件为false时，将元素的display属性设置为none而已。
>
> 当 `v-if` 与 `v-for` 一起使用时，`v-for` 具有比 `v-if` 更高的优先级
>
> 不推荐一起使用



### 登录demo

```html
<body>
<div id="app">
    <span v-if="isUser">
      <!-- 点击获取聚焦   -->
      <label for="username">用户账号</label>
      <input type="text" id="username" placeholder="请输入用户名" >
    </span>
  <span v-else="isUser">
        <label for="email">用户邮箱</label>
        <input type="text" id="email" placeholder="请输入用户邮箱" >
    </span>
  <button @click="isUser=!isUser">切换类型</button>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      isUser: true
    }
  })
</script>
</body>
```

**渲染问题**

在已有输入内容的情况下，切换类型后不会清空已有内容

**原因**

Vue在进行DOM渲染时，出于性能考虑，会**尽可能的复用已经存在的元素**，而不是重新创建新的元素。所以Vue内部发现原来的`input`元素不再使用后，所以直接将其映射对应成虚拟DOM复用

**解决**

给对应的`input`添加`key`属性，并且需要保证`key`不同

```html
<input type="text" id="username" placeholder="请输入用户名" key="username">
<input type="text" id="email" placeholder="请输入用户邮箱" key="email">
```



## 列表渲染	

### 遍历数组

使用`v-for`指令和 `(item,index) in items` 语法，基于一个数组来渲染一个列表

-  `index`：数组元素**索引**
-  `item` ：被迭代的**数组元素**
-  `items` ：**源**数据数组

> 响应式：追加数据可以自动展示
>
> `(item,index)`：元组
>
> 可以用 `of` 替代 `in` 作为分隔符

```html
<body>
<div id="app">
    <li v-for="item in items">
        {{item.message}}
    </li>
</div>
<div id="app">
    <li v-for="(item,index) in items">
        {{index + "." + item.message}}
    </li>
</div>
<script src="vue.js"></script>
<script>
    const vm = new Vue({
        el: ''#app',
        data: {
            items: [
                {message: 'ink'},
                {message: 'yinke'}
            ]
        }
    })
</script>
</body>
```

`v-for` 可以访问到**父作用域**的属性

```html
<body>
<div id="app">
  <ul id="app">
    <li v-for="(item, index) in items">
      {{ parentMessage + "-" + index + "-" + item.message}}
    </li>
  </ul>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      parentMessage: 'Parent',
      items: [
        { message: 'Foo' },
        { message: 'Bar' }
      ]
    }
  });
</script>
</body>
```

![v-for获取父作用域属性](Vue.js.assets/v-for获取父作用域属性.png)

### 遍历对象

- 遍历对象时如果只取一个值`item in items`，默认获取的是`value`
- 使用`(value,key) in items`获取`value`和`key`
- 使用`(value,key,index) in items`获取`value`，`key`和`index`

> 遍历对象时会按 `Object.keys()` 的结果遍历

```html
<body>
<div id="app">
  <ul>
    <li v-for="(value,key) in user" >{{key+"-"+value}}</li>
  </ul>
  <ul>
    <li v-for="(value,key,index) in user" >{{key+"-"+value+"-"+index}}</li>
  </ul>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: "#app",
    data: {
      user: {
        name: "ink",
        height: 182,
        age: 24
      }
    }
  })
</script>
</body>
```

![遍历对象](Vue.js.assets/遍历对象.png)



### key属性

官方推荐在使用`v-for`时给对应的**元素或组件**添加上一个`key`属性

**key的作用主要是为了高效的更新虚拟DOM**

> 要保证key绑定的值和元素一一对应，不要使用`index`，一般就使用`item`
>
> 不加`key`渲染的时候会**依次替换**渲染，加了`key`后会直接将其放在指定位置

```html
<body>
<div id="app">
  <!-- 不加key如果要插入f依次改变 -->
  <ul>
    <li v-for="item in letters">{{item}}</li>
  </ul>
  <button @click="add1">没有key</button>
  <!-- 加key如果要插入f使用diff算法高效 -->
  <ul>
    <li v-for="item in letters" :key="item">{{item}}</li>
  </ul>
  <button @click="add2">有key</button>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      letters: ['a','b','c','d','e']
    },
    methods: {
      add1(){
        this.letters.splice(2,0,'f')
      },
      add2(){
        this.letters.splice(2,0,'f')
      }
    }
  })
</script>
</body>
```



### 状态维护

Vue 更新使用 `v-for` 渲染的元素列表时默认使用**就地更新**的策略。如果数据项的顺序被改变，**Vue 将不会移动DOM元素来匹配数据项的顺序，而是就地更新每个元素**，确保它们在每个索引位置正确渲染

> **只适用**于不依赖子组件状态或临时DOM状态 (例如表单输入值) 的列表渲染输出



### 数组更新

改变DOM绑定的数据时DOM会动态改变值（响应式）

对于动态变化数据，**不是所有的改变数据的方法都是响应式的**

- **通过索引值改变数组中元素是非响应式的（不会重新渲染）**
  - `this.letters[0]='f'`
- **响应式方法**
  - `push()`：在数组最后面添加一个元素（可以添加多个）
  - `pop()`：删除数组最后一个元素
  - `shift()`：删除数组第一个元素
  - `unshift()`：在数组最前面添加一个元素（可以添加多个）
  - `splice(start,number,item)`：删除元素/插入元素/替换元素
  - `sort()`：排序
  - `reverse()`：反转



### 遍历demo

1. 给每个`<li>`标签加上点击事件，并将遍历的`index`作为参数传入点击事件的回调函数`liClick()`中
2. 定义`curIndex`表示当前索引用于表示选中的电影，初始值为-1
3. 通过`index=curIndex`判断是否是当前选中的电影来改变`class`属性

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>综合练习</title>
  <style>
    .active {
      background-color: red;
    }
  </style>
</head>

<body>
<div id="app">
  <ul>
    <li v-for="(item,index) in movies"
        @click="liClick(index)"
        :class="{active:index===curIndex}">
      {{index+"---"+item}}
    </li>
  </ul>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: "#app",
    data: {
      movies: ['复仇者联盟', '蝙蝠侠', '海贼王', '星际穿越'],
      curIndex:-1
    },
    methods: {
      liClick(index){
        this.curIndex = index
      }
    }
  })
</script>
</body>
</html>
```



## 表单绑定

多用于用户信息的提交

### 双向绑定

- `v-model`指令可以实现**表单输入和应用状态**之间的**双向绑定**
- `v-model`会忽略所有表单元素的`value`，`checked`，`selected`的初始值而**将Vue实例数据作为数据来源**（所以要在组件的`data`中声明初始值）
- `v-model`在内部为**不同的输入元素使用不同的属性并抛出不同的事件**
  - `text/textarea`：使用 `value`属性和 `input` 事件
  - `checkbox/radio`：使用 `checked`属性和 `change` 事件
  - `select`：使用 `value`属性和`change` 作为事件

> `label`标签
>
> 在label元素内点击文本就会触发此控件，即选择该标签时浏览器就会自动将焦点转到和标签相关的表单控件上

#### text

```html
<body>
<div id="app">
  <!--绑定message和input表单内容-->
  输入文本<input type="text" v-model="message">
  <p>{{message}}</p>
  <button type="button" @click="submit">提交</button>
  <div></div>
  
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      message: 'ink',
    },
    methods: {
      submit: function (){
        alert(this.message)
      }
    }
  });
</script>
</body>
```

![表单双向绑定](Vue.js.assets/表单双向绑定.png)

#### radio

多个`radio`单选框如果绑定相同的属性就可以实现互斥，如果使用`v-model`**绑定相同的属性**，也可以实现互斥

```html
<body>
<div id="app">
  <!-- v-model绑定sex后，用于互斥的name属性可以省略 -->
  <label for="male">
    <input type="radio" id="male" name="sex" value="男" v-model="sex">男
  </label>
  <label for="female">
    <input type="radio" id="female" name="sex" value="女" v-model="sex">女
  </label>
  <h2>你选择的性别是：{{sex}}</h2>

</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      sex: '男'
    },
  })
</script>
</body>
```

![v-model绑定radio](Vue.js.assets/v-model绑定radio.png)

#### checkbox单选

```html
<body>
<div id="app">
  <!-- 单个复选框-->
  <input type="checkbox" id="checkbox" v-model="checked">
  <label for="checkbox">{{ checked }}</label>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      checked: ''
    }
  });
</script>
</body>
```

#### checkbox多选

```html
<body>
<div id="app">
  <!-- 多个复选框-->
  <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
  <label for="jack">Jack</label>
  <input type="checkbox" id="john" value="John" v-model="checkedNames">
  <label for="john">John</label>
  <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
  <label for="mike">Mike</label>
  <br>
  <span>Checked names: {{ checkedNames }}</span>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      checkedNames: []
    }
  });
</script>
</body>
```

![checkbox多复选框](Vue.js.assets/checkbox多复选框.png)

#### select

`select`也分单选和多选两种情况

> 按住ctrl多选

```html
<body>
<div id="app">
  <!-- select单选 -->
  <select name="fruit" v-model="fruit">
    <option value="苹果">苹果</option>
    <option value="香蕉">香蕉</option>
    <option value="西瓜">西瓜</option>
  </select>
  <h2>你选择的水果是：{{fruit}}</h2>
  
  <!-- select多选 -->
  <select name="fruits" v-model="fruits" multiple>
    <option value="苹果">苹果</option>
    <option value="香蕉">香蕉</option>
    <option value="西瓜">西瓜</option>
  </select>
  <h2>你选择的水果是：{{fruits}}</h2>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      fruit: "苹果",
      fruits: []
    },
  })
</script>
</body>
```



### v-model原理

`v-model` = `v-bind` + `v-on`

`v-model`本质上是一个语法糖，它负责**监听用户的输入事件**以**更新数据**，并对一些极端场景进行特殊处理

它本质上包含两个操作

- `v-bind`绑定`input`标签的`value`属性
- `v-on`绑定`input`标签的`input`事件（通过event获取当前`value`值）

![v-model原理](Vue.js.assets/v-model原理.png)



### 值绑定

动态的给`input`标签的`value`属性赋值



### 修饰符

`.lazy`

默认情况下`v-model` 在每次 `input` 事件触发后就会将输入框的值与数据进行同步（即只要数据变化就会同步）

使用 `lazy` 修饰符可以设置为在 `change` 事件**之后**进行同步（只有在回车或者失去焦点后才会同步）

```html
<input v-model.lazy="ink">
```

`.number`

默认情况下输入框中无论输入的是字母还是数字，**都会被当做字符串类型**进行处理

使用 `number` 修饰符可以自动将用户的输入值转为**数字类型**

```html
<input v-model.number="age" type="number">
```

`.trim`

使用`trim`修饰符可以自动**过滤输入的首尾空格**

```html
<input v-model.trim="ink">
```



## 综合demo

![综合练习](Vue.js.assets/综合练习.png)

```html
<!DOCTYPE html>
<html lang="en" xmlns:v-bind="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <title>综合练习</title>
  <style>
    table {
      border: 1px solid #e9e9e9;
      border-collapse: collapse;
      border-spacing: 0;
    }
    th, td {
      padding: 8px 16px;
      border: 1px solid #e9e9e9;
      text-align: left;
    }
    th {
      background-color: #f7f7f7;
      color: #5c6b77;
      font-weight: 600;
    }
  </style>
</head>
<body>
<div id="app">
  <div v-if="books.length">
    <table>
      <thead>
      <tr>
        <th></th>
        <th>书籍名称</th>
        <th>出版日期</th>
        <th>价格</th>
        <th>购买数量</th>
        <th>操作</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(item,index) in books">
        
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
        <td>{{item.date}}</td>
        <td>{{price(item.price)}}</td>
        <td>
          <button @click="reduce(index)" v-bind:disabled="item.count <= 1">-</button>
          {{item.count}}
          <button @click="increase(index)">+</button>
        </td>
        <td>
          <button @click="remove(index)">移除</button>
        </td>
      </tr>
      </tbody>
    </table>
    <h2>总价格: {{price(totleprice)}}</h2>
  </div>
  <h1 v-else>购物车为空</h1>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      books: [
        {
          id: 1,
          name: '《算法导论》',
          date: '2006-9',
          price: 85.00,
          count: 1
        },
        {
          id: 2,
          name: '《UNIX编程艺术》',
          date: '2006-2',
          price: 59.00,
          count: 1
        },
        {
          id: 3,
          name: '《编程珠玑》',
          date: '2008-10',
          price: 39.00,
          count: 1
        },
        {
          id: 4,
          name: '《代码大全》',
          date: '2006-3',
          price: 128.00,
          count: 1
        },
      ]
    },
    methods: {
      price(price) {
        return '￥' + price.toFixed(2)
      },
      reduce(index) {
        this.books[index].count--
      },
      increase(index) {
        this.books[index].count++
      },
      remove(index){
        this.books.splice(index,1)
      }
    },
    computed: {
      totleprice(){
        let totle = 0
        for(let i=0; i<this.books.length; i++){
          totle += this.books[i].price * this.books[i].count
        }
        // for in
        // for (let i in this.books) {
        //   total = total + this.books[i].price * this.books[i].count
        // }
        // for of
        // for (const book of this.books) {
        //   total = total + book.price * book.count
        // }
        return totle
        
        // 高阶函数
        // return this.books.map(function (book) {
        //   return book.price * book.count
        //  }).reduce(function (preValue,currentValue) {
        //     return preValue + currentValue
        //   })
        // 高阶函数简写（箭头函数）
        // return this.books.length === 0 ? 0 : this.books.map(book => book.price * book.count).reduce((preValue,currentVlue) => preValue + currentVlue)

      }
    }
  })
</script>
</body>
</html>
```



# 计算属性

`computed`

计算属性：在内存中运行，能够将计算结果缓存起来的属性（将行为转换为静态的属性）

对于任何复杂逻辑都应当使用**计算属性**

```html
<body>
<div id="app">
  <!-- Mastache语法 -->
  <h2>{{firstName+ " " + lastName}}</h2>
  <!-- 方法 -->
  <h2>{{getFullName()}}</h2>
  <!-- 计算属性 -->
  <h2>{{fullName}}</h2>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data:{
      firstName: 'ink',
      lastName: 'yinke'
    },
    computed: {
      fullName(){
        return this.firstName + " " + this.lastName
      }
    },
    methods: {
      getFullName(){
        return this.firstName + " " + this.lastName
      }
    },
  })
</script>
</body>
```

```html
<body>
<div id="app">
  <h2>总价格：{{totalPrice}}</h2>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      books:[
        {id:110,name:"JavaScript从入门到入土",price:119},
        {id:111,name:"Java从入门到放弃",price:80},
        {id:112,name:"编码艺术",price:99},
        {id:113,name:"代码大全",price:150},
      ]
    },
    computed: {
      totalPrice(){
        let result= 0;
        for (let i = 0; i < this.books.length; i++) {
          result += this.books[i].price;
        }
        return result
      }
    }
  })
</script>
</body>
```



## setter和getter

完整的计算属性是一个对象，里面包含`set`方法和`get`方法。一般只实现`get`方法（默认）

> 不实现`set`方法的计算属性相当于只读属性
>
> 也可以实现`set`方法：`set:function(newValue){}`

```html
<body>
<div id="app">
  <!-- Mastache语法 -->
  <h2>{{firstName+ " " + lastName}}</h2>
  <!-- 方法 -->
  <h2>{{getFullName()}}</h2>
  <!-- 计算属性 -->
  <h2>{{fullName}}</h2>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data:{
      firstName: 'ink',
      lastName: 'yinke'
    },
    computed: {
      // 实际实现,但一般省略get
      fullName:{
        get(){
          return this.firstName + " " + this.lastName
        }
      }
      // 等价写法
      // fullName: function(){
      //   return this.firstName + " " + this.lastName
      // }
    },
    methods: {
      getFullName(){
        return this.firstName + " " + this.lastName
      }
    }
  })
</script>
</body>
```



## 计算属性和方法对比

**缓存**

- 计算属性是基于响应式依赖进行**缓存**的，只有相关响应式依赖发生**改变时才会重新计算**求值。只要计算值没有发生改变，多次访问计算属性都会立即返回之前的计算结果而不必再次执行函数（**只执行一次**）
- `methods`没有缓存特性，方法**只要被调用就会再次执行函数**

**使用**

- `methods`定义方法，调用要加上`()`
- `computed`定义计算属性，直接调用属性名

> `computed`中的方法不要和`methods`中的方法同名，同名时默认使用`methods`中的方法

```html
<body>
<div id="vue">
  <p>{{currentTime1()}}: methods</p>
  <!-- 计算属性将不再更新，因为Date.now()不是响应式依赖 -->
  <p>{{currentTime2}}: computed</p>
</div>
<script src="vue.js"></script>
<script>
  const app = new Vue({
    el: '#vue',
    data: {
      message: 'ink'
    },
    methods: {
      currentTime1(){
        return Date.now();
      }
    },
    computed: {
      currentTime2(){
        return Date.now();
      }
    }
  })
</script>
</body>
```

![计算属性](Vue.js.assets/计算属性.png)



## 监听器





# Vue生命周期

每个Vue实例在被创建时都要经过一系列的**初始化过程**（例如需要设置数据监听、编译模板、将实例挂载到DOM 并在数据变化时更新DOM）

在这个过程中会运行（回调）一些叫做**生命周期钩子**的函数，可以让用户在不同阶段实现想要的功能

> 组件的生命周期也相似



## 钩子函数

**钩子函数Hook以属性（函数）的方式声明在Vue对象中**（`options`）

- `beforeCreate`：实例初始化之后，数据观测和事件配置之前被调用（页面创建之前）
- `created`：在实例创建完成后被立即调用（数据观测和事件配置已经完成），此时挂载阶段还没开始，`el`属性不可见
- `beforeMount`：挂载开始之前被调用，相关的渲染函数首次被调用
- `mounted`：挂载成功时调用，`el`被新创建的`vm.$el`替换
- `beforeUpdate`：数据更新时被调用
- `updated`：更新之后调用，组件DOM已经更新
- `activated`
- `deactivated`
- `beforeDestory`
- `destroyed`



![Vue生命周期](Vue.js.assets/Vue生命周期.png)

```html
<body>
<div id="app">
  <div>{{info.name}}</div>
  <div>{{info.links[0].name}}</div>
  <!-- 错误:<a href="{{info.url}}">点击</a> -->
  <!-- 要用v-bind绑定 -->
  <a v-bind:href="info.url">点击跳转</a>
</div>
<script src="vue.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      // 设置info为{}，自动绑定response的各个属性
      info: {}
    },
    // 钩子函数（链式编程）
    // data.json路径
    mounted(){
      // GET请求得到返回数据绑定到data中
      axios.get('data.json').then(response=>(this.info = response.data));
    }
  });
</script>
</body>
```

json文件

```json
{
  "name": "ink",
  "url": "https://www.baidu.com/",
  "page": 1,
  "isNonProfit": true,
  "address": {
    "street": "知春路",
    "city": "北京",
    "country": "中国"
  },
  "links": [
    {
      "name": "Vue",
      "url": "https://cn.vuejs.org/"
    },
    {
      "name": "leetcode",
      "url": "https://leetcode-cn.com/"
    },
    {
      "name": "知乎",
      "url": "https://www.zhihu.com/"
    }
  ]
}
```

![异步通信](Vue.js.assets/异步通信.png)

![axios](Vue.js.assets/axios.png)



# Vue组件

**Vue组件化思想**

将一个页面拆分成多个组件（功能块），每一个组件又可以进行细分。每个组件完成属于自己的独立功能

几乎任意类型的应用界面都可以抽象为一个**组件树**

> 组件系统是一种抽象，可以使用小型、独立和可复用的组件构建大型应用
>
> 尽可能的将页面拆分成一个个小的、可复用的组件

![VueComponents](Vue.js.assets/VueComponents.png)**Vue组件**

- 一个组件本质上是一个拥有预定义选项的，可复用的一个**Vue实例**
- 组件是的Vue实例，所以它与 `new Vue` 接收相同的选项（如 `data`、`computed`、`watch`、`methods` 以及生命周期钩子函数等），但不包括`el` 这样的**根实例**特有的选项
- 每个组件都会各自独立维护它的属性。每用一次组件，就会有一个它的新**实例**被创建

> Vue 组件提供了纯自定义元素所不具备的一些重要功能，最突出的是跨组件数据流、自定义事件通信以及构建工具集成。



**idea新建Vue组件**

![新建组件](Vue.js.assets/新建组件.png)

![Vue组件模板](Vue.js.assets/Vue组件模板.png)



## 使用组件

**步骤**

1. 调用`Vue.extend()`方法创建**组件构造器**
   - 传入`template`代表自定义组件模板（模板是在使用到组件的地方要显示的HTML代码）
2. 调用`Vue.component()`方法**注册组件**
   - 将组件构造器注册为一个组件，并给它起一个标签名称，需要传递两个参数：
     - 注册组件的**标签名**
     - **组件构造器**
3. 在**Vue实例的作用范围内**使用组件

> 下面这种写法在Vue2.x的文档中几乎已经看不到了，但是是基础

```html
<body>
<div id="app">
  <!--3.使用组件-->
  <my-cpn></my-cpn>
  <my-cpn></my-cpn>
</div>
<script src="vue.js"></script>
<script>
  // 1.创建组件构造器对象
  const cpnC = Vue.extend({
    template: `
    <div>
      <h2>我是标题</h2>
      <p>我是内容, 哈哈哈哈</p>
      <p>我是内容, 呵呵呵呵</p>
    </div>`
  })
  // 2.注册组件
  Vue.component('my-cpn', cpnC)
  
  const app = new Vue({
    el: '#app',
    data: {
      message: '你好啊'
    }
  })
</script>
</body>
```



**组件注册类型**

- **全局注册**

  调用`Vue.component()`注册的组件。该组件可以在任意Vue实例下使用

- **局部注册**

  通过 `components`注册的组件，挂载在某个实例中。只能在当前vue实例挂载的对象中使用



**注册组件语法糖**

Vue为了简化，省去了调用`Vue.extend()`的步骤，可以直接**使用一个对象**来代替

`component()`函数包含两个参数

1. 组件名称
2. 以对象的形式描述组件

> Vue 将**模板**编译成虚拟 DOM 渲染函数
>
> Vue 能够计算出最少需要重新渲染多少组件，并把 DOM 操作次数减到最少

```html
<body>
<div id="app">
   <!-- 调用组件：创建一个 ink 组件的实例 -->
   <ink></ink>
</div>
<script src="vue.js"></script>
<script src="js/ink.js"></script>
</body>
```

```javascript
// 定义名为 ink 的新组件
Vue.component("ink",{
   template: '<li>ink</li>'
});

// 创建Vue实例才可以调用
var vm = new Vue({
    el: '#app'
});

//可以在一个通过new Vue创建的Vue根实例中，把组件作为自定义元素来使用
new Vue({ 
    el: '#ink' 
});
```

## 父子组件

组件和组件之间存在层级关系，其中一种非常重要的关系就是**父子组件的关系**

## data

组件的 `data` **必须是一个函数**，因此每个实例可以维护一份被返回对象的独立的拷贝

> 否则可能会影响其他实例



## template

**单个根元素**：组件的模板必须只具备一个根元素

如果在组件内包含多个元素，**需要有一个根元素将他们一起包起来**，否则会报错（都是根元素）

![模板单根元素](Vue.js.assets/模板单根元素.png)

> 实现同一个模板内有多个HTML标签的效果

```javascript
// 错误写法：每个组件必须只有一个根元素
Vue.component('ink',{
    props: ['yinke','value'],
    template: '<li> {{yinke}} </li>' +
        '<li> {{value}} </li>'
});

// 正确写法：用div标签包起来
Vue.component('ink',{
    props: ['yinke','value'],
    template: '<div>' +
        '<li> {{yinke}} </li>' +
        '<li> {{value}} </li>' +
        '</div>'
});
```



## props

prop是可以**在组件上**注册的一些自定义attribute

当一个值传递给一个prop attribute 的时候，它就变成了那个**组件实例的一个属性**

一个组件默认可以拥有任意数量的prop，任何值都可以传递给任何 prop（在组件实例中访问这个值就像访问 `data` 中的值一样）

> 默认规则下，`props`属性中的值不能大写
>
> Vue中的保留关键字不能作为`props`中的属性，如`key`



**父作用域将数据传到子组件**

组件中的`template`不能从Vue对象的`data`中直接获得数据

1. `v-for`遍历Vue对象中的`data`数据
2. `v-bind`绑定`data`数据到组件中`props`定义的`item`属性中
3. `template`通过`props`中的属性获得数据

> `props`类似于一个自定义attribute

```html
<body>
<div id="app">
    <!-- 创建一个 ink 组件的实例 -->
    <!-- 等号左边的item是props定义的属性名，等号右边的item是v-for遍历的item项 -->
   <ink v-for="item in items" 
        v-bind:item="item"
   ></ink>

</div>
<script src="vue.js"></script>
<script src="js/ink.js"></script>
</body>
```

```javascript
Vue.component('ink',{
    props: ['item'],
    template: '<li>{{item}}</li>'
});

var vm = new Vue({
    el: '#app',
    data: {
        items: ["neau","buaa","fushan"]
    }
});
```

![数据绑定](Vue.js.assets/数据绑定.png)

```html
<body>
<div id="app">
    <ink v-for="item in items"
         v-bind:yinke="item.id"
         v-bind:value="item.title"
    ></ink>
</div>
<div id="components-demo">
    <button-counter v-for="item in items"
                    :title="item"
    ></button-counter>
</div>
<script src="vue.js"></script>
<script src="js/ink.js"></script>
</body>
```

```javascript
Vue.component('ink',{
    props: ['yinke','value'],
    template: '<div>' +
        '<li> {{yinke}} </li>' +
        '<li> {{value}} </li>' +
        '</div>'
});

var vm = new Vue({
    el: '#app',
    data: {
        items: [
            { id: 1, title: 'My journey with Vue' },
            { id: 2, title: 'Blogging with Vue' },
            { id: 3, title: 'Why Vue is so fun' }
        ]
    }
});

Vue.component('button-counter', {
    props: ['title'],
    data: function () {
        return {
            count: 0
        }
    },
    template: '<button v-on:click="count++">{{title}} clicked me {{ count }} times.</button>'
})

var com = new Vue({
    el: '#components-demo',
    data: {
        items: ['ink','yinke']
    }
})
```

![props样例](Vue.js.assets/props样例.png)

## 组件事件

### 监听子组件事件

> 开发组件的一些功能可能要和父级组件进行沟通

Vue实例提供了一个**自定义事件的系统**来解决这个问题：父级组件可以像处理native DOM事件一样**通过 `v-on` 监听子组件实例的任意事件**



### 使用事件抛出特定值



### 组件使用v-model

自定义事件也可以用于创建支持 `v-model` 的自定义输入组件

```html
<input v-model="searchText">
<!--等价于-->
<input
  v-bind:value="searchText"
  v-on:input="searchText = $event.target.value"
>
```



# Axios网络通信

`Axios`异步通信

开源的用在浏览器端和Node.js的异步通信框架，主要作用是实现Ajax异步通信

[Axios API 中文文档](http://axios-js.com/)

> Vue.js是一个视图层框架，并不包含Ajax的通信功能。
>
> jQuery.ajax()可以实现网络通信，但jQuery操作DOM太频繁，不推荐使用

## 功能特点

- 从浏览器中创建`XMLHttpRequests`（XHR）
- 从Node.js创建http请求
- 支持Promise API（JavaScript中链式编程）
- 拦截请求和响应
- 转换请求和响应数据
- 取消请求
- 自动转换JSON数据
- 客户端支持防御XSRF（跨站请求伪造）

> 要求ES6
>
> ![ES6](Vue.js.assets/ES6.png)

## 安装Axios

- **npm**

  ```bash
  npm install axios
  ```

- **cdn**

  ```html
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  ```



# 插槽slot

Vue.js中使用`<slot>`元素作为承载**分发内容**的出口，可以应用在组合组件中

- 插槽内可以包含任何模板代码，包括 HTML，甚至其它组件
- 每一个slot都会加载全部的插件

> Vue在2.6.0中为**具名插槽**和**作用域插槽**引入了一个新的统一的`v-slot` 指令
>
> `v-slot` 指令取代了 `slot` 和 `slot-scope` 这两个目前已被废弃但未被移除且仍在文档中的attribute

```html
<body>
<div id="app">

<todo>
	<!-- 插槽内包含组件 -->
    <todo-title  slot="todo-title"
                 v-bind:title="todotitle"
    ></todo-title>
    <!-- item在前,index在后-->
    <todo-item  slot="todo-item"
                v-for="(item,index) in todoitems"
                v-bind:item="item"
                v-bind:index="index"
    ></todo-item>
</todo>

</div>
<!--1.导入Vue.js-->
<script src="vue.js"></script>
<script src="js/ink.js"></script>
</body>
```

```javascript
// 定义插槽<slot></slot>
Vue.component('todo',{
    template:   '<div>' +
                    '<slot name="todo-title"></slot>' +
                        '<ul>' +
                            '<slot name="todo-item"></slot>' +
                        '</ul>' +
                '</div>'
});

Vue.component('todo-title',{
    props: ['title'],
    template:'<div>{{title}}</div>'
});

Vue.component("todo-item",{
    props: ['item','index'],
    template:"<li>{{index}} : {{item}}</li>"
});

var vm = new Vue({
    el:"#app",
    data:{
        todotitle: 'Vuedemo',
        todoitems:['buaa','neau','fushan']
    }
});
```

![内容分发](Vue.js.assets/内容分发.png)



## 作用域

- **父级模板里的所有内容都是在父级作用域中编译的**
- **子模板里的所有内容都是在子作用域中编译的**

在插槽中使用数据跟模板的其它地方一样可以访问相同的实例属性 (也就是相同的**作用域**)

```html
<navigation-link url="/profile">
  Logged in as {{ user.name }}
</navigation-link>
```

但**不能**访问 父级（`<navigation-link>`） 作用域

```html
<navigation-link url="/profile">
  Clicking here will send you to: {{ url }}
  <!-- 这里的url是undefined
	   因为该插槽的内容是传递给<navigation-link>标签的
	   而不是在<navigation-link>组件内部定义的
  -->
</navigation-link>
```



# 自定义事件

场景：数据在Vue的实例中， 但删除操作要在组件中完成

1. 组件可以调用自身`methods`中的方法，但无法访问实例`methods`中的方法

   ```javascript
   Vue.component("todo-item",{
       props: ['item','index'],
       // 想删除vm中的data属性中的数据，报错
       template:"<li>{{index}} : {{item}} <button v-on:click=\"removeitems\"> 删除</button></li>",
       methods: {
           remove: function (){
               alert("删除！")
           }
       }
   });
   var vm = new Vue({
       el:"#app",
       data:{
           todotitle: 'Vuedemo',
           todoitems:['buaa','neau','fushan'],
           methods: {
               // removeitems方法
               removeitems: function (){
                   alert("删除~~~")
               }
           }
       }
   });
   ```

   ![组件无法访问实例属性](Vue.js.assets/组件无法访问实例属性.png)

2. Vue实例可以调用自身`methods`中定义方法操作数据

   ```javascript
   var vm = new Vue({
       el:"#app",
       data: {
           todotitle: 'Vuedemo',
           todoitems: ['buaa', 'neau', 'fushan'],
       },
       methods: {
           removeitems: function (index){
               // splice()方法，删除一个元素
               console.log("删除了" + this.todoitems[index]);
               this.todoitems.splice(index,1);
           }
       }
   });
   ```

3. Vue提供**自定义事件**使得**组件能访问实例中的方法**从而操作实例中的数据

   `this.$emit('自定义事件名'，参数)`

   > 参数传递与事件分发
   >
   > 定义事件名不能和JavaScript关键字重名

   - 前端通过id属性和Vue实例绑定，可以调用Vue实例中的方法
   - 前端通过`v-on`将自定义事件传递给Vue实例的中的方法
   - 组件通过`this.$emit`绑定前端的自定义事件从而调用Vue实例中的方法

   > Vue实例将数据和方法与View层绑定，View层在分发数据和方法到下面的组件绑定。View相当于中转Vue实例的数据和方法由组件控制（前端：View层）
   >
   > 前端通过`v-bind`绑定Vue实例的数据，组件通过`props`绑定前端的数据
   
   ```html
   <body>
   <div id="app">
   <todo>
       <todo-title  slot="todo-title"
                    v-bind:title="todotitle"
       ></todo-title>
       <todo-item  slot="todo-item"
                   v-for="(item,index) in todoitems"
                   v-bind:item="item"
                   v-bind:index="index"
                   v-on:remove="removeitems(index)"
       ></todo-item>
   </todo>
   </div>
   <script src="vue.js"></script>
   <script src="js/ink.js"></script>
   </body>
   ```
   
   ```javascript
   Vue.component("todo-item",{
       props: ['item','index'],
       template:"<li>{{index}} : {{item}} <button v-on:click=\"removeI\">删除</button> </li>",
       methods: {
           removeI: function (index){
               this.$emit('remove',index);
           }
       }
   });
   var vm = new Vue({
       el:"#app",
       data: {
           todotitle: 'Vuedemo',
           todoitems: ['buaa', 'neau', 'fushan'],
       },
       methods: {
           removeitems: function (index){
               // splice()方法，删除一个元素
               console.log("删除了" + this.todoitems[index]);
               this.todoitems.splice(index,1);
           }
       }
   });
   ```
   
   ![自定义删除事件](Vue.js.assets/自定义删除事件.png)



# Vue-cli

`vue-cli`是官方提供的一个脚手架，用于快速生成一个Vue项目模板（自动生成好项目目录，配置好Webpack以及各种依赖包的工具）

> 实际开发采用Vue-cli脚手架，vue-router路由，vuex状态管理，Vue UI使用ElementUI来快速搭建前端项目



**主要功能**

- 统一的目录结构
- 本地调试
- 热部署
- 单元测试
- 集成打包上线

## 环境配置

> 以管理员身份运行

1. 安装Node.js：[Node.js|Download](https://nodejs.org/en/download/)（自动配置环境变量）

   ```bash
   # 验证
   node -v
   # 自带npm
   npm -v
   ```

   > npm类似CentOS下的yum和Ubuntu下的apt-get

2. 安装Node.js淘宝**镜像加速器**（cnpm）

   ```bash
   # -g 全局安装
   npm install cnpm -g
   
   # 或者每次安装包都加上参数--registry
   npm install --registry=https://registry.npm.taobao.org
   ```
   
   > C:\Users\54164\AppData\Roaming\npm
   >
   > 尽量使用npm，cnpm可能打包会失败
   
3. 安装Vue-cli

   > vue-cli3.0要nodeJs ≥ 8.9（官方推荐 8.11.0+）
   
   ```bash
   npm install vue-cli -g
   
   # 验证
   vue -V
   
   # 查看可以基于哪些模板创建vue应用程序(通常选择webpack)
   vue list
   ```
   
   ![Vue-list](Vue.js.assets/Vue-list.png)

## 创建程序

创建一个基于`webpack`模板的Vue应用程序

1. **进入项目目录**

2. **创建项目**

   ```bash
   vue init webpack 项目名
   ```

3. **设置**

   - Project name：项目名称，默认回车即可
   - Project description：项目描述，默认回车即可
   - Author：项目作者，默认回车即可
   - Install vue-router：是否安装vue-router，选择n不安装（后期需要再手动添加）
   - Use ESLint to lint your code:是否使用ESLint做代码检查，选择n不安装（后期需要再手动添加)
   - Set up unit tests:单元测试相关，选择n不安装（后期需要再手动添加）
   - Setupe2etests with Nightwatch：单元测试相关，选择n不安装（后期需要再手动添加）
   - Should we run npm install for you after the,project has been created:创建完成后直接初始化，选择n，手动执行

   ![创建Vue-cli项目](Vue.js.assets/创建Vue-cli项目.png)

4. **初始化项目**

   在项目目录下安装依赖(根据项目中的`package.json`文件)，生成`node_modules`文件夹

   自动生成的package.json版本有问题

   > webpack3.0及其以上或4.0以下版本自带webpack-cli，不需要额外安装。而4.0以上则需要

   ```json
   {
     "name": "myvue",
     "version": "1.0.0",
     "description": "A Vue.js project",
     "author": "lzh <luzehua@zhongbei.com>",
     "private": true,
     "scripts": {
       "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
       "start": "npm run dev",
       "build": "node build/build.js"
     },
     "dependencies": {
       "vue": "^2.5.2"
     },
     "devDependencies": {
       "autoprefixer": "^7.1.2",
       "babel-core": "^6.22.1",
       "babel-helper-vue-jsx-merge-props": "^2.0.3",
       "babel-loader": "^7.1.1",
       "babel-plugin-syntax-jsx": "^6.18.0",
       "babel-plugin-transform-runtime": "^6.22.0",
       "babel-plugin-transform-vue-jsx": "^3.5.0",
       "babel-preset-env": "^1.3.2",
       "babel-preset-stage-2": "^6.22.0",
       "chalk": "^2.0.1",
       "copy-webpack-plugin": "^4.0.1",
       "css-loader": "^0.28.0",
       "extract-text-webpack-plugin": "^3.0.0",
       "file-loader": "^1.1.4",
       "friendly-errors-webpack-plugin": "^1.6.1",
       "html-webpack-plugin": "^2.30.1",
       "node-notifier": "^5.1.2",
       "optimize-css-assets-webpack-plugin": "^3.2.0",
       "ora": "^1.2.0",
       "portfinder": "^1.0.13",
       "postcss-import": "^11.0.0",
       "postcss-loader": "^2.0.8",
       "postcss-url": "^7.2.1",
       "rimraf": "^2.6.0",
       "semver": "^5.3.0",
       "shelljs": "^0.7.6",
       "uglifyjs-webpack-plugin": "^1.1.1",
       "url-loader": "^0.5.8",
       "vue-loader": "^13.3.0",
       "vue-router": "^3.3.4",
       "vue-style-loader": "^3.0.1",
       "vue-template-compiler": "^2.5.2",
       "webpack": "^3.6.0",
       "webpack-bundle-analyzer": "^2.9.0",
       "webpack-dev-server": "^2.9.1",
       "webpack-merge": "^4.1.0"
     },
     "engines": {
       "node": ">= 6.0.0",
       "npm": ">= 3.0.0"
     },
     "browserslist": [
       "> 1%",
       "last 2 versions",
       "not ie <= 8"
     ]
   }
   ```

   > npm版本过高可能会报错，需要降低版本
   >
   > warn不用管

   ```bash
   # 降低版本
   npm install npm@6.14.10 -g
   # 安装依赖
   npm install

5. **运行项目**

   webpack打包并运行

   ```bash
   npm run dev
   ```

   > `ctrl+c`停止
   >
   > 端口号配置文件：`config`目录下的index.js中的port

   ![启动vue-cli](Vue.js.assets/启动vue-cli.png)

6. **package.json** 

   可以看到**开发和生产 环境的入口**

   - dev：开发环境的启动命令

   - build：生产打包环境的命令

     > 运行 `npm run build` 命令就可以进行打包工作。打包完成后会生成 `dist` 目录，项目上线时，把`dist` 目录下的文件放到服务器就可以了

   ```json
   "scripts": {
       "dev": "webpack-dev-server --inline --progress --config build/webpack.dev.conf.js",
       "start": "npm run dev",
       "build": "node build/build.js"
   },
   ```



## idea

- 以管理员身份运行idea
- `File`->`Open`打开项目目录
- 在idea中的终端执行命令运行项目

> 项目入口：main.js绑定到index.html

![export导出](Vue.js.assets/export导出.png)

![import导入](Vue.js.assets/import导入.png)



# Webpack

- Webpack是一个现代JavaScript应用程序的静态模块**打包工具**(module bundler) 
- Wbpack处理应用程序时会递归地构建一个**依赖关系图**(dependency graph) ， 包含应用程序需要的每个模块， 然后将所有这些模块打包成一个或多个bundle
- Webpack可以将松散耦合的模块按照依赖和规则打包成**符合生产环境部署的前端资源**。还可以将按需加载的模块进行代码分离，等到实际需要时再异步加载。通过loader转换， 任何形式的资源都可以当做模块， 比如Commons JS、ES6、CSS、JSON、CoffeeScript等

> 现在越来越多的网站已经从网页模式进化到了WebApp模式，运行在浏览器里。 WebApp通常是一个SPA(单页面应用) ， 每一个视图通过异步的方式加载，这导致页面初始化和使用过程中会加载越来越多的JavaScript代码
>
> 前端开发和其他开发工作的主要区别：
>
> - 前端基于多语言、多层次的编码和组织工作
> - 前端产品的交付是基于浏览器的，这些资源是通过增量加载的方式运行到浏览器端



[Vue.js新手入门指南 ](https://zhuanlan.zhihu.com/p/25659025)

> - 前端代码为什么要打包呢？
>   因为单页应用程序中用到很多素材，如果每一个素材都通过在HTML中以src属性或者link来引入，那么请求一个页面的时候，可能浏览器就要发起十多次请求，往往请求的这些资源都是一些脚本代码或者很小的图片，这些资源本身才几k，下载连1秒都不需要，但是由于HTTP是应用层协议，它的下层是TCP这个运输层协议，TCP的握手和挥手过程消耗的时间可能比下载资源本身还要长，所以需要把这些小文件全部打包成一个文件，这样只要一次TCP握手和挥手的过程，就把多个资源给下载下来了，并且多个资源由于都是共享一个HTTP请求，所以head等部分也是共享的，相当于形成了规模效应，让网页展现更快，用户体验更好。
> - Webpack还有构建的功能
>   现在国内外还有很多人用着老版本的浏览器，这些浏览器并不支持ECMAScript6这个新版本的JavaScript，那么前端项目如何在这种浏览器上运行呢？这就需要Webpack的Loader自动载入一个转换器来将ECMAScript6转换成浏览器能支持的老版本JavaScript语言，这个转换器的名字叫做babel。这就是Webpack的构建功能。

## 规范

### CommonsJS规范

服务器端的Node.js遵循**CommonsJS规范**

核心思想是允许模块通过`require`方法来**同步加载**所需依赖的其它模块，然后通过`exports`或`module.exports`来导出需要暴露的接口

```javascript
require("module");
require("../module.js");
exports.doStuff = function(){};
module.exports = someValue;
```

**优点：**

- 服务器端模块便于重用
- NPM中已经有超过45万个可以使用的模块包
- 简单易用

**缺点：**

- 同步的模块加载方式不适合在浏览器环境中，同步意味着阻塞加载，浏览器资源是异步加载的
- 不能非阻塞的并行加载多个模块

**实现：**

- 服务端的NodeJS
- Browserify，浏览器端的CommonsJS实现，可以使用NPM的模块，但是编译打包后的文件体积较大
- modules-webmake，类似Browserify，但不如Browserify灵活
- wreq，Browserify的前身



### AMD规范

Asynchronous Module Definition规范主要是一个接口`define(id,dependencies,factory)`

在声明模块的时候指定所有的依赖`dependencies`并当做形参传到`factory`中，对于依赖的模块**提前执行**

```javascript
define("module",["dep1","dep2"],functian(d1,d2){
	return someExportedValue;
});
require（["module","../file.js"],function(module，file){});
```

**优点：**

- 适合在浏览器环境中**异步加载模块**
- 可以**并行加载**多个模块

**缺点：**

- 提高了开发成本，代码的阅读和书写比较困难，模块定义方式的语义不畅
- 不符合通用的模块化思维方式

**实现：**

- RequireJS
- curl



### CMD规范

Commons Module Definition规范和AMD相似，并与CommonsJS和NodeJS的Modules规范保持了很大的兼容性

```javascript
define(function(require,exports,module){
	var $=require("jquery");
	var Spinning = require("./spinning");
	exports.doSomething = ...;
	module.exports=...;
});
```

**优点：**

- 依赖就近，延迟执行
- 可以很容易在Node.js中运行

**缺点：**

- 依赖SPM打包，模块的加载逻辑偏重



### ES6模块

EcmaScript6标准增加了JavaScript语言层面的模块体系定义

**ES6模块的设计思想使编译时就能确定模块的依赖关系， 以及输入和输出的变量**。

> 严格检查模式`strict`
>
> Commons JS和AMD模块都只能在**运行时**确定这些东西

```javascript
import "jquery"
export function doStuff(){}
module "localModule"{}
```

**优点**

- 容易进行静态分析
- 面向未来的EcmaScript标准

**缺点**

- 原生浏览器端还没有实现该标准
- 全新的命令，新版的Node.js才支持



## 安装

```bash
# 打包工具
npm install webpack -g

# 客户端
npm install webpack-cli -g

# 验证
webpack -v
webpack-cli -v
```



## 配置

创建 `webpack.config.js`配置文件

- `entry`：入口文件， 指定webpack用哪个文件作为项目的入口
- `output`：输出， 指定webpack把处理完成的文件放到的路径
- `module`：模块， 用于处理各种类型的文件
- `plugins`：插件， 如热更新、代码重用等
- `resolve`：设置路径指向
- `watch`：监听， 用于设置文件改动后直接打包

```javascript
module.exports = {
	entry:"",
	output:{
		path:"",
		filename:""
	},
	module:{
		loaders:[
			{test:/\.js$/,;\loade:""}
		]
	},
	plugins:{},
	resolve:{},
	watch:true
}
```

运行`webpack`命令打包



## 运行

1. 创建webpack项目目录（空）

2. 在idea中**open**项目目录

3. 在**项目目录下**创建`modules`目录（Directory）

4. 在`modules`目录下创建模块文件hi.js，用于编写JavaScript模块相关代码

   ```javascript
   // 暴露一个方法
   exports.sayhi = function (){
       document.write("<h1>ink say hi!</h1>");
   }
   ```

5. 在`modules`目录下创建入口文件main.js，用于打包时设置`entry`属性

   ```javascript
   // 接收方法
   // 模块不用写.js后缀
   var hi = require("./hi");
   hi.sayhi();
   ```

6. 在**项目目录下**创建webpack.config.js配置文件，在idea终端中使用`webpack`命令打包

   ![webpack打包](Vue.js.assets/webpack打包.png)

7. 在**项目目录下**创建index.html，导入webpack打包后的JavaScript文件

   ```html
   <body>
   <!--导入包-->
   <script src="dist/js/bundle.js"></script>
   </body>
   ```



# Vue-router

Vue Router是Vue.js官方的路**由管理器**。

**功能：**

- 嵌套的路由/视图表
- 模块化的、基于组件的路由配置
- 路由参数、查询、通配符
- 基于Vue js过渡系统的视图过渡效果
- 细粒度的导航控制
- 带有自动激活的CSS class的链接
- HTML5 历史模式或hash模式， 在IE 9中自动降级
- 自定义的滚动行为

> Vue-route管理请求入口和页面映射关系，可以实现对页面局部进行无刷新的替换，让用户感觉就像切换到了网页一样
>
> 单页应用程序（SPA）：单页应用一般指的就是一个页面就是应用，当然也可以是一个子应用。单页应用程序中一般交互处理非常多，而且页面中的内容需要根据用户的操作动态变化。



## 安装

在idea的终端中执行命令安装

```bash
# --save-dev保存到node_modules目录下
npm install vue-router --save-dev
```

如果在一个模块化工程中使用vue-router，必须要通过`Vue.use()`显示声明

```vue
// 导入
import VueRouter from 'vue-router'

// 显示声明使用VueRouter
Vue.use(VueRouter);
```

## 运行

> 前端命名规则：`index.js`一般是主配置文件，会默认加载

1. 在`components` 目录下编写`Content.vue` 组件

   ```vue
   <template>
     <h1>内容页: router跳转!</h1>
   </template>
   <script>
   export default {
     name: "Content"
   }
   </script>
   <!-- scoped限制作用域 -->
   <style scoped>
   </style>
   ```

2. 在`components` 目录下编写`Main.vue` 组件

   ```vue
   <template>
       <h1>首页！</h1>
   </template>
   <script>
   export default {
     name: "Main"
   }
   </script>
   <style scoped>
   </style>
   ```

3. 在`src`目录下新建路由文件夹`router`专门存放路由

   在配`router`目录下新建路由主配置文件`index.js`

   1. 导入路由（import组件）
   2. 配置路由（跳转组件）

   ```javascript
   // index.js 主配置文件
   import Vue from 'vue'
   // 导入路由
   import VueRouter from 'vue-router'
   // 导入自定义组件
   import Content from '../components/Content'
   import Main from '../components/Main'
   // 安装路由
   Vue.use(VueRouter);
   // 配置导出路由
   export default new VueRouter({
     routes: [
       {
         // 路由路径
         path: '/content',
         // 路由名(可省略)
         name: 'content',
         // 跳转组件
         component: Content
       },
       {
         path: '/main',
         name: 'main',
         component: Main
       }
     ]
   })
   ```

4. 在`main.js`中配置路由

   ```javascript
   // 导入组件
   import Vue from 'vue'
   import App from './App'
   
   // 会自动扫描里面的路由配置index.js(不用写)
   import router from './router'
   
   Vue.config.productionTip = false;
   
   new Vue({
     el: '#app',
     // 配置路由
     router,
     components: { App },
     template: '<App/>'
   })
   ```

5. 在`App.vue`中使用路由

   - `router-link`：控制路由
   - `router-view`：控制页面展示

   ```vue
   <template>
     <div id="app">
       <h1>Vue-router</h1>
       <!-- router-link默认会被渲染成一个<a>标签，to属性为指定链接 -->
       <router-link to="/main" >首页</router-link>
       <router-link to="/content">内容页</router-link>
       <!-- router-view：用于渲染路由匹配到的组件 -->
       <router-view></router-view>
     </div>
   </template>
   
   <script>
   export default {
     name: 'App'
   }
   </script>
   
   <style></style>
   ```

![main](Vue.js.assets/main.png)

![content](Vue.js.assets/content.png)



# Vue-ElementUI

## 创建项目

- `npm install moduleName`：安装模块到项目目录下
- `npm install -g moduleName`：`-g`表示将模块安装到全局（具体位置看npm config prefix)
- `npm install -save moduleName`：`–save`表示将模块安装到项目目录下， 并在`package.json`文件的`dependencies`节点写入依赖（缩写为-S)
- `npm install -save-dev moduleName`：`–save-dev`表示将模块安装到项目目录下，并在`package.json`文件的`devDependencies`节点写入依赖（缩写为-D)

```bash
# 新建项目
vue init webpack hello-vue

#进入项目目录
cd hello-vue

#安装Vue-router
npm install vue-router --save-dev

#安装ElementUI
npm i element-ui -S

#安装依赖
npm install

# 安装SASS加载器(sass-loader和node-sass)
cnpm install sass-loader node-sass --save-dev

#启功
npm run dev
```

**调整项目结构**

在`src`目录中创建目录：

- assets：存放资源文件
- components：存放Vue功能组件
- views：存放Vue视图组件
- router：存放vue-router路由配置

![目录结构](Vue.js.assets/目录结构.png)

**创建首页视图**

在`views`目录下创建`Main.vue`视图组件

```vue
<template>
  <h1>首页</h1>
</template>
<script>
export default {
  name: "Main"
}
</script>
<style scoped>
</style>
```

**创建登录页视图**

在`views`目录下创建`Login.vue`视图组件

> `el-form`的元素为ElementUI组件

```vue
<template>
  <div>
    <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
      <h3 class="login-title">欢迎登录</h3>
      <el-form-item label="账号" prop="username">
        <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-on:click="onSubmit('loginForm')">登录</el-button>
      </el-form-item>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>请输入账号和密码</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      form: {
        username: '',
        password: ''
      },

      // 表单验证，需要在 el-form-item 元素中增加 prop 属性
      rules: {
        username: [
          {required: true, message: '账号不可为空', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不可为空', trigger: 'blur'}
        ]
      },

      // 对话框显示和隐藏
      dialogVisible: false
    }
  },
  methods: {
    onSubmit(formName) {
      // 为表单绑定验证功能
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
          this.$router.push("/main");
        } else {
          this.dialogVisible = true;
          return false;
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.login-box {
  border: 1px solid #DCDFE6;
  width: 350px;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
}

.login-title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #303133;
}
</style>

```

**创建路由**

在`router`目录下创建`index.js`路由配置文件

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
// 导入组件
import Main from '../views/Main'
import Login from '../views/Login'

Vue.use(VueRouter);

export default new VueRouter({
  routes:[
    {
      path: '/main',
      name: 'main',
      component: Main
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
});
```

**APP.vue**

```vue
<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
```

**main.js**

入口文件

```javascript
import Vue from 'vue'
import App from './App'
// 导入路由
import router from "./router"
// 导入ElementUI和css文件
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(router)
Vue.use(ElementUI)

new Vue({
  el: '#app',
  router,
  // 引入element-ui
  render:h=>h(App)
})

```

**运行**

> 安装问题：Error:Node Sass version 5.0.0 is incompatible with ^4.x
>
> 解决方案：此错误来自sass-loader，因为node-sass@latest为v5.0.0而sass-loader期望值为^4.0.0
>
> ```bash
> //卸载 node-sass
> npm uninstall node-sass
> 
> //然后安装最新版本（5.0之前）
> npm install node-sass@4.14.1
> ```
>
> sass-loader版本太高，修改："sass-loader": "^7.3.1" 

![登录页面](Vue.js.assets/登录页面.png)



## 嵌套路由

嵌套路由又称子路由。URL中各段**动态路径也**按某种结构对应**嵌套的各层组件**

![嵌套路由](Vue.js.assets/嵌套路由.png)

在`views`目录下创建`user`目录

在`user`目录下创建`Profile.vue`视图组件

```vue
<template>
  <h1>个人信息</h1>
</template>
<script>
export default {
  name: "Profile"
}
</script>
<style scoped>
</style>
```

在`user`目录下创建`UserList.vue`视图组件

```vue
<template>
  <h1>用户列表</h1>
</template>
<script>
export default {
  name: "UserList"
}
</script>
<style scoped>
</style>
```

**配置嵌套路由**

修改`router`目录下的`index.js`路由配置文件

添加`children`

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main'
import Login from '../views/Login'

import Profile from '../views/user/Profile'
import Userlist from '../views/user/UserList'

Vue.use(VueRouter);

export default new VueRouter({
  routes:[
    {
      path: '/main',
      name:'main',
      component:Main,
      // 嵌套路由
      children: [
        {
          path: '/user/Profile',
          component: Profile
        },
        {
          path: '/user/UserList',
          component: UserList
        }
      ]
    },{
      path:'/login',
      name:'login',
      component: Login
    }
  ]
});
```

**修改首页视图**

使用ElementUI布局容器组件修改`Main.vue`视图组件

```vue
<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <el-menu :default-openeds="['1']">
          <!-- 第一部分 -->
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-caret-right"></i>用户管理</template>
            <el-menu-item-group>
                
              <el-menu-item index="1-1">
                <!-- router-link展示 -->
                <router-link to="/user/profile">个人信息</router-link>
              </el-menu-item>
                
              <el-menu-item index="1-2">
                <router-link to="/user/UserList">用户列表</router-link>
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>

		  <!-- 第二部分 -->
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-caret-right"></i>内容管理</template>
            <el-menu-item-group>
              <el-menu-item index="2-1">分类管理</el-menu-item>
              <el-menu-item index="2-2">内容列表</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>个人信息</el-dropdown-item>
              <el-dropdown-item>退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </el-header>
          
        <!-- router-view显示 -->
        <el-main>
          <router-view />
        </el-main>
          
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Main"
}
</script>

<style scoped lang="scss">
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}
.el-aside {
  color: #333;
}
</style>
```

![用户列表](Vue.js.assets/用户列表.png)



## 参数传递

把某种模式**匹配到的所有路由全都映射到同个组件**，根据**不同的属性**用组件渲染就需要用参数传递

**$route方式**

在`Main.vue`中修改`router-link to`接收参数`name`和`params`

```vue
<el-menu-item index="1-1">
  <!-- router-link展示 -->
  <!-- 参数传递需要对象,v-bind绑定:name组件名,params传递参数 -->
  <router-link :to="{ name:'Profile', params:{id:1} }">个人信息</router-link>
</el-menu-item>
```

修改路由配置`index.js`，在`path`属性中增加`:id`占位符（对应params参数名匹配），接受参数

```javascript
 children: [
        {
          // 接受参数id
          path: '/user/Profile/:id',
          name: 'Profile',
          component: Profile
        },
        {
          path: '/user/UserList',
          component: UserList
        }
      ]
```

修改`Profile.vue`中的`template`标签展示参数信息

```vue
<template>
<!--  只能有一个根标签-->
  <div>
    <h1>个人信息</h1>
    {{$route.params.id}}
  </div>
</template>
```

![参数传递](Vue.js.assets/参数传递.png)

**props方式**

在`Main.vue`中修改`router-link to`接收参数`name`和`params`

```vue
<el-menu-item index="1-1">
  <!-- router-link展示 -->
  <!-- 参数传递需要对象,v-bind绑定:name组件名,params传递参数 -->
  <router-link :to="{ name:'Profile', params:{id:1} }">个人信息</router-link>
</el-menu-item>
```

修改路由配置 `index.js`，在`chidren`中增加`props`属性（表明支持传递参数方式）

```javascript
children: [
        {
          // 接受参数id
          path: '/user/Profile/:id',
          name: 'Profile',
          component: Profile,
          props: true
        },
        {
          path: '/user/UserList',
          component: UserList
        }
      ]
```

修改`Profile.vue`，增加`props`属性

```vue
<template>
<!--  只能有一个根标签-->
  <div>
    <h1>个人信息</h1>
    {{id}}
  </div>
</template>

<script>
export default {
  props: ['id'],
  name: "Profile"
}
```

**获取用户名**

修改`Login.vue`中的`methods`中的`onSubmit`，增加`+this.form.username`

```vue
<template>
  <div>
    <el-form ref="loginForm" :model="form" :rules="rules" label-width="80px" class="login-box">
      <h3 class="login-title">欢迎登录</h3>
      <el-form-item label="账号" prop="username">
        <el-input type="text" placeholder="请输入账号" v-model="form.username"/>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" placeholder="请输入密码" v-model="form.password"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" v-on:click="onSubmit('loginForm')">登录</el-button>
      </el-form-item>
    </el-form>

    <el-dialog
      title="温馨提示"
      :visible.sync="dialogVisible"
      width="30%">
      <span>请输入账号和密码</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      // 当前用户信息
      form: {
        username: '',
        password: ''
      },

      // 表单验证，需要在 el-form-item 元素中增加 props 属性
      rules: {
        username: [
          {required: true, message: '账号不可为空', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不可为空', trigger: 'blur'}
        ]
      },

      // 对话框显示和隐藏
      dialogVisible: false
    }
  },
  methods: {
    onSubmit(formName) {
      // 为表单绑定验证功能
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 使用 vue-router 路由到指定页面，该方式称之为编程式导航
          // 获取username信息
          this.$router.push("/main/"+this.form.username);
        } else {
          this.dialogVisible = true;
          return false;
        }
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.login-box {
  border: 1px solid #DCDFE6;
  width: 350px;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  box-shadow: 0 0 25px #909399;
}

.login-title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #303133;
}
</style>
```

修改路由配置`index.js`，在`path`属性中增加`:name`占位符并设置`props`属性

```javascript
{
      path: '/main/:name',
      name:'main',
      component:Main,
      props:true,
      // 嵌套路由
      children: [
        {
          // 接受参数id
          path: '/user/Profile/:id',
          name: 'Profile',
          component: Profile,
          props: true
        }
```

修改`Main.vue`

- 增加`props`属性
- 显示`name`信息

```vue
<template>
  <div>
    <el-container>
      <el-aside width="200px">
        <el-menu :default-openeds="['1']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-caret-right"></i>用户管理</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <!-- router-link展示 -->
                <!-- 参数传递需要对象,v-bind绑定:name组件名,params传递参数 -->
                <router-link :to="{ name:'Profile', params:{id:1} }">个人信息</router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/user/UserList">用户列表</router-link>
              </el-menu-item>
              <el-menu-item index="1-3">
                <router-link to="/goHome">回到主页</router-link>
              </el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-caret-right"></i>内容管理</template>
            <el-menu-item-group>
              <el-menu-item index="2-1">分类管理</el-menu-item>
              <el-menu-item index="2-2">内容列表</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>个人信息</el-dropdown-item>
              <el-dropdown-item>退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <!-- 显示name信息 -->
          <span>{{name}}</span>
        </el-header>
        <!-- router-view显示 -->
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  <!-- 增加props属性 -->
  props: ['name'],
  name: "Main"
}
</script>

<style scoped lang="scss">
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}
.el-aside {
  color: #333;
}
</style>

```

![显示name](Vue.js.assets/显示name.png)

## 重定向

`redirect`

Vue中的重定向是作用在**路径不同但组件相同**的情况下

修改路由配置`index.js`，在`routes`中需要重定向的路径，并使用`redirect`属性指定重定向路径

```javascript
routes:[
  {
    path: '/main',
    name:'main',
    component:Main,
    // 嵌套路由
    children: [
      {
        // 接受参数id
        path: '/user/Profile/:id',
        name: 'Profile',
        component: Profile,
        props: true
      },
      {
        path: '/user/UserList',
        component: UserList
      }
    ]
  },{
    path:'/login',
    name:'login',
    component: Login
  },{
    path: '/goHome',
    redirect: '/main'
  }
]
```

在`Main.vue`中添加`router-link`

```vue
<el-menu-item index="1-3">
  <router-link to="/goHome">回到主页</router-link>
</el-menu-item>
```

![重定向](Vue.js.assets/重定向.png)

## 路由模式

路由模式有两种

- `hash`：路径带`#`，如 http://localhost:8080/#/main/ink（默认为hash路由模式）
- `history`：路径不带`#`，如 http://localhost:8080/main/ink

`mode`：设置路由模式

修改路由配置`index.js`，增加`mode`属性

```javascript
export default new VueRouter({
  // 设置路由模式
  mode: 'history',
  routes:[
    {
      path: '/main/:name',
      name:'main',
      component:Main,
      props:true,
      // 嵌套路由
      children: [
        {
          // 接受参数id
          path: '/user/Profile/:id',
          name: 'Profile',
          component: Profile,
          props: true
        },
        {
          path: '/user/UserList',
          component: UserList
        }
      ]
    },{
      path:'/login',
      name:'login',
      component: Login
    },{
      path: '/goHome',
      redirect: '/main'
    }
  ]
});
```

![路由模式](Vue.js.assets/路由模式.png)

## 404NotFound

在`views`目录下创建`NotFound.vue`

```vue
<template>
<div>
  <h1>404 你的页面走丢了</h1>
</div>
</template>
<script>
export default {
  name: "NotFound"
}
</script>
<style scoped>
</style>
```

配置路由`index.js`

```javascript
{
  // 匹配所有其他的路径
  path: '*',
  component: NotFound
}
```

![404](Vue.js.assets/404.png)

## 路由钩子函数

创建Vue对象前先执行钩子函数

- `beforeRouteEnter`：进入路由前执

- `beforeRouteLeave`：离开路由前执行

  参数

  - `to`：路由将要跳转的路径信息
  - `from`：路径跳转前的路径信息
  - `next`：路由的控制参数
    - `next()`：跳入下一个页面
    - `next(’/path’)`：改变路由的跳转方向，使其跳到另一个路由
    - `next(false)`：返回原来的页面
    - `next((vm)=>{})`：仅在`beforeRouteEnter`中可用，vm 是组件实例

修改`Profile.vue`

```vue
export default {
  props: ['id'],
  name: "Profile",
  beforeRouteEnter:(to,from,next)=>{
    // 业务代码
    console.log('进入路由之前')
    next();
  },
  beforeRouteLeave:(to,from,next)=>{
    // 业务代码
    console.log('离开路由之前')
    next();
  }
}
```



# Vue CLI

vue cli3版本和vue cli2 相比文件目录少了很多配置，没有了build和config目录，那么像vue cli2 之前的关于端口号的配置，打包之后路径的配置，图片的配置 等等

vue cli3 可以在项目根目录新建一个vue.config.js文件，像之前的很多繁琐配置，都可以在这个文件里配置啦


vue.config.js

一个可选的配置文件，如果项目的 (和 `package.json` 同级的) **根目录**中存在这个文件，那么它会被 `@vue/cli-service` 自动加载。

[Vue CLI (vuejs.org)](https://cli.vuejs.org/zh/config/#vue-config-js)



process（进程）其实就是存在nodejs中的一个全局变量。

process.env属性返回一个包含用户环境信息的对象。

[Node.js中环境变量process.env详解](https://www.jb51.net/article/126838.htm#)