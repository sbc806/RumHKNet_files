import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_1_dfs=[]
for i in range(0,4):
  df_i=check_specific(predictions_path,f"9342_all_proteins_newrun_1_small_{i}_predicted")
  print(i, len(df_i))
  small_1_dfs.append(df_i)
small_1_df=pd.concat(small_1_dfs)

threshold=0.2
print(f"Number of predictions for threshold {threshold}:",np.sum(small_1_df["prob"]>=threshold),np.sum(small_1_df["pred"]==1))

large_1_df=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_1_large_predicted_02_v2.csv"))
print(len(large_1_df))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_1_df["prob"]>=threshold),np.sum(large_1_df["label"]))
large_2_df=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_2_large_predicted_02_v2.csv"))
print(len(large_2_df))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_2_df["prob"]>=threshold),np.sum(large_2_df["label"]))

"""
complete_df=pd.concat([small_df,large_df])
print(len(complete_df),len(small_df),len(large_df),len(small_df)+len(large_df))
print(np.unique(complete_df["seq_id"]).shape,np.unique(complete_df["seq"]).shape)

small_kinase_df=small_df[small_df["pred"]==1][["seq_id","seq"]]
print(small_kinase_df)
small_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/4824human_newrun_step_1_kinase_small.csv",index=False)

large_kinase_df=large_df[large_df["label"]==1][["seq_id","seq"]]
print(large_kinase_df)
large_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/4824human_newrun_step_1_kinase_large.csv",index=False)
"""
