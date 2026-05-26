import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_dfs=[]
for i in range(0,3):
  df_i=check_specific(predictions_path,f"4824human_newrun_small_{i}_predicted")
  print(i, len(df_i))
  small_dfs.append(df_i)
small_df=pd.concat(small_dfs)

threshold=0.2
print(f"Number of predictions for threshold {threshold}:",np.sum(small_df["prob"]>=threshold),np.sum(small_df["pred"]==1))

large_df=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_large_predicted_02_v2.csv"))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_df["prob"]>=threshold),np.sum(large_df["label"]==1))

complete_df=pd.concat([small_df,large_df])
print(len(complete_df),len(small_df),len(large_df),len(small_df)+len(large_df))
print(np.unique(complete_df["seq_id"]).shape,np.unique(complete_df["seq"]).shape)

small_kinase_df=small_df[small_df["pred"]==1][["seq_id","seq"]]
print(small_kinase_df)
# small_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/4824human_newrun_step_1_kinase_small.csv",index=False)

large_kinase_df=large_df[large_df["label"]==1][["seq_id","seq"]]
print(large_kinase_df)
# large_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/4824human_newrun_step_1_kinase_large.csv",index=False)
print()

large_df.columns=small_df.columns
complete_predictions_df=pd.concat([small_df,large_df])
print("Number of total predictions:",len(complete_predictions_df))
print(complete_predictions_df.columns)
complete_kinase_df=pd.concat([small_kinase_df,large_kinase_df])
print(f"Number of predicted kinases for threshold {threshold}:",len(complete_kinase_df),len(small_kinase_df),len(large_kinase_df),len(small_kinase_df)+len(large_kinase_df))

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_cluster_data/RumHKNet_predictions/4824human_newrun/step_1_02_step_2_02"
complete_predictions_df.to_csv(os.path.join(save_path,"4824human_newrun_step_1_predictions_02.csv"),index=False)
# df_to_fasta(complete_kinase_df,os.path.join(save_path,"4824human_newrun_step_1_kinase_02.fasta"))
