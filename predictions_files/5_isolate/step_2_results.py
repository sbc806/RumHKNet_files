import os
import numpt numpy as np
import pandas as pd

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clusterd"

small=pd.read_csv(os.path.join(predictions_path,"5_isolate_step_1_kinase_small_predicted_02_v2.csv"))
print(len(small))
print(np.sum(small["prob"]>=0.2),np.sum(small["label"]==1))
