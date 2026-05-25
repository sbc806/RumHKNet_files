import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta, add_label, reverse_dict


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

all_predictions=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_step_3_histidine_kinase_family_predicted_02_v2.csv"))
print("Number of predictions:",len(all_predictions))
print(all_predictions.columns)


def adjusted_df(df):
  df_selected=df[["seq_id","seq","top1_label"]]
  df_selected.columns=["seq_id","seq","batch"]
  df_selected.iloc[np.where(df_selected["batch"]==10)[0],2]=-1
  print(df_selected)
  return df_selected
  
all_predictions_selected=adjusted_df(all_predictions)


"""
complete=pd.concat([small,small_0_1,small_2_3,large_1])
print("Number of predictions:",len(complete))
print(np.unique(complete["seq_id"]).shape,np.unique(complete["seq"]).shape)

complete_selected=complete[["seq_id","seq","top1_label"]]
complete_selected.columns=["seq_id","seq","pred"]
with open("/home/schen123/scratch/kinases/kinases_dataset/step_3_11_family/protein/multi_class/label.json","r") as f:
  label_family=json.load(f)
complete_selected=add_label(complete_selected,reverse_dict(label_family))
print(complete_selected)

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_22_clustered95_rep_seq_predictions/RumHKNet_predictions/step_1_02_step_2_02"
save_name="2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family"
# complete_selected.to_csv(os.path.join(save_path,f"{save_name}.csv"),index=False)
# df_to_fasta(complete_selected,os.path.join(save_path,f"{save_name}.fasta"),extra_column="pred_other")
"""
