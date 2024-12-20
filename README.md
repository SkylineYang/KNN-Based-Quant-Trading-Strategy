# KNN-Based-Quant-Trading-Strategy

## 基于KNN算法的量化交易策略

将6支股票的历史数据打上标签（-1为卖出，0为持仓，1为买入），并根据KNN进行训练集的划分。在获得股票当日最新的各项特征时，便可作为特征对此时的股票状态进行分类，从而提示应卖出/持仓/买入。

Label the historical data of 6 stocks (with -1 for sell, 0 for hold, and 1 for buy), and divide the training set based on KNN. When obtaining the latest features of the stock on the current day, these features can be used to classify the stock's status, thereby providing a recommendation to sell, hold, or buy.
