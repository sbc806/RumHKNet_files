import os as os
import numpy as np
import pandas as pd

def check_specific(dir_path,f_name):
  files-os.listdir(dir_path)
  selected_files=[fnfor f in files if f_name in f]

  dfs=[]
  for f in selected_files:
    df=pd.read_csv(os.path.join(dir_path,f))
    dfs.append(df)
  return pd.concat(dfs)
