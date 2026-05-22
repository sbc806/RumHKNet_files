import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, check_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_dfs=[]
for i in range(0,3):
  df_i=check_specific(predictions_path,f"4824human_newrun_small_{i}_predicted")
  print(i, len(df_i))
  small_dfs.append(df_i)
small_df=pd.concat(small_df)

threshold=0.2
print(f"Number of predictions for threshold {threshold}:",np.sum(small_df["prob"]>=threshold),np.sum(small_df["pred"]==1))

large_df=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_large_predicted_02_v2.csv"))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_df["prob"]>=threshold),np.sum(large_df["label"]))

complete_df=pd.concat([small_df,large_df])
print(len(complete_df),len(small_df),len(large_df),len(small_df)+len(large_df))
print(np.unique(complete_df["seq_id"]).shape,np.unique(complete_df["seq"]).shape)
