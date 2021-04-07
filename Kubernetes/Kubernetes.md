# kubernetes

kubernetes是一个软件系统，依赖于Linux容器的特性来运行异构的应用，它将底层基础设施抽象，简化应用的开发，部署和运维。

# kubernetes集群架构

- 主节点（控制面版）
  - kubernetesAPI服务器
  - Scheculer
  - Controller Manager
  - etcd
- 工作节点
  - 容器（docker，rtk）
  - kubelet
  - kube-proxy