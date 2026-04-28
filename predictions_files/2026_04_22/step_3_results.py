import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import add_label, reverse_dict, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_3/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_2_histidine_kinase_small_predicted_02.csv"))
print(len(small))
print(small)
print(small.columns)
small_0_1=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_2_histidine_kinase_small_0_1_predicted_02.csv"))
print(len(small_0_1))

def adjusted_df(df):
  df_selected=df[["seq_id","seq","top1_label"]]
  df_selected.columns=["seq_id","seq","batch"]
  df_selected.iloc[np.where(df_selected["batch"]==10)[0],2]=-1
  print(df_selected)
  return df_selected

small_selected=adjusted_df(small)
# small_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered/2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_small.csv",index=False)

small_0_1_selected=adjusted_df(small_0_1)
small_0_1_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered/2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_small_0_1.csv",index=False)

"""
small_selected=small[["seq_id","seq","top1_label"]]
small_selected.columns=["seq_id","seq","pred"]
with open("/home/schen123/scratch/kinases/kinases_dataset/step_3_11_family/protein/multi_class/label.json","r") as f:
  label_family=json.load(f)
small_selected=add_label(small_selected,reverse_dict(label_family))
print(small_selected)
"""
# small_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_3_histidine_kinase_family.csv",index=False)
# df_to_fasta(small_selected,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_3_histidine_kinase_family.fasta",extra_column="pred_other")
