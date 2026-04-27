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
