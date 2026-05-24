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

small_df_2_12=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_1_kinse_small_2_12_predicted_02_v2.csv"))
print(len(small_df_2_12))
print(np.sum(small_df_2_12["prob"]>=0.2),np.sum(small-df_2_12["plabel"]==1))

print()

small_df_2_5=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_1_kinase_small_2_5_predicted_02_v2.csv"))
print(len(small_df_2_5))
print(np.sum(small_df_2_5["prob"]>=0.2),np.sum(small_df_2_5["label"]==1))

print()
