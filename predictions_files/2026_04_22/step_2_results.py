import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import check_specific

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"


small_1=check_specific(predictions_path,"2026_04_22_clustered95_rep_seq_step_1_kinase_small_predicted")
print(len(small_1))
threshold=0.2
small_1_kinase=small_1["prob"]>=0.2
print(f"Threshold {threshold}:",np.sum(small_1_kinase),np.sum(small_1["pred"]==1))
small_1_kinase_chosen=small_1[small_1_kinase][["seq_id","seq"]]
print(small_1_kinase_chosen)
# small_1_kinase_chosen.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/2026_04_22_clustered95_rep_seq_step_2_histidine_kinase_small.csv",index=False)

small_0_1=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_step_1_kinase_small_remaining_1_predicted_02_1500_v3_0.csv"))
print(len(small_0_1))
small_0_1_kinase=small_0_1["prob"]>=0.2
print(f"Threshold {threshold}:",np.sum(small_0_1_kinase),np.sum(small_0_1["pred"]==1))
small_0_1_kinase_chosen=small_0_1[small_0_1_kinase][["seq_id","seq"]]
print(small_0_1_kinase_chosen)
