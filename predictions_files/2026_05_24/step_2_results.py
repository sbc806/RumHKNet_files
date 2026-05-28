import os
import numpy as np

import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"


small_individual=[]
for i in range(0,3):
  small_i=check_specific(predictions_path,f"9342_all_proteins_remove2_step_1_kinase_small_012_{i}")
  print(i,len(small_i))
  small_individual.append(small_i)
small_012=pd.concat(small_individual)
print(len(small_012))
print(np.sum(small_012["prob"]>=0.2),np.sum(small_012["pred"]==1))
small_012_histidine_kinase=small_012[small_012["pred"]==1]
print(len(small_012_histidine_kinase))
small_012_histidine_kinase[["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/9342_all_proteins_remove2_step_2_histidine_kinase_small_012.csv",index=False)

small_3=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_remove2_step_1_kinase_small_3_predicted_02_v2.csv"))
print(len(small_3))
print(np.sum(small_3["prob"]>=0.2),np.sum(small_3["label"]==1))
small_3_histidine_kinase=small_3[small_3["label"]==1]
print(len(small_3_histidine_kinase))
print()

large=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_remove2_step_1_kinase_large_predicted_02_v2.csv"))
print(len(large))
print(np.sum(large["prob"]>=0.2),np.sum(large["label"]==1))
large_histidine_kinase=large[large["label"]==1]
print(len(large_histidine_kinase),max(large_histidine_kinase["seq"].str.len()))
print()

small_3_large_histidine_kinase=pd.concat([small_3_histidine_kinase,large_histidine_kinase])
print(len(small_3_large_histidine_kinase))
# small_3_large_histidine_kinase[["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/9342_all_proteins_remove2_step_2_histidine_kinase_small_3_large.csv",index=False)

"""
large.columns=small_012.columns
print(large.columns)
complete=pd.concat([small_012,small_3,large])
print(len(complete),np.unique(complete["seq_id"]).shape,np.unique(complete["seq"]).shape)
"""
print()

print(small_012.columns)
small_3.columns=small_012.columns
large.columns=small_012.columns
print(small_3.columns)
print(large.columns)
complete=pd.concat([small_012,small_3,large])
print(len(complete),len(small_012),len(small_3),len(large),len(small_012)+len(small_3)+len(large))
print(np.sum(complete["pred"]>=1),len(small_012_histidine_kinase),len(small_3_histidine_kinase),len(large_histidine_kinase),len(small_012_histidine_kinase)+len(small_3_histidine_kinase)+len(large_histidine_kinase))
complete_histidine_kinase=pd.concat([small_012_histidine_kinase,small_3_histidine_kinase,large_histidine_kinase])
print(len(complete_histidine_kinase))

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_24/RumHKNet_predictions/step_1_02_step_2_02"
# complete.to_csv(os.path.join(save_path,"9342_all_proteins_remove2_step_2_predictions_02.csv"),index=False)
# df_to_fasta(complete_histidine_kinase,os.path.join(save_path,"9342_all_proteins_remove2_step_2_histidine_kinase_02.fasta"))
