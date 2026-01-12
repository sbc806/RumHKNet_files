import os as os
import pandas as pd
import numpy as np

def make_df(dir_path):
  files=os.listdir(dir_path)
  dfs=[]
  for f in files:
    df=pd.read_csv(os.path.join(f))
    dfs.append(df)
  return pd.concat(dfs)

