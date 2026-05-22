import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific, df_to_fasta

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

small_1_dfs=[]
for i in range(0,8):
  df_i=check_specific(dataset_path,f"9342_all_proteins_newrun_1_small_{i}")
  print(i, len(df_i))

small_2_dfs=[]
selected=[0,1,2,3,4,5]
for i in selected:
  df_i=check_specific(dataset_path,f"9342_all_proteins_newrun_2_small_{i}")
  print(i,len(df_i))


large_1_df=pd.read_csv(os.path.join(predictions_path,"9342_all_proteins_newrun_1_large.csv"))
print(len(large_1_df))

large_2_df=pd.read_csv(os.path.join(dataset_path,"9342_all_proteins_newrun_2_large.csv"))
print(len(large_2_df))
