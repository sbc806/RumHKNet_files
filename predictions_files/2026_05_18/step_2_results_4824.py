import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

small_df=check_specific(predictions_path,"4824human_newrun_step_1_kinase_small_predicted")
print(len(small_df))
print(np.sum(small_df["prob"]>=0.2),np.sum(small_df["pred"]==1))

large_df=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_step_1_kinase_large_predicted_02_v2.csv"))

print(len(large_df))
print(np.sum(large_df["prob"]>=0.2),np.sum(large_df["label"]==1))
print(max(large_df["seq"].str.len()))

small_histidine_kinase_df=small_df[small_df["pred"]==1]
print(len(small_histidine_kinase_df))
large_histidine_kinase_df=large_df[large_df["label"]==1]
print(len(large_histidine_kinase_df))
      
histidine_kinase_df=pd.concat([small_histidine_kinase_df[["seq_id","seq"]],large_histidine_kinase_df[["seq_id","seq"]]])
print(len(histidine_kinase_df),len(small_histidine_kinase_df)+len(large_histidine_kinase_df))
print(histidine_kinase_df)
# histidine_kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/4824human_newrun_step_2_histidine_kinase.csv",index=False)
print()

large_df.columns=small_df.columns
complete_df=pd.concat([small_df,large_df])
print("Number of predictions:",len(complete_df))
print(complete_df.columns)
save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_cluster_data/RumHKNet_predictions/4824human_newrun/step_1_02_step_2_02"
complete_df.to_csv(os.path.join(save_path,"4824human_newrun_step_2_predictions_02.csv"),index=False)
# df_to_fasta(histidine_kinase_df,os.path.join(save_path,"4824human_newrun_step_2_histidine_kinase_02.fasta"))
