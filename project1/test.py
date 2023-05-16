import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

df=pd.read_csv('pre.csv')[20:].sample(frac=.3,replace=True)
# df2=pd.read_csv('pre1.csv')[20:]
# df=pd.concat([df,df2])
# df.fillna(0, inplace=True)
# df = df.reset_index()

# Binary

df1=df[['SMA','SMA_b','WMA_b','STCK_b','MOM_b','LWR_b','ADO_b','CCI_b','TREND']]

df1.to_csv('test.csv',index=False)

