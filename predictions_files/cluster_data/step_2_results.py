import os
import numpy as np
import pandas as pd

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/predictions/predicted_results/step_2/both/clustered"

large=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_large_step_1_kinase_predicted_02_v2.csv"))
print(large)
