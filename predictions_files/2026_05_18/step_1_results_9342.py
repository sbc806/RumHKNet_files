import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_1_dfs=[]
for i in range(0,7):
  df_i=check_specific(predictions_path,f"9342_all_proteins_newrun_1_small_{i}_predicted")
  print(i, len(df_i))
  small_1_dfs.append(df_i)
small_1_df=pd.concat(small_1_dfs)

threshold=0.2
print(f"Number of predictions for threshold {threshold}:",np.sum(small_1_df["prob"]>=threshold),np.sum(small_1_df["pred"]==1))
print()

small_2_dfs=[]
selected=[0,3,4]
for i in selected:
  df_i=check_specific(predictions_path,f"9342_all_proteins_newrun_2_small_{i}_predicted")
  print(i,len(df_i))
  small_2_dfs.append(df_i)
small_2_df=pd.concat(small_2_dfs)
print(len(small_2_df))
print(f"Number of predictions for threshold {threshold}:",np.sum(small_2_df["prob"]>=threshold),np.sum(small_2_df["pred"]==1))

small_df=pd.concat([small_1_df,small_2_df])
small_kinase_df=small_df[small_df["pred"]==1][["seq_id","seq"]]
print(small_kinase_df)
# small_kinase_df.iloc[0:400000].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_newrun_step_1_kinase_small_0.csv",index=False)
# small_kinase_df.iloc[400000:].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_newrun_step_1_kinase_small_1.csv",index=False)
print()

small_dfs_2_12=[]
for i in [1,2]:
  df_i=check_specific(predicions_path,f"9342_all_proteins_newrun_2_small_{i}_prediccted")
  print(i,len(df_i))
  small_dfs_2_12.append(df_i)
small_df_2_12=pd.concat(small_dfs_2_12)
print(len(small_df_2_12))
print(f"Number of predictions for threshold {threshold}:", np.sum(small_df_2_12["prob"]>=threshold),np.sum(small_df_2_12["pred"]==1))

print()

small_df_2_5=check_specific(predictions_path,f"9342_all_proteins_newrun_2_small_5_predicted")
print(5,len(small_df_2_5))
print(np.sum(small_df_2_5["prob"]>=0.2),np.sum(small_df_2_5["pred"]==1))
small_kinase_df_2_5=small_df_2_5[small_df_2_5["pred"]==1][["seq_id","seq"]]
print(small_kinase_df_2_5)
# small_kinase_df_2_5.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_newrun_step_1_kinase_small_2_5.csv",index=False)
print()

large_1_df=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_1_large_sorted_predicted_02_v2.csv"))
print(len(large_1_df))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_1_df["prob"]>=threshold),np.sum(large_1_df["label"]))

large_1_kinase_df=large_1_df[large_1_df["label"]==1]
print(max(large_1_kinase_df["seq"].str.len()))

large_2_df=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_2_large_sorted_predicted_02_v2.csv"))
print(len(large_2_df))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_2_df["prob"]>=threshold),np.sum(large_2_df["label"]))

large_2_kinase_df=large_2_df[large_2_df["label"]==1]
print(max(large_2_kinase_df["seq"].str.len()))
print()

large_kinase_df=pd.concat([large_1_kinase_df,large_2_kinase_df])[["seq_id","seq"]]
print(large_kinase_df)
# large_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_newrun_step_1_kinase_large_1_2.csv",index=False)

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
