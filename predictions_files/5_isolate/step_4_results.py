import os
import numpy as np
import pandas as pd

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_4/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_4/both/clustered"

small=pd.read_csv(os.path.join(predictions_path,"5_isolate_step_3_histidine_kinase_family_small_predicted_02_v2.csv"))
print(small)
