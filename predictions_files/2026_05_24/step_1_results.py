import os
import numpy as np

import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_individual=[]
for i in range(0,3):
  small_i=check_specific(predictions_path,f"9342_all_proteins_remove2_small_{i}")
  print(i,len(small_i))
  small_individual.append(small_i)
small_012=pd.concat(small_individual)
print(len(small_012))
print(np.sum(small_012["prob"]>=0.2),np.sum(small_012["pred"]==1))
small_012_kinase=small_012[small_012["pred"]==1]
print(len(small_012_kinase))
# small_012_kinase[["seq_id","seq"]].iloc[0:70000].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_remove2_step_1_kinase_small_012_0.csv",index=False)
# small_012_kinase[["seq_id","seq"]].iloc[70000:140000].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_remove2_step_1_kinase_small_012_1.csv",index=False)
# small_012_kinase[["seq_id","seq"]].iloc[140000:].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_remove2_step_1_kinase_small_012_2.csv",index=False)

small_3=check_specific(predictions_path,"9342_all_proteins_remove2_small_3")
print(len(small_3))
print(np.sum(small_3["prob"]>=0.2),np.sum(small_3["pred"]==1))
small_3_kinase=small_3[small_3["pred"]==1]
print(len(small_3_kinase))
# small_3_kinase[["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_remove2_step_1_kinase_small_3.csv",index=False)
print()

large=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_remove2_large_sorted_predicted_02_v2.csv"))
print(len(large))
print(np.sum(large["prob"]>=0.2),np.sum(large["label"]==1))
large_kinase=large[large["label"]==1]
print(len(large_kinase),max(large_kinase["seq"].str.len()))

# large_kinase[["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/9342_all_proteins_remove2_step_1_kinase_large.csv",index=False)
print()

large.columns=small_012.columns
print(large.columns)
complete=pd.concat([small_012,small_3,large])
print(len(complete),np.unique(complete["seq_id"]).shape,np.unique(complete["seq"]).shape)
complete_kinase=complete[complete["pred"]==1]
print(len(complete_kinase),len(small_012_kinase),len(small_3_kinase),len(large_kinase),len(small_012_kinase)+len(small_3_kinase)+len(large_kinase))

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_24/RumHKNet_predictions/step_1_02_step_2_02"
complete.to_csv(os.path.join(save_path,"9342_all_proteins_remove2_step_1_predictions_02.csv"),index=False)
df_to_fasta(complete,os.path.join(save_path,"9342_all_proteins_remove2_step_1_kinase_02.fasta"))
