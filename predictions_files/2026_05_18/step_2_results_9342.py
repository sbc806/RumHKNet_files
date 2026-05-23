import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

small_dfs_034=[]
for i in range(0,2):
  df_i=check_specific(predictions_path,f"9342_all_proteins_newrun_step_1_kinase_small_{i}_predicted")
  small_dfs_034.append(df_i)
small_df_034=pd.concat(small_dfs_034)
print(len(small_df_034))
print(np.sum(small_df_034["prob"]>=0.2),np.sum(small_df_034["pred"]==1))
