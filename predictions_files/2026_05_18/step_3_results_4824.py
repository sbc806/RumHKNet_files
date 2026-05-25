import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta, add_label, reverse_dict


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_3/both/clustered"

all_predictions=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_step_2_histidine_kinase_predicted_02.csv"))
print("Number of predictions:",len(all_predictions))
print(all_predictions.columns)


def adjusted_df(df):
  df_selected=df[["seq_id","seq","top1_label"]]
  df_selected.columns=["seq_id","seq","batch"]
  df_selected.iloc[np.where(df_selected["batch"]==10)[0],2]=-1
  print(df_selected)
  return df_selected
  
all_predictions_selected=adjusted_df(all_predictions)
# all_predictions_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered/4824human_newrun_step_3_histidine_kinase_family.csv",index=False)
print()

print(np.unique(all_predictions["seq_id"]).shape,np.unique(all_predictions["seq"]).shape)

all_predictions_selected=all_predictions[["seq_id","seq","top1_label"]]
all_predictions_selected.columns=["seq_id","seq","pred"]
with open("/home/schen123/scratch/kinases/kinases_dataset/step_3_11_family/protein/multi_class/label.json","r") as f:
  label_family=json.load(f)
complete_selected=add_label(complete_selected,reverse_dict(label_family))
print(complete_selected)

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_clustered_data/RumHKNet_predictions/4824human_newrun/step_1_02_step_2_02"
save_name="4824human_newrun_step_3_histidine_kinase_family"
complete_selected.to_csv(os.path.join(save_path,f"{save_name}.csv"),index=False)
df_to_fasta(complete_selected,os.path.join(save_path,f"{save_name}.fasta"),extra_column="pred_other")

