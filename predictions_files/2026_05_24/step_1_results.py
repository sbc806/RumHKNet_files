import os
import numpy as np

import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific


dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_individual=[]

small_3=check_specific(predictions_path,"9342_all_proteins_remove2_small_3")
print(len(small_3))
print(np.sum(small_3["prob"]>=0.2),np.sum(small_3["pred"]==1))
print()

large=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_remove2_large_sorted_predicted_02_v2.csv"))
print(len(large))
print(np.sum(large["prob"]>=0.2),np.sum(large["label"]==1))
