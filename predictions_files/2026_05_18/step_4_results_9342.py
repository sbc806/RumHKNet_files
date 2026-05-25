import json
import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta, add_label, reverse_dict


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

all_predictions=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_3_histidine_kinase_family_small_1_0123456_2_034_predicted_02_v2.csv"))
print("Number of predictions:",len(all_predictions))
print(all_predictions.columns)
all_predictions_remaining=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_step_3_histidine_kinase_family_remaining_predicted_02_v2.csv"))
print("Number of predictions:",len(all_predictions_remaining))
print(all_predictions_remaining.columns)
