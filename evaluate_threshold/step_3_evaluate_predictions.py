import pandas as pd
import os as os
import numpy as np

dataset_path="../../predictions/predictions_dataset/step_3/"
predictions_path="../../predictions/predicted_results/step_3/both"

step_3_dev_0=pd.read_csv(os.path.join(predictions_path,"step_3_11_family_dev_predicted_03.csv"))
step_3_dev_1=pd.read_csv(os.path.join(predictions_path,"step_3_11_family_dev_predicted_03_3432_v4_0.csv"))

print(step_3_dev_0)
print(step_3_dev_1)
print(step_3_dev_0.columns)
print(step_3_dev_1.columns)
print()

print("Number of seq_id in common:",np.sum(step_3_dev_0["seq_id"]==step_3_dev_1["seq_id"]))
print("Number of seq in common:",np.sum(step_3_dev_0["seq"]==step_3_dev_1["seq"]))
