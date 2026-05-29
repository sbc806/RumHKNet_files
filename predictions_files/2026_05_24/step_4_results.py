import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta, add_label, reverse_dict


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

all_predictions=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_remove2_step_3_histidine_kinase_family_small_3_large_predicted_02_v2.csv"))
print("Number of predictions:",len(all_predictions))
print(all_predictions.columns)
# all_predictions_remaining=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_3_histidine_kinase_family_remaining_predicted_02_v2.csv"))
# print("Number of predictions:",len(all_predictions_remaining))
# print(all_predictions_remaining.columns)


"""
complete=pd.concat([all_predictions,all_predictions_remaining])

print(np.unique(complete["seq_id"]).shape,np.unique(complete["seq"]).shape)
print()

complete_selected=complete[["seq_id","seq","top1_label"]]
complete_selected.columns=["seq_id","seq","pred"]
print(complete_selected)

with open("/home/schen123/scratch/kinases/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)

complete_selected=add_label(complete_selected,reverse_dict(ko_label))
print(complete_selected)

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_05_18_cluster_data/RumHKNet_predictions/9342_all_proteins_newrun/step_1_02_step_2_02"
save_name="9342_all_proteins_newrun_step_4_histidine_kinase_ko"
complete_selected.to_csv(os.path.join(save_path,f"{save_name}.csv"),index=False)
df_to_fasta(complete_selected,os.path.join(save_path,f"{save_name}.fasta"),extra_column="pred_other")
"""
