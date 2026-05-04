import os
import numpy as np
import pandas as pd


def get_unique_information(df):
  print("Number of unique sequences:",len(df))
  print("Number of unique sequence IDs:",np.unique(df["seq_id"]).shape)
  print("Number of unique sequences:",np.unique(df["seq"])/shape)

def compare(df_1,df_2)
  get_unique_information(df_1)
  get_unique_information(df_2)
  seq_argsort_1=np.argsort(df_1["seq"].values)
  seq_argsort_2=np.argsort(df_2["seq"].values)
  print(df_1.columns)
  print(df_2.columns)
  df_1=df_1.iloc[seq_argsort_1]
  df_2=df_2.iloc[seq_argsort_2]
  for column in df_1.columns:
    print(np.sum(df_1[column].values==df_2[column]).values,np.sum(df_1[column].values!=df_2[column].values))
