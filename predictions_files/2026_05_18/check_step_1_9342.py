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
  df_i=pd.read_csv(os.path.join(dataset_path,f"9342_all_proteins_newrun_1_small_{i}.csv"))
  print(i, len(df_i))

small_2_dfs=[]
selected=[0,1,2,3,4,5]
for i in selected:
  df_i=pd.read_csv(os.path.join(dataset_path,f"9342_all_proteins_newrun_2_small_{i}.csv"))
  print(i,len(df_i))


large_1_df=pd.read_csv(os.path.join(dataset_path,"9342_all_proteins_newrun_1_large.csv"))
print(len(large_1_df))
large_1_df_argsort=np.argsort(large_1_df["seq"].str.len())
large_1_df_sorted=large_1_df.iloc[large_1_df_argsort]
print(large_1_df_sorted)
large_1_df_sorted.to_csv(os.path.join(dataset_path,"9342_all_proteins_newrun_1_large_sorted.csv"),index=False)

large_2_df=pd.read_csv(os.path.join(dataset_path,"9342_all_proteins_newrun_2_large.csv"))
print(len(large_2_df))
large_2_df_argsort=np.argsort(large_2_df["seq"].str.len())
large_2_df_sorted=large_2_df.iloc[large_2_df_argsort]
print(large_2_df_sorted)
large_2_df_sorted.to_csv(os.path.join(dataset_path,"9342_all_proteins_newrun_2_large_sorted.csv"),index=False)
