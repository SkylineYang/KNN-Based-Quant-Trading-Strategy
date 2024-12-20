#coding=UTF-8

import numpy as np
import pandas as pd

def get_most_effective_factor(df):
    df_corr = df.corr()#.abs()
    df_corr = df_corr.sort_values(by = '涨跌幅(%)', ascending = False)
    most_effective_factor_list = df_corr.index.values.tolist()[1:6]
    print(most_effective_factor_list)
    return most_effective_factor_list

def get_factors(filenames):
    factor_list = []
    for name in filenames:
        factor_list += get_most_effective_factor(pd.read_csv(name))
    result = pd.value_counts(factor_list)
    print(result)
    return

