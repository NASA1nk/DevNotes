# 敏捷开发

`Agile`

一种以人为核心、迭代、循序渐进的开发方法

- 在敏捷开发中，软件项目的构建被切分成多个子项目，各个子项目的成果都经过测试，具备集成和可运行的特征

- 简单地来说，**敏捷开发并不追求前期完美的设计、完美编码，而是力求在很短的周期内开发出产品的核心功能，尽早发布出可用的版本**，然后在后续的生产周期内，按照新需求不断迭代升级，完善产品

# CICD

CI/CD 其实就是一个**流程**（通常形象地表述为管道pipeline），用于实现应用开发中的高度持续自动化和持续监控 

## CI

Continuous Integration

- CI始终指**持续集成**，它属于开发人员的自动化流程

- 成功的CI意味着应用代码的新更改会定期构建、测试并合并到共享存储库中，可以解决在一次开发中有太多应用分支，从而导致相互冲突的问题

## CD

CD指的是**持续交付**或**持续部署**

- 这两个概念有时会交叉使用，两者都事关管道后续阶段的自动化
- 有时也会单独使用，用于说明自动化程度

### 持续交付

Continuous Delivery

- 通常是指开发人员对应用的更改会自动进行错误测试并上传到存储库，然后由运维团队将其部署到实时生产环境中

- 目的是解决开发和运维团队之间可见性及沟通较差的问题

因此，持续交付的目的就是确保尽可能减少部署新代码时所需的工作量

### 持续部署

Continuous Deployment

- 指的是自动将开发人员的更改从存储库发布到生产环境，以供客户使用
- 主要为了解决因手动流程降低应用交付速度，从而使运维团队超负荷的问题

持续部署以持续交付的优势为根基，实现了管道后续阶段的自动化

> CI/CD既可能仅指持续集成和持续交付构成的关联环节，也可以指持续集成、持续交付和持续部署这三项构成的关联环节
>
> 更为复杂的是，有时持续交付也包含了持续部署流程

## 流程

1. 一旦开发人员对应用所做的更改被合并，系统就会通过自动构建应用并运行不同级别的**自动化测试**（通常是单元测试和集成测试）来验证这些更改，确保这些更改没有对应用造成破坏
   1. 这意味着测试内容涵盖了从类和函数到构成整个应用的不同模块，如果自动化测试发现新代码和现有代码之间存在冲突，CI可以更加轻松地快速修复这些错误
2. 完成CI中构建及单元测试和集成测试的自动化流程后，**持续交付可自动将已验证的代码发布到存储库**
   1. 为了实现高效的持续交付流程，务必要确保CI已内置于开发管道
   2. 持续交付的目标是拥有一个可随时部署到生产环境的代码库
   3. 在持续交付中，每个阶段（从代码更改的合并，到生产就绪型构建版本的交付）都涉及测试自动化和代码发布自动化，在流程结束时，运维团队可以快速、轻松地将应用部署到生产环境中
3. 对于一个成熟的CI/CD管道来说，最后的阶段是持续部署，作为持续交付的延伸，**持续部署可以自动将应用发布到生产环境**
   1. 由于在生产之前的管道阶段没有手动门控，因此持续部署在很大程度上都得依赖精心设计的测试自动化
   2. 实际上，持续部署意味着开发人员对应用的更改在编写后的几分钟内就能生效（假设它通过了自动化测试），这更加便于持续接收和整合用户反馈


# 灰度发布

又叫**金丝雀发布**，是指在黑与白之间，能够**平滑过渡**的一种发布方式

- 在其上可以进行**A/B testing**，让一部分用户继续用产品特性A，一部分用户开始用产品特性B，如果用户对B没有什么反对意见，那么逐步扩大范围，把所有用户都迁移到B上面来
- 灰度发布可以保证整体系统的稳定，在初始灰度的时候就可以发现、调整问题，以保证其影响度

**灰度放量**：对产品的发布逐步扩大使用群体范围

**灰度期**：灰度发布开始到结束期间的这一段时间

> 初次发布给少量用户，发现问题希望用户及时反馈，修复/上线，稳定阶段扩大用户，所有用户可见，灰度发布结束
>
> 设定分流规则，调整分流规则

# YAML

## 基本语法

* 大小写敏感
* 使用缩进表示层级关系，使用**空格做为缩进**
  * 缩进的空格数目不重要，只要相同层级的元素左侧**对齐即可**
  * **低版本缩进时不允许使用Tab键，只允许使用空格**
* **使用`#`标识注释**，从`#`字符一直到行尾，都会被解释器忽略
* `---`为可选的分隔符，当需要在一个文件中定义多个同级的结构的时候使用

## 数据结构

字符串，整数，小数，布尔值，null等类型

### 字符串

**Plain Style**：除了特殊符号`& * { } [ ] : # !` 等，**其他直接使用**

```yaml
abcdef
foo: bar
```

等价json

```json
"abcdef"
{
  "foo": "bar"
}
```

**Quoted Style**：使用`''`或`""`，使用`\`可以连接多行内容

- 如果**直接换行则会用空格连接多行内容**

> 同一个`''`或`""`包裹

```yaml
"abcdef"
1: 'foo'
2: "bar\
    bar\
    bar"
3: "baz
    baz
    baz"
```

等价json

```json
"abcdef"
{
  "1": "foo", 
  "2": "barbarbar", 
  "3": "baz baz baz"
}
```

**Block Style**：使用`|`连接多行，保留末尾换行，或使用`>`，用空格连接多行

```json
literal: |
  some
  text
folded: >
  some
  text
quoted: "some\ntext\n"
```

等价json

```json
{
  "literal": "some\ntext\n", 
  "folded": "some text\n", 
  "quoted": "some\ntext\n"
}
```

**Trailing Empty Lines**

- `|`和`>`默认保留一个末尾换行
- `|+`和`>+`会保留所有末尾换行
- `|-`和`>-`会去除所有末尾换行

```yaml
1: |
   line 1

2: |+
   line 1



3: |-
   line 1


4: line 1
```

等价json

```json
{
  "1": "line 1\n", 
  "2": "line 1\n\n\n", 
  "3": "line 1", 
  "4": "line 1"
}
```

### 对象

键值对集合

- 映射（mapping）：`{ key: value }` 或 `key: value`
- 哈希（hashes）
- **字典**（dictionary）：用`:`标识
  - 普通字典
  - 多层嵌套字典：值也是字典

```yaml
1: { a: b, c: d }
2: {
 a: b,
 c: d, e: f
}
3:
  a: b
  c: d
```

等价json

```json
{
  "1": {
    "a": "b", 
    "c": "d"
  }, 
  "2": {
    "a": "b", 
    "c": "d", 
    "e": "f"
  }, 
  "3": {
    "a": "b", 
    "c": "d"
  }
}
```

### 数组

一组按次序排列的值，通常使用`-`标识

- 序列（sequence）
- **列表**（list）：`[]`或`-`

```yaml
1: [ a, b, c ]
2: [
  a, b,
  c,
]
3:
  - a
  - b
  - c
```

等价json

```json
{
  "1": ["a", "b", "c"], 
  "2": ["a", "b", "c"],
  "3": ["a", "b", "c"]
}
```

**Demo**

```yaml
volumes:
- name: kubernetes-dashboard-certs

# 解析为json
{"volumes":[{"name":"kubernetes-dashboard-certs"}]}
```

## 定义复用

使用`&`定义数据，使用`*`复用（引用）**已定义的数据**（必须在引用前定义）

```yaml
key_1: &def value_1
key_2: *def


jobs:
  job_a:
    steps:
      - &init_step
        name: Init Step
        commands: [ ls, pwd, whoami ]
  job_b:
    steps:
      - *init_step
      
      
1: &array_of_string
  type: array
  items:
    type: string
2:
  type: boolean
3: *array_of_string
```

等价json

```json
{
  "key_1": "value_1", 
  "key_2": "value_1"
}


{
  "jobs": {
    "job_a": {
      "steps": [
        {
          "commands": [
            "ls",
            "pwd",
            "whoami"
          ],
          "name": "Init Step"
        }
      ]
    }, 
    "job_b": {
      "steps": [
        {
          "commands": [
            "ls",
            "pwd",
            "whoami"
          ],
          "name": "Init Step"
        }
      ]
    }
  }
}


{
  "1": {
    "items": {
      "type": "string"
    },
    "type": "array"
  }, 
  "2": {
    "type": "boolean"
  }, 
  "3": {
    "items": {
      "type": "string"
    },
    "type": "array"
  }
}
```

### map合并

在复用定义的时候，可以使用`<<`将已定义的map展开和当前map合并，根据缩进，展开对应的map

> 就是在复用map的时候可以在后面追加新的内容

```yaml
1:
  a: b
2: &2
  c: d
<<: *2


1: &array_of_string
  type: array
  items:
    type: string
2:
  type: boolean
3:
  required: true
  <<: *array_of_string
```

等价json

```json
{
  "1": {
    "a": "b"
  }, 
  "2": {
    "c": "d"
  },
  "c": "d"
}

{
  "1": {
    "items": {
      "type": "string"
    },
    "type": "array"
  },
  "2": {
    "type": "boolean"
  }, 
  "3": {
    "required": true,
    "items": {
      "type": "string"
    },
    "type": "array"
  }
}
```

# Gitlab CI实践

[gitlab-ci官方文档翻译 (github.com)](https://github.com/Fennay/gitlab-ci-cn)

## 基本概念

### pipeline

Pipeline 即整个 CI 自动化流程的统称，一次 Pipeline 的运行称为 Pipeline run

- 在gitlab仓库里创建一个YAML文件（`.gitlab-ci.yml`），即可配置一个 Pipeline，它就是根据`.gitlab-ci.yml`文件执行的一个流程
- 一个 YAML 文件对应一个Pipeline的配置，**多个YAML文件可以对应多个不同的Pipeline配置**
- YAML文件中其中包含**事件触发**和**具体任务**的配置，即Trigger和Jobs，一个Pipeline会包含若干个 Job，即若干个任务节点（每一个任务节点都是一个独立的 Job）
  - 一个Pipleline有若干个`stage`，每个`stage`上有至少一个Job


### Job

Job可以视为**资源单位**，多个job互相是独立、分散的，都有独立的上下文（context）

- 一个 Pipeline 包含若干个 Job，**每一个 Job 各自会被分发到不同的机器上执行，默认并行**
- **每个Job都会配置一个stage属性**，来表示这个Job所处的阶段
- 一个 Job 包含若干个 Step

**注意**

- **Job 执行过程中产生的所有文件都会在 job 结束后丢失**，即运行下一个Job的时候，会默认把前一个Job**新增的资源删除**


```yaml
jobs:
  job_1:
    name: First Job
    image: debian
    steps:
      - commands: [ date ]
  job_2:
    name: Second Job
    image: python:3
    steps:
      - commands:
          - pwd
          - python3 -c "import datetime; print(datetime.datetime.now())"
```

### Step

- 一个Step包含若干命令（commands）或一个Action

- **一个 Job 中的Step都在同一个机器中，按配置顺序依次执行，共享同一份机器资源，共享同一个工作目录**
  - 环境不一样时（比如使用不同的镜像）并非所有目录均共享

### Action

- Action封装了一些可复用的命令操作，可以在Step中直接使用，以减少重复劳动

### Event / Trigger

Event / Trigger 用于配置**如何触发 Pipeline**

在仓库项目里配置好 Pipeline 后，**当事件和 Pipeline 配置中的 Trigger 相匹配时，会触发任务执行**

- **MR触发**：change
  - 使用branches参数限定MR的目标分支
  - 使用paths参数限定MR变更文件
- **Push触发**：push
  - 使用types参数限定push的动作类型，branch或tag
  - 使用branches参数限定push 分支
- **手动触发**
- 定时触发

### Runner

- Runner可以理解为：在特定机器上根据项目的`.gitlab-ci.yml`文件对项目执行pipeline的**程序**

- Runner可以分为两种： **Specific Runner** 和 **Shared Runner**

  - **Shared Runner**：Gitlab平台提供的免费使用的runner程序，由Google云平台提供支持，每个开发团队有十几个，对于公共开源项目是免费使用的，如果是私人项目则有每月2000分钟的CI时间上限

  - **Specific Runner**：用户自定义，在用户选择的机器上运行的runner程序
    - **Gitlab提供了一个`gitlab-runner`的命令行软件**，只要在对应机器上下载安装这个软件，然后运行`gitlab-runner register`命令，再输入从gitlab-ci交互界面获取的token进行注册，就可以在对应机器上远程运行pipeline程序了

#### 配置runner

[Install GitLab Runner | GitLab](https://docs.gitlab.com/runner/install/)

```bash
# 1. 下载runner，然后初始化
gitlab-runner install
gitlab-runner start

# 2. 注册runner，输入从setting中获取的Specific Runners的url和token，填写runner的tag
sudo gitlab-runner register

# 3. 激活
sudo gitlab-runner verify
sudo gitlab-runner restart
```

#### runner冲突

- 连续注册了多个Runner，这些Runner冲突了，或者是新注册的Runner和旧Runner使用了同一个token

```bash
# 1. 先删掉本地其他旧的Runner
sudo gitlab-runner unregister --all-runners

# 2.然后重置token，使用更新后的token重新注册一个Runner
```



## CI配置

gitlab提供了很多配置关键字，这些配置关键之不能被定义为`job`名称

- `stages`
- `stage`
- `script`
- `tags`
- `cache`
- `variables`

> `stage`，`script`，`tags`这三个关键字，都是**作为Job的子属性**来使用的

| 关键字        | 是否必须 | 描述                                 |
| :------------ | :------- | :----------------------------------- |
| image         | 否       | 用于docker镜像                       |
| services      | 否       | 用于docker服务                       |
| stages        | 否       | 定义构建阶段                         |
| before_script | 否       | 定义在每个job之前运行的命令          |
| after_script  | 否       | 定义在每个job之后运行的命令          |
| variable      | 否       | 定义构建变量                         |
| cache         | 否       | 定义一组文件列表，可在后续运行中使用 |

### stages

- 定义在yaml文件的最外层，是一个数组，**用于定义一个pipeline不同的流程节点**，会展示在Gitlab的交互界面中
- `stages`中的元素顺序决定了对应job的执行顺序

```yaml
stages: # 定义所有的stage
  - test
  - build
  - deploy
```

### stage

- 是一个字符串，是`stages`数组的一个子项，表示的是**当前的pipeline节点**

### script

- 是当前pipeline节点运行的**shell脚本**（以**项目根目录**为上下文执行）
  - 可以直接执行系统命令（`./configure`，`make`，`make install`）或者是直接执行脚本
- script是控制CI流程的核心，所有的工作，从安装，编译到部署都是通过script中定义的shell脚本来完成的
- 如果脚本执行成功，pipeline就会进入下一个Job，如果执行失败，pipeline就会终止

> 可以在当前job的script中手动触发另一个pipeline

### tags

- 是当前Job的标记，**gitlab-runner会通过tags去判断能否执行当前这个Job**
- 一个Runner只会执行tag和自己tag匹配的Job，如果一个Job没有tag或者tag不是自身的tag，那么即使这个Runner是激活且空闲的，也不会去执行

### cache

cache可以用来做pipeline中的资源共享

- **在不同pipeline之间重用资源**
- **在同一pipeline的不同Job之间重用资源**

**问题**

- Job执行过程中产生的所有文件都会在job结束后丢失，即运行下一个Job的时候，会默认把前一个Job**新增的资源删除**

**解决方案**

- 把`bulid`阶段生成的包的路径添加到`cache`里面，虽然gitlab还是会删除`bulid`包，但是因为在删除前已经重新上传到`cache`，所以就可以在下个Job运行时在cache把生成的包`pull`下来，实现在下一个Job里面使用前一个Job的资源

### variables

- 定义变量，并可以通过`${variables}`来使用

```yaml
variables:
  PROJECT: "model"
  VERSION: "1.0"
  REGISTRY: "gitlab.buaanlsde.cn:4567/buaapyj/registry"
  
  # 使用${REGISTRY}来代替gitlab.buaanlsde.cn:4567/buaapyj/registry
```

# CI with docker/k8s

[Use Docker to build Docker images | GitLab](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-the-docker-executor-with-the-docker-image-docker-in-docker)

[基于 GitLab CI/CD 实践 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/435567049)

使用CI创建一个新的pod，并部署到Kubernetes集群里面，出错可进行任意版本回退

> **可靠性**：应用会持续运行，不会被 pod 或 节点的故障所中断，如果出现故障，K8s也会创建必要数量的应用replicas，并分配到健康的节点上，直到系统恢复，用户无感知

`dind`：docker in docker

- 使用dind需注意，必须使用特权模式，即`privileged: true`

```yaml
stages:
  - install # 安装依赖，做缓存
  - build 	# build 镜像
  - test 		# 运行测试用例
  - deploy 	# 部署

services:
  - name: docker:18.09.7-dind
    alias: docker
    command: ["--registry-mirror=https://cbmiolsi.mirror.aliyuncs.com"]

variables:
  DOCKER_HOST: tcp://docker:2375
  DOCKER_DRIVER: overlay2
  FF_USE_FASTZIP: "true"
  CACHE_COMPRESSION_LEVEL: fastest

######################## 安装依赖并缓存 ###########################
# 仅当 package.json 变化时安装依赖
install_packages:
  stage: install   # 指定job属于哪个stage
  image: node:latest
  tags:						 # 指定runner
    - ci-example
  only:
    - test
    - tags
  services: []
  script:          # job执行的脚本or命令
    - cd ./services
    - npm install
 cache:
    key: "${CI_COMMIT_REF_NAME}_NPM_CACHE"
    untracked: true
    paths:
      - services/node_modules

#-------- build -------
build_test:
  stage: build
  tags:
    - ci-example
  only:
    - test
 cache:
    policy: pull
    key: "${CI_COMMIT_REF_NAME}_NPM_CACHE"
    untracked: true
    paths:
      - services/node_modules
  before_script:
    - docker login ...
  script:
    - docker build ...
    - docker push ...

#--------deploy -------
deploy_test:
  stage: deploy
  image: kubectl:v1.0.0
  services: []
  cache: {}
  tags:
    - ci-example
  only:
    - test
  # 可使用 kubectl,helm 等工具执行部署
  script:
    - kubectl ....
```

