import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import add_label, reverse_dict, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"5_isolate_step_3_histidine_kinase_family_small_predicted_02_v2.csv"))
print(small)

small_selected=small[["seq_id","seq","top1_label"]]
small_selected.columns=["seq_id","seq","pred"]
print(small_selected)

with open("/home/schen23/scratch/kinases/kinases_dataset/extra_p_133_class_v3/protein/multi_class/label.json","r") as f:
  label_ko=json.load(f)

small_selected=add_label(small_selected,reverse_dict(label_ko))
print(small_selected)

# small_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predic5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_4_histidine_kinase_ko.csv",index=False)
# df_to_fasta(small_selected,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/5_isolate_predictions/RumHKNet_predictions/step_1_02_step_2_02/5_isolate_step_4_histidine_kinase_ko.fasta",extra_column="pred_other")
