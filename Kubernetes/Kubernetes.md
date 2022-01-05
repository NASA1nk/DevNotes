# kubernetes

kubernetes是一个**软件系统**，依赖于Linux容器的特性来**运行异构的应用**，它将底层基础设施抽象，简化应用的开发，部署和运维

**基础概念**

- Pod
  - 资源清单
  - Pod的生命周期
- 控制器类型
  - Pod 控制器的特点以及使用定义方式
- K8S网络通讯模式

- 服务发现
  - SVC原理及其构建方式

- 服务分类

  - 有状态服务：DBMS，数据持久化存储  

  - 无状态服务：LVS，APACHE


- 存储
  - 多种存储类型的特点
  - 不同环境中选择合适的存储方案
- 调度器
  - 调度器原理
  - 根据要求把Pod定义到特定的节点运行
- 安全
  - 集群的认证，鉴权，访问控制
- HELM
  - 类似Linux的yum，HELM 原理
  - HELM自定义模板
  - HELM部署一些常用插件
- 高可用集群
  - 副本数据最好是3个以上的（3，5，7，9）

 **特点**

- 开源
- 轻量级
- 弹性伸缩 
- 负载均衡

## 云计算架构

经典的云计算架构分为三大服务层

1. IaaS（Infrastructure as a Service）：**基础设施即服务**
1. IaaS层通过**虚拟化技术**提供计算、存储、网络等基础资源，可以在上面部署各种OS以及应用程序
   2. 开发者可以通过云厂商提供的API控制整个基础架构，无须对其进行**物理上的维护和管理**

2. PaaS（Platform as a Service）：**平台即服务**
   1. PaaS层提供软件部署平台（runtime），**抽象掉了硬件和操作系统**，可以无缝地扩展（scaling）
   2. 开发者只需要关注自己的业务逻辑，不需要关注底层

3. SaaS（Software as a Service）：**软件即服务**
   1. SaaS 层直接为开发者提供软件服务，将软件的开发、管理、部署等全部都交给第三方
   2. 用户不需要再关心技术问题，可以拿来即用  

# Kubernetes组件

![kubernetes架构](Kubernetes.assets/kubernetes架构.png)

### Kubernetes集群架构

- **Master**：集群控制节点，执行所有的命令，通常占据一个独立服务器
  - Api Server（kube-apiserver）：所有服务访问唯一入口，提供HttpRest接口的服务进程
  - CrontrollerManager（kube-controller-manager）：所有资源对象的自动化控制中心，维持副本期望数目
  - Scheduler（kube-scheduler）：负责接受任务并实现资源调度，选择合适的节点进行分配任务
  - Etcd：键值对数据库，采用http协议，储存K8S集群所有重要信息
    - 一个可信赖的分布式键值存储服务，能够为整个分布式集群存储一些关键数据，协助分布式集群的正常运转
      - 可信赖指天生支持集群化，不需要其他组件
      - 正常运转：保存分布式存储持久化的配置信息）
- **Node**：除了Master控制节点，Kubernetes集群中的其他工作负载节点
  - Kubelet：直接跟容器引擎交互实现容器的生命周期管理
  - Kube-proxy：负责写入规则至IpTables、Ipvs，从而实现服务映射访问，实现Kubernetes，Service的通信与负载均衡机制的重要组件
  - Docker Engine（docker）：Docker引擎，负责容器创建和管理工作。

### Pod分类

**生命周期**

- **自主式Pod**：Pod退出了，此类型的Pod不会被创建
  - 无法确保稳定性

- **控制器管理的Pod**：在控制器的生命周期里，始终要维持Pod的副本数目

**编程**

- **声明式编程（Deployment）**：侧重于定义想要什么，然后告诉计算机让它帮你实现
  - apply > create  

- **命令式编程（ReplicaSet）**：侧重于如何实现程序，把实现过程按逻辑一步步写出
  -  create > apply      


## 其他组件

- CoreDns：可以为集群中的SVC创建一个域名IP的对应关系解析
- DashBoard：给Kubernetes集群提供一个B/S结构访问体系
- **IngressController**：Ingress可以实现七层代理
  - 官方只能实现四层代理

- Federatiom：提供一个可以跨集群中心多Kubernetes统一管理功能
- **Prometheus**：提供Kubernetes集群的监控能力
- **Efk**：提供Kubernetes集群日志统一分析介入平台

# 部署Kubernetes集群

集群类型

- 单Master集群
- 多Master集群

先部署一套单Master架构（3台），再扩容为多Master架构（4台或6台）

**单Master服务器规划**

| **角色**   | **IP**        | **组件**                                                     |
| ---------- | ------------- | ------------------------------------------------------------ |
| k8s-master | 192.168.31.71 | kube-apiserver，kube-controller-manager，kube-scheduler，etcd |
| k8s-node1  | 192.168.31.72 | kubelet，kube-proxy，docker，etcd                            |
| k8s-node2  | 192.168.31.73 | kubelet，kube-proxy，docker，etcd                            |

**服务器要求**

- 2核CPU，2G内存，30G硬盘

- 集群中所有机器之间网络互通

- 可以访问外网，需要拉取镜像（NAT）

- 禁止swap分区

| **软件**   | **版本**               |
| ---------- | ---------------------- |
| 操作系统   | CentOS7.x_x64 （mini） |
| 容器引擎   | Docker CE 19           |
| Kubernetes | Kubernetes v1.20       |

**搭建方式**

- **kubeadm**：K8s 部署工具，快速部署Kubernetes集群
  - `kubeadm init`：创建Master节点
  - `kubeadm join`：将Node节点加入集群`kubeadm join <Master节点IP:端口>`
- **二进制**：手动部署每个组件，组成Kubernetes集群

> Kubeadm 降低部署门槛，但屏蔽了很多细节，遇到问题很难排查
>
> 使用二进制包部署Kubernetes 集群更容易可控，也利于后期维护

## 安装虚拟机

**新建虚拟机**

- 稍后安装OS
- 2个处理器，2个内核
- 2G内存
- 100G磁盘
- 磁盘存储为单个文件

**虚拟机设置**

- CD/DVD选择CentOS镜像
- 网络适配器选择NAT模式
- 安装位置默认
- 最小化安装
- 密码：空格

**地址分配**

| 节点         | IP             |
| ------------ | -------------- |
| k8s-master01 | 192.168.192.31 |
| k8s-node01   | 192.168.192.32 |
| k8s-node02   | 192.168.192.33 |

## 系统初始化

**查看NAT网关**

1. VMware-编辑-虚拟网络编辑器-更改设置
2. 选择NAT模式的网卡，点击NAT设置
3. 查看网关IP：192.168.192.2

![NAT](Kubernetes.assets/NAT.png)

```bash
# 设置IP地址
vi /etc/sysconfig/network-scripts/ifcfg-ens33
# 修改
BOOTPROTO=static
ONBOOT=yes
# 增加 
# 三个节点分别是31,32,33
IPADDR=192.168.192.31
NETMASK=255.255.255.0
GATEWAY=192.168.192.2

# 设置DNS
vi /etc/resolv.conf
# 增加
nameserver 192.168.192.2
# 重启
service network restart
# 验证
ping www.baidu.com

# 安装wget
yum install wget
```

![撰写栏](Kubernetes.assets/撰写栏.png)

同时写入三个节点

```bash
# 根据规划设置主机名
hostnamectl set-hostname <hostname>

# 添加hosts
cat >> /etc/hosts << EOF
192.168.192.31 k8s-master01
192.168.192.32 k8s-node01
192.168.192.33 k8s-node02
EOF

# 关闭防火墙
systemctl stop firewalld
systemctl disable firewalld

# 关闭selinux
sed -i 's/enforcing/disabled/' /etc/selinux/config  # 永久
setenforce 0  # 临时

# 关闭swap
swapoff -a  # 临时
sed -ri 's/.*swap.*/#&/' /etc/fstab    # 永久

# 重启

# 将桥接的IPv4流量传递到iptables的链
cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
# 生效
sysctl --system  

# 时间同步
yum install ntpdate -y
ntpdate time.windows.com

## 安装docker

Kubernetes 默认CRI（容器运行时）为Docker，因此先安装Docker

​```bash
# 下载Docker
wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo

# 安装指定版本
yum -y install docker-ce-18.06.1.ce-3.el7

# 设置开机启动
systemctl enable docker && systemctl start docker

# 验证
docker --version

# 设置仓库
cat > /etc/docker/daemon.json << EOF
{
"registry-mirrors": ["https://b9pmyelo.mirror.aliyuncs.com"]
}
EOF

# 重启docker
systemctl restart docker

# 验证
docker info

# 添加yum源
cat > /etc/yum.repos.d/kubernetes.repo << EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```

## 安装k8s组件

- kubeadm
- kubectl
- kubelet

```bash
# 指定版本
yum install -y kubelet-1.18.0 kubeadm-1.18.0 kubectl-1.18.0

# 设置开机启动
systemctl enable kubelet
```

## 部署Master节点

- apiserver-advertise-address：当前节点IP
- image-repository：阿里云镜像
- kubernetes-version：指定版本

> 默认拉取镜像地址k8s.gcr.io国内无法访问，指定阿里云镜像仓库地址

```bash
# 在Master节点上执行
kubeadm init \
--apiserver-advertise-address=192.168.192.31 \ 
--image-repository registry.aliyuncs.com/google_containers \ 
--kubernetes-version v1.18.0 \ 
--service-cidr=10.96.0.0/12 \
--pod-network-cidr=10.244.0.0/16
```

验证安装成功

- 提示成功信息**initialized successfully**
- 提示接下来步骤

![kubeadm init](Kubernetes.assets/kubeadm init.png)

查看下载的镜像

![master images](Kubernetes.assets/master images.png)

按提示操作

```bash
# 在master上运行
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# 查看节点,只有master节点,状态是NotReady
kubectl get nodes
```

## 添加Node节点

按提示操作

> 默认的token：`sha256:94a3812eff925d99fcc31b54febe76863bc0606da49fc09def8b97ea0e4b7227`有效期是24h，过期需要重新创建

```bash
# 在node上运行
kubeadm join 192.168.192.31:6443 --token 1f2a01.p9gda3tufqr2299x \
    --discovery-token-ca-cert-hash sha256:94a3812eff925d99fcc31b54febe76863bc0606da49fc09def8b97ea0e4b7227
    
# 查看节点,有master节点和node节点,状态都是NotReady
kubectl get nodes

# 重新创建token
kubeadm token create --print-join-command
```

## 部署CNI网络插件

节点状态NotReady：缺少网络组件

> 默认镜像地址无法访问，sed命令修改为docker hub镜像仓库。

```bash
# 下载网络插件配置
wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# 查看pods
kubectl get pods -n kube-system
```

状态变为Ready

![集群状态](Kubernetes.assets/集群状态.png)

[K8S应用FLANNEL失败解决INIT:IMAGEPULLBACKOFF](https://www.cnblogs.com/pyxuexi/p/14288591.html)

## 测试k8s集群

在Kubernetes集群中创建一个pod验证是否正常运行

在master节点上运行

```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl get pod,svc
```

访问：http://192.168.192.32:30561  

![验证](Kubernetes.assets/验证.png)



## Harbor

>  企业级 Docker 私有仓库

安装底层需求

- Python应该是应该是2.7或更高版本
- Docker引擎应为引擎应为1.10或更高版本
- Docker Compose需要为需要为1.6.0或更高版本

```bash
# 添加假证书
vim /etc/docker/daemon.json
# 中括号后加逗号，
"insecure-registries": ["[https://hub.atguigu.com](https://hub.atguigu.com/)"]

# 重启
systemctl restart docker
mv docker-compose /usr/local/bin
chmod a+x /usr/local/bin/docker-compose

# 解压
tar -zxvf harbor-offline-installer-v1.2.0.tgz
mv harbor /usr/local/
cd /usr/local/harbor
mkdir -p /data/cert

openssl genrsa -des3 -out server.key 2048
# 创建密码：123456

openssl req -new -key server.key -out server.csr
# 输入密码：123456
# 输入国家CN
# 输入城市BJ
# 默认城市BJ
# 组织atguigu

# 备份私钥
cp server.key server.key.org
# 退出密码
openssl rsa -in server.key.org -out server.key
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
mkdir  /data/cert
chmod -R 777 /data/cert
docker ps -a

# 访问hub.atguigu.com
# 登陆：admin
# 密码：Harbor12345
# 访问尝试
docker login https://hub.atguigu.com
# 下载镜像
docker pull wangyanglinux/myapp:v1
# 命令名称
# 规范：docker tag SOURCE_IMAGE[:TAG] hub.atguigu.com/library/IMAGE[:TAG]
# 把SOURCE_IMAGE[:TAG]和IMAGE[:TAG]替换掉
docker tag wangyanglinux/myapp:v1 hub.atguigu.com/library/myapp:v1
# 上传镜像到仓库
docker  push hub.atguigu.com/library/myapp:v1
# 链接私有仓库
kubectl run nginx-deployment --image=hub.atguigu.com/library/myapp:v1 --port=80 --replicas=1
# replicas标识副本数目，必须保持为1
# 删除
kubectl delete pod +名称
# 修改数目
kubectl scale --replicas=3 deployment/nginx-deployment
kubectl get deployment
kubectl get node -o wide

# 查看帮助文档
kubectl expose --help
# 访问模板
kubectl expose deployment nginx --port=80 --target-port=8000
# 访问服务的80端口，访问容器的8000端口（Create a service for an nginx deployment, which serves on port 80 and connects to the containers on port 8000）
# 修改虚拟ip为外网ip
kubectl edit svc nginx-deployment
# 将type里的ClusterIP改为NodePort
netstat -anpt | grep :30000
```



# YAML

Kubernetes集群中对**资源管理**和**资源对象编排部署**都可以通过YAML文件（声明样式文件）来解决

- 可以把需要对资源对象的操作编辑到YAML格式文件中，把这种文件叫做**资源清单文件**
- 通过kubectl命令直接使用资源清单文件就可以实现对大量的资源对象进行编排部署

**书写格式**

- YAML是一种**标记语言**，**以数据做为中心**，而不是以标记语言为重点
- YAML是一个可读性高，用来表达数据序列的格式

**基本语法**

* 使用**空格做为缩进**
  * 缩进的空格数目不重要，只要相同层级的元素左侧**对齐即可**
  * 低版本**缩进时不允许使用Tab键**，只允许使用空格

* **使用`#`标识注释**
  * 从`#`字符一直到行尾，都会被解释器忽略

**数据结构**

- **对象**：键值对集合

  - 映射（mapping）

  - 哈希（hashes）

  - 字典（dictionary）


- **数组**：一组按次序排列的值

  - 序列（sequence）

  - 列表（list）


# kubectl

`kubectl command type name flags`

- comand：指定**对资源执行的操作**
  - `create`，`get`，`describe`和`delete`

- type：指定**资源类型**
  - 大小写敏感，可以是单数、复数和缩略的形式
  - `pod`，`pods`和`po`

- name：**指定资源的名称**
  - 大小写敏感，省略名称会显示所有的资源

- flags：**指定可选的参数**
  - 用`-s`或者`–server`参数指定API server 的地址和端口




# Kuboard

**在Kuboard中集群概览的展示形式**

- 上层：运行于计算资源与存储资源上的名称空间（应用）

- 下层：计算资源、存储资源并列




**在Kuboard中名称空间的展示形式：以微服务参考分层架构的形式，将所有的微服务分为如下几层：**

- 展现层：终端用户访问的 Web 应用
- API网关层：Spring Cloud Gateway / Zuul /Kong 等接口网关
- 微服务层：Spring Boot 微服务，或 PHP / Python 实现的微服务
- 持久层：MySQL 数据库等（开发及测试环境里将MySQL部署于K8s可以极大地降低环境维护的任务量）
- 中间件层
  - 消息队列
  - 服务注册 Eureka / Zookeeper / Consul
- 监控层
  - Prometheus + Grafana
  - Pinpooint

# Rancher

- Rancher的集群管理基于角色的访问控制策略，策略管理和工作负载等功能在导入集群中可用
- 对于除K3s集群外的所有导入的 Kubernetes 集群，必须在Rancher外部编辑集群的配置，需要自己在集群中修改Kubernetes组件的参数、升级Kubernetes版本以及添加或删除节点
- Rancher中不能配置或扩展导入的集群

## 搭建Rancher环境

> ERROR: Rancher must be ran with the --privileged flag when running outside of Kubernetes

在浏览器中访问：https://192.168.192.31，首次访问会提示设置admin管理员密码

```bash
sudo docker run --privileged -d  --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher:stable
```



