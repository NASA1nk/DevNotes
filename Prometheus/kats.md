# Kats

**Kits to Analyze Time Series**

FaceBook开源的一款**轻量级的**、**易于使用的**、**通用**的时间序列分析框架

## 功能

Kats的核心四大功能包括

- **模型预测**（Forecasting）
  - Kats提供了一套完整的预测工具，包括10+个单独的预测模型、ensembling、自监督学习（meta-learning）模型、backtesting、超参数调整和经验预测区间。
- **检测**（Anomaly and Change Point Detection）
  - Kats支持检测时间序列数据的各种模式的功能，包括季节性、异常值、变化点和缓慢的趋势变化检测。
- **特征提取与嵌入**（Feature Extraction）
  - Kats中的时间序列特征（TSFeature）提取模块可以产生65个具有明确统计定义的特征，这些特征可以应用于大多数机器学习（ML）模型，如分类和回归。
- Kats还提供了一组有用的实用程序，例如时间序列模拟器。



## kats Basics

`TimeSeriesData`

Kats中用来表示单变量和多变量时间序列的基本数据结构

**初始化**

- `TimeSeriesData(df)`
  - `df`要求是一个包含`time`列和**任意值列**的`pd.DataFrame`对象
- `TimeSeriesData(time, value)`
  - `time`是`pd.Series`或`pd.DatetimeIndex`对象，
  - `value`是`pd.Series`（单变量）或`pd.DataFrame`（多变量）

**操作**

**TimeSeriesData**对象支持标准`pandas.DataFrame`的许多相同操作

- Slicing切片取数
- Math Operations数学计算
- Extend扩充
- Plotting绘图
- Utility Functions实用函数
  - to_dataframe
  - to_array
  - is_empty
  - is_univariate



## 预测算法

目前支持以下10种基本预测模型

1. Linear
2. Quadratic
3. ARIMA
4. SARIMA
5. Holt-Winters
6. Prophet
7. AR-Net
8. LSTM
9. Theta
10. VAR

> 每个模型都遵循`sklearn`模型API模式：创建模型类的一个实例，然后调用它的`fit()`和`predict()`方法



## 异常检测

Kats提供了一组模型和算法来检测时间序列数据中的异常值、变化点和趋势变化

**异常检测算法**

- Outlier Detection：使用OutlierDetector检测异常尖峰

- Change Point Detection：检测变化前后具有不同的统计特征的突然变化，变点检测

- - CUSUM Detection：累积和的检测
  - Bayesian Online Change Point Detection (BOCPD)：贝叶斯在线变化点检测
  - Stat Sig Detection：统计信号检测

- Trend Change Detection：趋势变化检测 MKDetector（Mann-Kendall）

