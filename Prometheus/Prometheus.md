# Prometheus

Prometheus是一个开源的监控解决方案

## Prometheus架构

Prometheus生态圈由多个组件构成，其中许多组件是可选的

- **Prometheus Server**
  
  - 用于收集、存储和查询时间序列数据
  - 通过**静态配置文件**（`prometheus.yml`）管理监控目标，也可以配合使用**动态服务发现**的方式动态管理监控目标，并从这些监控目标中获取数据，然后将采集到的数据**按照时间序列的方式存储**在本地磁盘当中或者外部的时序数据库中，可通过**PromQL语言**对数据的查询以及分析
  
- **Client Library**
  
  为被监控的应用**生成相应的指标**（Metric）数据并暴露给Prometheus Server，当Prometheus Server来拉取时直接返回**实时状态**的指标数据
  
- **Push Gateway**
  
  - 相当于一个代理服务，**独立部署**。它没有数据拉取功能，**只能被动的等待数据推送**
  - 主要用于短期存在的Jobs，这类Jobs由于存在时间较短，可能在Prometheus Server来拉取数据之前就消失了。所以这些Jobs可以直**接向Push Gateway推送它们的指标数据**，等到这些jobs把数据推送到Push Gateway后，P**rometheus Server再从Push Gateway拉取**
  - 当由于子网络或者防火墙的原因，Prometheus Server不能直接拉取各个目标（target）的指标数据，此时可以让各个目标（target）往Push Gateway上推送数据，然后Prometheus Server去PushGateway上定时拉取
  - 在监控各个业务数据时，需要**将各个不同的业务数据进行统一汇总**，此时也可以采用Push Gateway来统一收集数据，然后Prometheus Server在来统一拉取
  
  > 即使jobs推送了所有的数据到Push Gateway，Prometheus Server也不是每次都拉取这个期间推上来的所有数据，而是**只拉取jobs最后一次推送的数据**。如果jobs一直没有推送新的指标（Metric）到Push Gateway，那么Prometheus Server将始终拉取最后推送上的数据，直到指标消失（默认5分钟）
  
- **Exporters**
  
  输出被监控组件信息的HTTP接口被叫做`exporter`
  
  - 用于暴露已有的第三方服务的指标（Metric）数据**通过HTTP服务的形式**暴露给Prometheus Server，比如HAProxy、StatsD、Graphite等
    Prometheus Server周期性的从Exporter暴露的HTTP服务地址（通常是/metrics）拉取监控样本数据
  
- **Alertmanager**
  
  - 从Prometheus Server接收到告警后，Alertmanager会进行去除重复数据，分组，并路由到接收方，发出报警。
  - AlertManager支持自定义告警规则。告警方式也非常灵活，支持通过邮件、slack或钉钉等多种途径发出告警。

![Prometheus架构图](Prometheus.assets/Prometheus架构图.jpg)

## Prometheus工作流程

1. Prometheus Server从HTTP接口或者从Push Gateway拉取指标（Metric）数据
2. Prometheus Server在本地存储所有采集的指标（Metric）数据，并在这些数据上运行规则，从现有数据中聚合和记录新的时间序列生成告警
3. Alertmanager根据配置文件，对接收到的告警进行处理，发出报警
4. 在Grafana或其他API客户端中，可视化收集的数据

> Prometheus其实并不需要每一个精确的数据，长期保存的是中等或者低精度的数据。它每次只抓取一个数据，在固定的频率下。也能形成某种数据的趋势。



## Prometheus数据模型

Prometheus会将所有采集到的监控数据以**时间序列**的方式保存在内存数据库中并定时保存到硬盘上

**数据组成**

- **指标**（Metric）：由**指标名称**和描述当前**数据特征的标签**组成
- **时间戳**（Timestamp）：一个精确到毫秒的时间戳
- **数据值**（Value）：一个float64的浮点型数据表示当前数据的值

Prometheus是一个**时序数据库**，**相同指标相同标签的数据构成一条时间序列**

如果以传统数据库的概念来理解时序数据库

- 指标名是表名
- 标签是字段
- Timestamp是主键
- float64类型的字段表示值（

> Prometheus 里面所有值都是按 float64 存储

**指标（Metric）**

- **指标格式**

  `指标名称{标签名称="标签值"}`

  - 标签（Label）：反映了当前数据的特征维度，Prometheus通过这些维度可以对数据进行过滤，聚合等操作


例

`promhttp_metric_handler_requests_total{code="200",instance="192.168.0.107:9090",job="prometheus"} 106`

- 指标名称：`promhttp_metric_handler_requests_total`
- 标签：
  - code
  - instance
  - job
- 值：106

- **指标类型**

  Prometheus定义了4种不同的指标类型（Metric Type）

  - **Counter**（计数器）
  - **Gauge**（仪表盘）
  - **Histogram**（直方图）
  - **Summary**（摘要）

**Counter**

- Counter类型和计数器一样，只增不减（除非系统发生重置）

- 一般在定义Counter类型指标的名称时推荐使用`_total`作为后缀。比如Prometheus Server中`prometheus_http_requests_total`表示Prometheus处理的HTTP请求总数


```text
# HELP prometheus_http_requests_total Counter of HTTP requests.
# TYPE prometheus_http_requests_total counter
prometheus_http_requests_total{code="200",handler="/api/v1/label/:name/values"} 3
prometheus_http_requests_total{code="200",handler="/api/v1/query"} 5
prometheus_http_requests_total{code="200",handler="/api/v1/query_range"} 15
prometheus_http_requests_total{code="200",handler="/graph"} 3
prometheus_http_requests_total{code="200",handler="/metrics"} 23
```

**Gauge**

- Gauge类型侧重于反应系统的某一个**瞬时的值**，可增可减

- 比如Prometheus Server中`go_threads`表示Prometheus当前go线程的数量


```text
# HELP go_threads Number of OS threads created.
# TYPE go_threads gauge
go_threads 13
```

**Histogram**

- 主要用于表示**一段时间范围内**对数据进行采样的结果，并能够对其指定区间以及总数进行统计（通常展示为直方图）
- Histogram类型由`_bucket{le=""}`，`_bucket{le="+Inf"}`, `_sum`，`_count`组成
- 比如Prometheus Server中`prometheus_http_response_size_bytes`


```text
# HELP prometheus_http_response_size_bytes Histogram of response size for HTTP requests.
# TYPE prometheus_http_response_size_bytes histogram
prometheus_http_response_size_bytes_bucket{handler="/",le="100"} 1
prometheus_http_response_size_bytes_bucket{handler="/",le="1000"} 1
prometheus_http_response_size_bytes_bucket{handler="/",le="1e+06"} 1
prometheus_http_response_size_bytes_bucket{handler="/",le="+Inf"} 1
prometheus_http_response_size_bytes_sum{handler="/"} 29
prometheus_http_response_size_bytes_count{handler="/"} 1
```

**Summary**

- 主要用于表示**一段时间内**数据采样结果，它直接存储了**分位数据**而不是根据统计区间计算出来
- Summary类型由 `{quantile="<φ>"}`，`_sum`，`_count` 组成

- 比如Prometheus Server中`prometheus_target_interval_length_seconds`


```text
# HELP prometheus_target_interval_length_seconds Actual intervals between scrapes.
# TYPE prometheus_target_interval_length_seconds summary
prometheus_target_interval_length_seconds{interval="15s",quantile="0.01"} 14.9986249
prometheus_target_interval_length_seconds{interval="15s",quantile="0.05"} 14.998999
prometheus_target_interval_length_seconds{interval="15s",quantile="0.5"} 15.0000428
prometheus_target_interval_length_seconds_sum{interval="15s"} 315.0013755
prometheus_target_interval_length_seconds_count{interval="15s"} 21
```



## Prometheus数据获取

Prometheus主要是通过**拉取**（pull）的方式获取数据

Prometheus每隔一段时间会从配置的**目标（target）**（获取数据的url）以Http协议拉取**指标（metrics）**，这些目标（target）可以是应用，也可以是代理，缓存中间件，数据库等等一些中间件

> 需要服务端提供http的接口来获取实时的数据

Prometheus会将拉取出来的数据存到**自己的TSDB时序数据库**

Prometheus的WebUI控制台以及Grafana可以对数据进行时间范围内的不断查询，绘制成实时图表工展现

Prometheus支持例如zookeeper，consul之类的服务发现中间件，用以对目标（target）的自动发现。而不用一个个去配置

## Prometheus配置文件

Prometheus 默认的配置文件分为四部分

- global：Prometheus 的全局配置
  -  `scrape_interval` 表示多久抓取一次数据
  - `evaluation_interval` 表示多久检测一次告警规则
- alerting：关于Alertmanager的配置
- rule_files：告警规则
- scrape_config：定义了 Prometheus 要抓取的目标
  - 默认已经配置了一个名称为 `prometheus` 的 job，这是Prometheus在启动的时候也会通过HTTP接口暴露自身的指标数据（相当于 Prometheus自己监控自己）可以访问 http://localhost:9090/metrics查看 Prometheus暴露的指标



## 部署Prometheus Server

访问Web管理页面( http://10.2.14.105:9090 )可以看到Prometheus服务正确启动

```bash
# 拉取镜像
docker pull prom/prometheus

# 下载prometheus的配置文件并将其存放在/home/dog/yinke/prometheus/config路径下 https://github.com/prometheus/prometheus/blob/master/documentation/examples/prometheus.yml

# 启动容器
# -v: 挂载到容器内的/etc/prometheus/prometheus.yml
docker run --name inkPrometheus \
-d -p 9090:9090 \
-v /home/dog/yinke/prometheus/config/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus
```



# Exporters

Prometheus服务负责收集、存储、查看监控数据，真正**直接进行监控通过Exporters完成**

Exporters相当于是Prometheus服务的客户端，**负责向其提供监控数据**，针对不同的被监控目标需要使用不同的Exporter

Exporters的实例称为目标（Target），Prometheus通过轮询的方式定时从这些目标（Target）中获取监控数据样本，并且存储在数据库中

[Exporters | Prometheus](https://prometheus.io/docs/instrumenting/exporters/)

> i386是32位的版本，amd64是64位的版本
>
> - i386=Intel 80386，i386通常被用来作为对Intel（英特尔）32位微处理器的统称
>
> - AMD64又称x86-64或x64”，是一种64位元的电脑处理器架构。它是建基于现有32位元的x86架构，由AMD公司所开发

**直接部署**

> **配置报错**
>
> level=info ts=2020-07-18T04:38:46.494Z caller=tls_config.go:170 msg="TLS is disabled and it cannot be enabled on the fly." http2=false
>
> **原因**
>
> node_exporter版本升到1.0.0之后，因为安全性考虑支持了TLS，所以要添加证书

通过 http://49.232.207.245:9100/metrics 可以看到采集的监控数据

```bash
# 下载 node exporter(64bit)
wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz
wget https://github.com/prometheus/node_exporter/releases/download/v0.16.0/node_exporter-0.16.0.linux-amd64.tar.gz

# 解压
tar xvfz node_exporter-1.1.2.linux-amd64.tar.gz

# 移动到exporter 目录下
mkdir exporter
mv node_exporter-1.1.2.linux-amd64/* exporter

# 进入目录
# 将node_exporter和node_exporter.crt和node_exporter.key放在同一个目录
cd exporter

# 生成证书
# 得到node_exporter.crt和node_exporter.key两个文件
openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -keyout node_exporter.key -out node_exporter.crt -subj "/C=CN/ST=Beijing/L=Beijing/O=test.cn/CN=localhost"

# 编写配置文件
vim config.yaml

# 复制进去
tls_server_config:
  cert_file: node_exporter.crt
  key_file: node_exporter.key

# 查看node_exporter是否正常
./node_exporter --version

# 使用配置文件启动
./node_exporter --web.config=config.yaml
```



**docker部署**

[Monitoring Linux host metrics with the Node Exporter](https://prometheus.io/docs/guides/node-exporter/)

[Prometheus Exporter for machine metrics ](https://github.com/prometheus/node_exporter#using-docker)

官方不建议将node_exporter部署为Docker容器，因为它需要访问主机系统。

如果要部署Docker以进行主机监控，必须使用一些额外的参数来允许node_exporter访问主机名称空间。

`path.rootfs`参数，此参数必须与`host root`的`bind-mount`中的路径匹配。node_exporter将`path.rootfs`用作**访问主机文件系统的前缀**

> 要监视的所有非root挂载点都需要绑定挂载到容器中

```bash
docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter \
  --path.rootfs /host
  
# 查看
curl http://localhost:9100/metrics
curl http://localhost:9100/metrics | grep "node_"
```

**配置**

在Prometheus服务的配置文件`prometheus.yml`中添加相应的配置来收集Node Exporter的监控数据

1. 在`scrape_configs`下添加一个新的job
2. **重启prometheus服务**然后进入Web管理页面 http://10.2.14.105:9090
3. 输入`up`，点击Execute按钮，可看到刚刚添加的job（1表示正常，0表示异常）

```yaml
...
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  # 收集主机的监控数据  
  - job_name: 'exporter'
  	# 每隔5秒钟从http://IP:Port/actuator/prometheus拉取指标
  	scrape_interval: 5s
  	# scheme: https
    # tls_config:
    #   ca_file: node_exporter.crt
    # metrics_path: '/actuator/prometheus'
    static_configs:
    # 多个node_exporter，在targets数组后面加即可
    - targets: ['10.2.14.105:9100']
```





# 数据查询

进入http://10.2.14.105:9090

- Alerts：展示了定义的所有告警规则
- Status：可以查看各种Prometheus的状态信息
- Graph：可以使用PromQL查询数据，还可以通过 Prometheus 提供的 HTTP API 来查询数据
  - 查询的监控数据有列表和曲线图两种展现形式（对应上图中 Console 和 Graph 这两个标签）

![9090](Prometheus.assets/9090.png)



**查询**

`promhttp_metric_handler_requests_total`：表示 `/metrics` 页面的访问次数

![查询结果](Prometheus.assets/查询结果.png)

![查询图表](Prometheus.assets/查询图表.png)



## PromQL 

Prometheus Query Language



## HTTP API

Prometheus还提供了一种**HTTP API**的方式，可以更灵活的将 PromQL 整合到其他系统中使用，实际上Prometheus 的Graph页面查询也是使用了 HTTP API

[HTTP API | Prometheus](https://prometheus.io/docs/prometheus/latest/querying/api/)

> Grafana就是通过 Prometheus 的 HTTP API 来查询指标数据的

- GET /api/v1/query
- GET /api/v1/query_range
- GET /api/v1/series
- GET /api/v1/label/<label_name>/values
- GET /api/v1/targets
- GET /api/v1/rules
- GET /api/v1/alerts
- GET /api/v1/targets/metadata
- GET /api/v1/alertmanagers
- GET /api/v1/status/config
- GET /api/v1/status/flags
- POST /api/v1/admin/tsdb/snapshot
- POST /api/v1/admin/tsdb/delete_series
- POST /api/v1/admin/tsdb/clean_tombstones

# Grafana

Grafana是一个开源的跨平台的度量分析、可视化工具

## Grafana配置

访问http://10.2.14.105/:3000进入Grafana的Web页面

默认账号密码均为admin，进入后修改密码（123456）

```bash
# 拉取镜像
docker pull grafana/grafana

# 启动容器
docker run --name iGrafana \
-d -p 3000:3000 \
grafana/grafana
```



## 添加数据源

1. 设置`Configuration`
2. 选择`Data Sources`
3. 点击`Add data source`，
4. 选择`Time series databases`时序数据库中的`Prometheus`
5. 填写数据源名称和URL地址http://49.232.207.245:9090并保存

![Grafana连接Prometheus](Prometheus.assets/Grafana连接Prometheus.png)



## 仪表盘配置

在Grafana中可以自定义各种监控所需的仪表盘

> 完全自己搭建较麻烦，可在现有模板的基础上根据需要进行微调

进入Grafana官网( [https://grafana.com](https://link.zhihu.com/?target=https%3A//grafana.com) )，选择仪表盘

![Grafana仪表盘](Prometheus.assets/Grafana仪表盘.png)

过滤出适用Node Exporter类型的相关模板

- 选择中文版本
- 复制该**模板ID-8919**（9276）

![过滤仪表盘](Prometheus.assets/过滤仪表盘.png)

回到Grafana的Web管理页面

- 点加号选择import导入模板，输入模板ID
- 点击loda，在VictoriaMetrics中选择Prometheus，点击import

![导入模板](Prometheus.assets/导入模板.png)





# MySQL监控

[mysqld_exporter](https://github.com/prometheus/mysqld_exporter)是Prometheus官方提供的一个exporter

访问http://49.232.207.245:9104/metrics可查看MySQLD Exporter采集的MySQL监控数据

```bash
# 拉取镜像
docker pull prom/mysqld-exporter

# 启动容器
docker run -d --name mysqldExporter \
-p 9104:9104 \
-e DATA_SOURCE_NAME="root:123456@(49.232.207.245:3306)/"  \
prom/mysqld-exporter
```

![监控MySQLD](Prometheus.assets/监控MySQLD.png)

在Prometheus服务的配置文件`prometheus.yml`中添加job

重启Prometheus服务

```yaml
vim prometheus.yml

...
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  # 收集MySQL的监控数据      
  - job_name: 'MySQL'
    static_configs:
    - targets: ['49.232.207.245:9104']
```

![监控MySQLD-Target](Prometheus.assets/监控MySQLD-Target.png)

进入Grafana官网( [https://grafana.com](https://link.zhihu.com/?target=https%3A//grafana.com) )，选择适用于监控MySQL的模板选择仪表盘

过滤条件：

- Name/Description：mysql 
- Data Source：Prometheus

复制**模板ID—12826**

导入

![MySQL仪表盘](Prometheus.assets/MySQL仪表盘.png)



# CAdvisor配置

cAdvisor是Google一款开源的用于分析、展示容器运行状态的可视化工具，用于监控Dcoker整体的运行情况

> cAdvisor原生支持Prometheus

```bash
# 拉取镜像
docker pull google/cadvisor

# 启动容器
docker run --name=mycAdvisor \
  -p 8081:8080 -d \
  -v /:/rootfs:ro \
  -v /var/run:/var/run:ro \
  -v /sys:/sys:ro \
  -v /var/lib/docker/:/var/lib/docker:ro \
  -v /dev/disk/:/dev/disk:ro \
  --privileged \
  --device=/dev/kmsg \
  google/cadvisor
```

在`prometheus.yml`配置文件中添加job

重启Prometheus服务

```yaml
...
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  # 收集Docker容器的监控数据
  - job_name: 'cAdvisor'
    static_configs:
    - targets: ['10.2.14.105:8081']
```

访问 http://10.2.14.105:8081 查看监控页面（Docker中整体及各容器的监控指标）

![cAdvisor](Prometheus.assets/cAdvisor.png)

![Usage per Core](Prometheus.assets/Usage per Core.png)

![Throughput](Prometheus.assets/Throughput.png)

访问http://10.2.14.105:8081/metrics 查看到采集的监控数据

![cAdvisormetrics](Prometheus.assets/cAdvisormetrics.png)

进入Grafana官网( [https://grafana.com](https://link.zhihu.com/?target=https%3A//grafana.com) )，选择适用于cAdvisor的模板

过滤条件：

- Name/Description=cAdvisor
- Data Source=Prometheus

复制**模板ID—893**

导入

![cAdvisior](Prometheus.assets/cAdvisior.png)



# AlterManager

Pormetheus的告警由独立的两部分组成

- Prometheus服务中的告警规则发送告警到Alertmanager。
- Alertmanager管理这些告警，包括silencing, inhibition, aggregation，并通过邮件发送通知

建立警告和通知的主要步骤：

1. 创建和配置Alertmanager
2. 启动Prometheus服务时，通过-alertmanager.url标志配置Alermanager地址，以便Prometheus服务能和Alertmanager建立连接。
3. 在Prometheus中配置告警规则

## SMTP

在报警邮箱中开通smtp功能，并获取授权码（smtp_auth_password中填写）

> pttg hhoz jymp bcjf

![报警邮箱设置](Prometheus.assets/报警邮箱设置.png)

>  smtp.qq.com:465 ，端口使用465。其他资料说用587端口也可以（如果是云服务器，25端口通常是被服务商封闭的，所有也不能使用25端口）
>
>  报错信息：
>
> msg="Notify for alerts failed" num_alerts=1 err="*notify.loginAuth failed: 530 Must issue a STARTTLS command first."
>
> 3.smtp_require_tls: false 必须加上，因为smtp_require_tls默认为true。



## rule_files

在`/home/dog/yinke/prometheus/config`目录下创建告警规则文件`alertrules.yml`

这个规则文件里包含了两条告警规则：

- `InstanceDown`：表示当实例宕机时（up == 0）触发告警
-  `APIHighRequestLatency`：表示有一半的API请求延迟大于1s时（api_http_request_latencies_second{quantile="0.5"} > 1）触发告警

```bash
groups:
- name: node_rules
  rules:
  # Alert for any instance that is unreachable for > 5 minutes.
  - alert: InstanceDown
    # 0不正常，1正常
    expr: up == 0
    # 持续5分钟获取不到信息，触发报警
    for: 5m
    labels:
      # 告警紧急程度
      severity: error
    # 说明内容
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 5 minutes."
 
  # Alert for any instance that has a median request latency >1s.
  - alert: APIHighRequestLatency
    expr: api_http_request_latencies_second{quantile="0.5"} > 1
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "High request latency on {{ $labels.instance }}"
      description: "{{ $labels.instance }} has a median request latency above 1s (current value: {{ $value }}s)"
  - alert: HighMemoryUsage
    expr: node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.5
    for: 1m
    labels:
      severity: warning
    annotations:
      summary: High memory usage
```

因为Prometheus是docker部署的，因此`alertrules.yml`位置必须是**容器内部的目录位置**，而不是宿主机上目录

将`/home/dog/yinke/prometheus/config/alertrules.yml`拷贝到容器内`/etc/prometheus/`

```bash
# 拷贝
docker cp /home/dog/yinke/prometheus/config/alertrules.yml e87a0a440925:/etc/prometheus/
# 进入查看是否拷贝成功
docker exec -it e87a0a440925 /bin/sh
cd /etc/prometheus/
```

在`Prometheus.yml`的`rule_files`块中添加告警规则文件`alert.rules`

```bash
# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).
 
# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093
 
# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  - "alert.rules"
```

重启Prometheus Server服务

访问 http://10.2.14.105:9090/rules 查看配置规则

![rulefiles](Prometheus.assets/rulefiles.png)

访问 http://10.2.14.105:9090/alerts 可以看到根据配置的规则生成的告警

![rulealerts](Prometheus.assets/rulealerts.png)

停掉两个实例node-exporter和cAdvisor

```bash
docker stop 5ce59207a273
docker stop 82a19860304a
```

![stop两个实例](Prometheus.assets/stop两个实例.png)

可以看到有2条alert的状态是 **PENDING**，表示已经触发了告警规则，但还没有达到告警条件。这是因为这里配置的 `for` 参数是 5m，所以5分钟后才会触发告警

![开始down提示](Prometheus.assets/开始down提示.png)

5分钟后可以看到这2条alert的状态变成了 `FIRING`

![firing](Prometheus.assets/firing.png)



## 部署AlterManager

**直接部署**

在`/home/dog/yinke/prometheus`下创建 `alertmanager`目录，进入

```bash
wget https://github.com/prometheus/alertmanager/releases/download/v0.15.2/alertmanager-0.15.2.linux-amd64.tar.gz

tar xvfz alertmanager-0.15.2.linux-amd64.tar.gz

cd alertmanager-0.15.2.linux-amd64

./alertmanager
```



**docker部署**

在`/home/dog/yinke/prometheus/alertmanager`目录下创建配置文件`alertmanager.yml`

```yaml
global:
  resolve_timeout: 5m
  # 发件服务器,可设置qq企业,163邮箱等
  smtp_smarthost: 'smtp.139.com:465'   
  smtp_from: '541640794@qq.com'
  smtp_auth_username: '541640794@qq.com'
  smtp_auth_password: 'XX自己的密码XXX'
————————————————
版权声明：本文为CSDN博主「ghostwritten」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xixihahalelehehe/article/details/80391733
route:
  group_by: ['cqh']
  group_wait: 10s #组报警等待时间
  group_interval: 10s #组报警间隔时间
  repeat_interval: 1m #重复报警间隔时间
  receiver: 'email'
receivers:
  - name: 'email'
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'dev', 'instance']
    
global:
resolve_timeout: 5m
smtp_smarthost: 'smtp.qq.com:465'
smtp_from: '541640794@qq.com'
smtp_auth_username: 'xxxxxx@qq.com'
smtp_auth_password: 'xxxxxxxxxx'
smtp_require_tls: false
```





## 告警通知







## Grafana配置邮箱

**安装邮件发送服务** 

```bash
sudo apt-get install sendmail
sudo apt-get install sendmail-cf
```

**添加邮件配置**

进入grafana容器中，默认的配置文件在`/etc/grafana/`目录下

修改`grafana.ini`文件的smtp部分

> `.ini`文件中分号`;`是表示注释该行，更改设置必须先删除设置前面的分号`;`才能起作用

```bash
docker exec -it ContainerID /bin/bash

vim /etc/grafana/grafana.ini 

[admin@prometheus ~]$ sudo vim /etc/grafana/grafana.ini
...
enabled = true                                          #默认是false
host = smtp.mxhichina.com:465                           #smtp服务器的地址和端口，阿里云的企业邮箱。465加密端口    25非加密端口
user = 541640794@qq.com                                     #登录邮箱的账号
password =                                       #你邮箱账号的密码
from_address = 541640794@qq.com                             #发邮件的账号
from_name = Grafana                                     #自定义的名字
ehlo_identity = example.com                   #无关紧要的一个标示
...

# 重启grafana服务
sudo service grafana-server restart  
```

##### 通过配置Grafana的环境变量修改

grafana的配置选项也可以使用环境变量指定覆盖配置文件中的**所有选项**

`SectionName`是`.ini`文件中**方括号中的文本**，字母大写，`.`用`_`代替

```bash
GF_<SectionName>_<KeyName>
```

![SectionName](Prometheus.assets/SectionName.png)







- 