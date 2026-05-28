import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

small_dfs_1_0123456_2_034=[]
for i in range(0,2):
  df_i=check_specific(predictions_path,f"9342_all_proteins_newrun_step_1_kinase_small_{i}_predicted")
  small_dfs_1_0123456_2_034.append(df_i)
small_df_1_0123456_2_034=pd.concat(small_dfs_1_0123456_2_034)
print(len(small_df_1_0123456_2_034))
print(np.sum(small_df_1_0123456_2_034["prob"]>=0.2),np.sum(small_df_1_0123456_2_034["pred"]==1))
small_histidine_kinase_df_1_0123456_2_034=small_df_1_0123456_2_034[small_df_1_0123456_2_034["pred"]==1][["seq_id","seq"]]
print(small_histidine_kinase_df_1_0123456_2_034)
# small_histidine_kinase_df_1_0123456_2_034.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/9342_all_proteins_newrun_step_2_histidine_kinase_small_1_0123456_2_034.csv",index=False)
print()

small_df_2_12=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_1_kinase_small_2_12_predicted_02_v2.csv"))
print(len(small_df_2_12))
print(np.sum(small_df_2_12["prob"]>=0.2),np.sum(small_df_2_12["label"]==1))
small_histidine_kinase_df_2_12=small_df_2_12[small_df_2_12["label"]==1][["seq_id","seq"]]
print(small_histidine_kinase_df_2_12)

print()

small_df_2_5=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_1_kinase_small_2_5_predicted_02_v2.csv"))
print(len(small_df_2_5))
print(np.sum(small_df_2_5["prob"]>=0.2),np.sum(small_df_2_5["label"]==1))
small_histidine_kinase_df_2_5=small_df_2_5[small_df_2_5["label"]==1][["seq_id","seq"]]
print(small_histidine_kinase_df_2_5)

print()

large_df_1_2=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_1_kinase_large_1_2_predicted_02_v2.csv"))
print(len(large_df_1_2))
print(np.sum(large_df_1_2["prob"]>=0.2),np.sum(large_df_1_2["label"]==1))
large_histidine_kinase_df_1_2=large_df_1_2[large_df_1_2["label"]==1][["seq_id","seq"]]
print(large_histidine_kinase_df_1_2)
print(max(large_histidine_kinase_df_1_2["seq"].str.len()))
print()

histidine_kinase_df_remaining=pd.concat([small_histidine_kinase_df_2_12,small_histidine_kinase_df_2_5,large_histidine_kinase_df_1_2])
print(len(histidine_kinase_df_remaining),histidine_kinase_df_remaining.columns)
# histidine_kinase_df_remaining.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/9342_all_proteins_newrun_step_2_histidine_kinase_remaining.csv",index=False)
print()

small_df_2_12.columns=small_df_1_0123456_2_034.columns
small_df_2_5.columns=small_df_1_0123456_2_034.columns
large_df_1_2.columns=small_df_1_0123456_2_034.columns
complete_df=pd.concat([small_df_1_0123456_2_034,small_df_2_12,small_df_2_5,large_df_1_2])
print(f"Number of predictions:",len(complete_df))
print(complete_df.columns)
complete_histidine_kinase_df=pd.concat([small_histidine_kinase_df_1_0123456_2_034,histidine_kinase_df_remaining])
print(f"Number of predicted histidine kinases with threshold 0.2:",np.sum(complete_df["pred"]==1),len(complete_histidine_kinase_df))
print(complete_histidine_kinase_df.columns)

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_cluster_data/RumHKNet_predictions/9342_all_proteins_newrun/step_1_02_step_2_02"
# complete_df.to_csv(os.path.join(save_path,"9342_all_proteins_newrun_step_2_predictions_02.csv"),index=False)
# df_to_fasta(complete_histidine_kinase_df,os.path.join(save_path,"9342_all_proteins_newrun_step_2_histidine_kinase_02.fasta"))
