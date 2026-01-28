import os as os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import predictions_information

def create_df(dir_path):
  dfs=[]
  for f in os.listdir(dir_path):
    df=pd.read_csv(os.path.join(dir_path,f))
    dfs.append(df)
  return pd.concat(dfs)
  
small_dfs=[]
for i in range(0,3):
  smmall_dir="clustered_newrun_rbags_02_not_contained_small_{i}"
  small_dir_path=os.path.join(predictions_path,small_dir)
  small_df=create_df(small_dir_path)
  small_dfs.append(small_df)
complete_small_df=pd.concat(small_dfs)

large_dir_path=os.path.join(predictions_path,"step_1_clustered_newrun_rbags_02_not_contained_large_predicted_03_v2.csv")
large_df=pd.read_csv(large_dir_path)
large_df.columns=complete_small_df.columns

step_1_02_not_contained_df=pd.concat([complete_small_df,large_df])
predictions_information(step_1_02_not_contained_df)

step_1_03_df=pd.read_csv("../../../RumHKNet_csv/step_2_03/step_2_clustered_newrun_rbags_predicted_03.csv")
step_2_predicted_df=pd.concat([step_1_03_df,step_1_02_not_contained_df])
predictions_information(step_2_predicted_df)

step_1_df=pd.read_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03.csv")

print(np.sum(step_2_predicted_df["seq_id"].isin(step_1_df["seq_id"].values)))



