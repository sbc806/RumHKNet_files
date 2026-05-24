import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_3/both/clustered"

all_predictions=pd.read_csv(os.path.join(predictions_path,"4824human_newrun_step_2_histidine_kinase_predicted_02.csv"))
print("Number of predictions:",len(all_predictions))
print(all_predictions.columns)
