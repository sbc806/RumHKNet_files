import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import add_label, reverse_dict, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_small_predicted_02_v2.csv"))
print(len(small))
small_0_1=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_small_0_1_predicted_02_v2.csv"))
print(len(small_0_1))
small_2_3=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_small_2_3_predicted_02_v2.csv"))
print(len(small_2_3))

large_1=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_3_histidine_kinase_family_large_1_predicted_02_v2.csv"))
print(len(large_1))

print()
complete=pd.concat([small,small_0_1,small_2_3,large_1])
print("Number of predictions",len(complete))
print(np.unique(complete["seq_id"]).shape,np.unique(complete["seq"]).shape)
print()

complete_selected=complete[["seq_id","seq","top1_label"]]
complete_selected.columns=["seq_id","seq","pred"]
print(complete_selected)

with open("/home/schen123/scratch/kinases/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)

complete_selected=add_label(complete_selected,reverse_dict(ko_label))
print(complete_selected)

save_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/2026_04_22_clustered95_rep_seq_predictions/RumHKNet_predictions/step_1_02_step_2_02"
save_name="2026_04_22_clustered95_rep_seq_step_4_histidine_kinase_ko_label"
complete_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_4_histidine_kinase_ko.csv",index=False)
df_to_fasta(complete_selected,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_4_histidine_kinase_ko.fasta",extra_column="pred_other")
