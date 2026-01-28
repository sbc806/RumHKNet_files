import os as os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import predictions_information


small_dfs=[]
for i in range(0,3):
  smmall_dir="clustered_newrun_rbags_02_not_contained_small_{i}"
  small_dir_path=os.path.join(predictions_path,small_dir)
  small_df=create_df(small_dir_path)
  small_dfs.append(small_df)

large_dir_path=os.path.join(predictions_path,"step_1_clustered_newrun_rbags_02_not_contained_large_predicted_03_v2.csv")
large_df=pd.read_csv(large_dir_path)

step_1_not_contained_02_df=pd.concat([complete_small_df,large_df])
step_1_df=pd.read_csv("../../../")
