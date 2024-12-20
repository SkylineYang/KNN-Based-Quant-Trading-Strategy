#coding=UTF-8

import numpy as np
import pandas as pd
import Data
import Correlationship as Cor

csv_names = ['比亚迪002594.csv', '国药600511.csv', '科兴688136.csv', '山东钢铁600022.csv', '永泰能源600157.csv', '山煤国际600546.csv']

action = input("Action: ")
while action.find("quit") == -1:
    if action.find("Cor") >= 0 or action.find("cor") >= 0:
        print("*" * 20, end = "\n\n")
        Cor.get_factors(csv_names)
    elif action.find("Sto") >= 0 or action.find("sto") >= 0:
        print("*" * 20, end = "\n\n")
        name = input("Stock Name/Stock Code:")
        print("*" * 20, end = "\n\n")
        for csv_name in csv_names:
            if csv_name.find(name) > 0:
                print(csv_name.replace(".csv", ""), end = "\n\n")
                df = Data.get_label(Data.get_df(csv_name))
                model = Data.get_model(df)
                X = Data.get_X()
                Data.get_signal(Data.predict(model, X))
    else:
        print("error: Undefined Action")
    print("*" * 20, end = "\n\n")
    action = input("Action: ")


print("Program Finished")
# print(df_list)
