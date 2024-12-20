#coding=UTF-8

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import time

def get_df(filename):
    df = pd.read_csv(filename).dropna()
    df = df.drop(columns = ['B股流通市值(元)', '总股本(股)'])
    print("File reading step completed", end = "\n\n")
    return df

def get_label(df): # 1为买入，0为持仓，-1为卖出
    labels = []
    df = df.sort_values(by = '涨跌幅(%)', ascending = True)
    increase = min(len(df[df['涨跌幅(%)'] > 0]), int(len(df) / 3))
    decrease = min(len(df[df['涨跌幅(%)'] < 0]), int(len(df) / 3))
    for i in range(len(df)):
        if i < increase:
            labels.append(1)
        elif i >= increase and i < len(df) - decrease:
            labels.append(0)
        else:
            labels.append(-1)
    df['Label'] = labels
    df = df.sort_index().dropna()
    print("Label marking step completed", end = "\n\n")
    return df

def get_model(df):
    knn = KNeighborsClassifier()
    train_X = df[['涨跌(元)', '成交量(股)', '换手率(%)', '成交金额(元)', '收盘价(元)']]
    train_Y = df['Label']
    knn.fit(train_X.values, np.ravel(train_Y))
    print("Model training step completed", end = "\n\n")
    return knn

def predict(model, df):
    y_predict = model.predict(df)
    print("Prediction step completed", end = "\n\n")
    return y_predict[0]

def get_signal(signal):
    print("Advice: ", end = "\n" + "*" * 20 + "\n")
    if signal == 1:
        print("Buy In")
    elif signal == -1:
        print("Sell")
    else:
        print("Hold")

def get_X():
    df_dict = {}
    df_dict['涨跌(元)'] = input("涨跌额：")
    df_dict['成交量(股)'] = input("成交量：")
    df_dict['换手率(%)'] = input("换手率：")
    df_dict['成交金额(元)'] = input("成交金额：")
    df_dict['收盘价(元)'] = input("收盘价：")
    X = pd.DataFrame([df_dict])
    print(X)
    return X
