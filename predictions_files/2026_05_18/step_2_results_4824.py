import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

small_df=check_specific(predictions_path,"4824human_newrun_step_1_kinase_small_predicted")
print(len(small_df))
print(np.sum(small_df["prob"]>=0.2),np.sum(small_df["pred"]==1))

large_df=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_step_1_kinase_large_predicted_02_v2.csv"))

print(len(large_df))
print(np.sum(large_df["prob"]>=0.2),np.sum(large_df["label"]==1))
