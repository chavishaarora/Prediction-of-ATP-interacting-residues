# this file converts the predicted data into the format required. 
import pandas as pd
import numpy as np 
df=pd.read_csv('/Users/chavishaarora/Desktop/Predictions.csv')
for i in range(len(df)):
    if df.iloc[i,1]==True:
        df.iloc[i,1]=1
    else:
        df.iloc[i,1]=-1
    # print(df.iloc[i,1])

df.to_csv('/Users/chavishaarora/Desktop/Submit.csv',index=False)
# print(df)