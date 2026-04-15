import os
import numpy as np
import pandas as pd

dir_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases"

rumhknet_path=os.path.join(dir_path,"RumHKNet_csv/step_1_02_step_2_02")
rumhknet=pd.read_csv(os.path.join(rumhknet_path,"step_1_clustered_newrun_rbags_predicted_02.csv"))
print(len(rumhknet))

unique=pd.read_csv(os.path.join(dir_path,"unique_clustered_rep_seq_All140086RBAGs_95_90.csv"))
print(len(unique))

def get_information(df):
  print("Number of unique sequence IDs:",np.unique(df["seq_id"]).shape)
  print("Number of unique sequences:",np.unique(df["seq"]).shape)

get_information(rumhknet)
print()
get_information(unique)

print()

contained=unique["seq_id"].isin(rumhknet["seq_id"].values)
print(np.sum(contained),np.sum(~contained))

selected=rumhknet["seq_id"].isin(unique["seq_id"].values)
print(np.sum(selected)
rumhknet[selected].to_csv(os.path.join(dir_path,"unique_clustered_rep_seq_All140086RBAGs_95_90_step_1_predictions_02.csv"),index=False)
