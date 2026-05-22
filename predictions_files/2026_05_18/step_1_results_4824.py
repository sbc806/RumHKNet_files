import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, echeck_fasta

small_dfs=[]
for i in range(0,3):
  df_i=check_specific(predictions_path,f"4824human_newrun_small_{i}_predicted")
  print(i, len(df_i))
  small_dfs.append(df_i)

large_df=pd.read_csv(os.path.join(predictions_path,"4924human_newrun_large_predicted_02_v2.csv"))
print(f"Number of predictions for threshold {threshold}:",np.sum(large_df["prob"]>=threshold),np.sum(large_df["label"]))
