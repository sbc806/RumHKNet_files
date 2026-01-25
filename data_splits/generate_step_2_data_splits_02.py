import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_files.predictions_helpers import predictions_information

step_1_rbag_02_df=pd.read_csv("../../predictions/predictions_dataset/step_2/clustered/step_1_clustered_newrun_rbags_02_not_contained.csv")
predictions_information(step_1_rbag_02_df)
step_1_rbag_02_small_df=step_1_rbag_02_df[step_1_rbag_02_df["seq"].str.len()<=1500]
step_1_rbag_02_large_df=step_1_rbag_02_df[step_1_rbag_02_df["seq"].str.len()>1500]

split_size=900000
num_splits=len(step_1_rbag_02_small_df)//split_size+1
dfs=[]
for i in range(0,num_splits):
  start=i*split_size
  end=start+split_size
  step_1_rbag_02_small_df_i=step_1_rbag_02_small_df[start:end]
  step_1_rbag_02_small_df_i.to_csv(f"../../predictions/predictions_dataset/step_2/clustered/step_1_clustered_newrun_rbags_02_not_contained_{i}.csv",index=False)
  dfs.append(step_1_rbag_02_small_df_i)
print(len(step_1_rbag_02_small_df),len(pd.concat(dfs)))






