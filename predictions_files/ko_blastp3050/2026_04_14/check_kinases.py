import os
import pandas as pd
import numpy as np

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

blastp_kofamscan_path=os.path.join(dir_path,"2026_04_14_blastp_kofamscan/cluster_data")

def get_df(dir_path,desired_file="")
  chosen=[f for f in dir_path if desired_file in f and "predictions" in f]
  dfs=[]
  for f in chosen:
    df=pd.read_csv(os.path.join(dir_path,f))
    print(df.columns)
    dfs.append(df)
  return pd.concat(dfs)
