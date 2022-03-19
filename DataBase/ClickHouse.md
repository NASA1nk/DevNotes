# ClickHouse

ClickHouse 是 Yandex（俄罗斯最大的搜索引擎）开源的一个**用于实时数据分析的基于列存储的数据库**，是一个主要用于数据分析（OLAP）领域的列式数据库管理系统(columnar DBMS)

- 列存储
- 实时数据分析
  
> ClickHouse处理数据的速度比传统方法快100-1000倍
> 
> ClickHouse 的性能超过了目前市场上可比的面向列的DBMS，每秒钟每台服务器每秒处理数亿至十亿多行和数十千兆字节的数据

## 特性

- 快速：ClickHouse会充分利用所有可用的硬件，以尽可能快地处理每个查询
  - 单个查询的峰值处理性能超过每秒2TB（解压缩后，仅使用的列）
  - 在分布式设置中，读取是在健康副本之间自动平衡的，以避免增加延迟
- 容错：ClickHouse支持多主机异步复制，并且可以跨多个数据中心进行部署
  - 所有节点都相等，这可以避免出现单点故障，单个节点或整个数据中心的停机时间不会影响系统的读写可用性
- 可伸缩：ClickHouse可以在垂直和水平方向上很好地缩放
  - ClickHouse易于调整以在具有数百或数千个节点的群集上或在单个服务器上，甚至在小型虚拟机上执行
  - 当前每个单节点安装的数据量超过数万亿行或数百兆兆字节
- 易用：ClickHouse简单易用，开箱即用
  - 简化了所有数据处理：将所有结构化数据吸收到系统中，并且立即可用于构建报告
  - SQL允许表达期望的结果，而无需涉及某些DBMS中可以找到的任何自定义非标准API
- 充分利用硬件：ClickHouse与具有相同的可用I/O吞吐量和CPU容量的传统的面向行的系统相比，其处理典型的分析查询要快两到三个数量级
  - 列式存储格式允许在RAM中容纳更多热数据，从而缩短了响应时间
- 提高CPU效率：向量化查询执行涉及相关的SIMD处理器指令和运行时代码生成，处理列中的数据会提高CPU行缓存的命中率
- 优化磁盘访问：ClickHouse可以最大程度地减少范围查询的次数，从而提高了使用旋转磁盘驱动器的效率，因为它可以保持连续存储数据
- 最小化数据传输：ClickHouse使公司无需使用专门针对高性能计算的专用网络即可管理其数据

## OLAP

数据处理大致可以分成两大类

- 联机事务处理OLTP（on-line transaction processing）
- 联机分析处理OLAP（On-Line Analytical Processing）

> OLTP是传统的关系型数据库的主要应用，主要是基本的、日常的事务处理，例如银行交易

**联机分析处理**（On-Line Analytical Processing）
- 数据仓库系统的主要应用，支持复杂的分析操作，侧重决策支持，并且提供直观易懂的查询结果。

**应用场景**
- 绝大多数操作是读、极少更新甚至无需更新
- 读取大量行的数据，但是一次查询往往只关注少量列
- 无需事务的支持、数据一致性要求低，追求极致的速度
- 统计分析场景、多维度聚合查询


## 存储
### 列式存储

列式数据库将每一列的数据连续存储，组织磁盘或内存中给定的连续列数据

- 基于列的存储方式，有助于减少**联机分析处理 (OLAP)** 的负载
  - 因为查询会涉及到列的一个子集，这些列有大量的行数，对于这类查询，使用列数据格式可以大大减少从磁盘到内存和从内存到寄存器的数据转换，可以有效地提高整个存储体系的吞吐量
- 列式存储可以使用一些基于每列的轻量级压缩算法，节省了空间，提升了IO性能

> 常见的列式存储有：Vertical、HBase等

**优点**
- 查询时只需读取涉及的列
- 任何列都可以做索引

相比于行式存储，列式存储在分析场景下有着许多优良的特性

- 分析场景中往往需要读大量行但是少数几个列
  - 在行存模式下，数据按行连续存储，所有列的数据都存储在一个block中，不参与计算的列在IO时也要全部读出，读取操作被严重放大
  - 而在列存模式下，只需要读取参与计算的列即可，极大的减低了IO cost，加速了查询
- 同一列中的数据属于同一类型，压缩效果显著
  - 列存往往有着高达十倍甚至更高的压缩比，节省了大量的存储空间，降低了存储成本
  - 更高的压缩比意味着更小的data size，从磁盘中读取相应数据耗时更短
- 自由的压缩算法选择
  - 不同列的数据具有不同的数据类型，适用的压缩算法也就不尽相同，可以针对不同列类型，选择最合适的压缩算法
  - 高压缩比，意味着同等大小的内存能够存放更多数据，系统cache效果更好

**缺点**
- 不适用于`Insert / Update`
- 不支持事务

### 有序存储

ClickHouse支持在建表时，指定将数据按照某些列进行sort by

- 排序后，保证了相同sort key的数据在磁盘上连续存储，且有序存储
- 在进行等值、范围查询时，where条件命中的数据都紧密存储在一个或若干个连续的Block中，而不是分散的存储在任意多个Block，大幅减少需要IO的block数量

### 数据分片

在分布式模式下，ClickHouse会将数据分为多个分片，并且分布到不同节点上。不同的分片策略在应对不同的SQL Pattern时，各有优势。ClickHouse提供了丰富的sharding策略，让业务可以根据实际需求选用

- random随机分片：写入数据会被随机分发到分布式集群中的某个节点上
- constant固定分片：写入数据会被分发到固定一个节点上。
- column value分片：按照某一列的值进行hash分片
- 定义表达式分片：指定任意合法表达式，根据表达式被计算后的值进行hash分片


数据分片让ClickHouse可以充分利用整个集群的大规模并行计算能力，快速返回查询结果

### 数据分区

ClickHouse支持PARTITION BY子句，在建表时可以指定按照任意合法表达式进行数据分区操作，比如
- 通过toYYYYMM()将数据按月进行分区
- 通过toMonday()将数据按照周几进行分区
- 对Enum类型的列直接每种取值作为一个分区
