import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_3/both/clustered"

small_step_3=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_small_step_2_histidine_kinase_predicted_02.csv"))
print(small_step_3.columns)
print(small_step_3["top1_label"])
print(small_step_3)

small_step_3_selected=small_step_3[["seq_id","seq","top1_label"]]
small_step_3_selected.columns=["seq_id","seq","batch"]
small_step_3_selected.iloc[np.where(small_step_3_selected["batch"]==10)[0],2]=-1
print(small_step_3_selected)
# small_step_3_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered/newadd_155098MAGs_small_step_3_histidine_kinase_family.csv",index=False)

large_step_3=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_large_step_2_histidine_kinase_predicted_02.csv"))
print(large_step_3.columns)
print(large_step_3["top1_label"])
print(large_step_3)

large_step_3_selected=large_step_3[["seq_id","seq","top1_label"]]
large_step_3_selected.columns=["seq_id","seq","batch"]
large_step_3_selected.iloc[np.where(large_step_3_selected["batch"]==10)[0],2]=-1
print(large_step_3_selected)
# large_step_3_selected.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered/newadd_155098MAGs_large_step_3_histidine_kinase_family.csv",index=False)
