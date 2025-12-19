import os
import numpy as np
import pandas as pd

csv_path = "../predictions/predictions_dataset/step_2/clustered/clustered_rep_seq95_small_kinase.csv"
df_small_seq=pd.read_csv(csv_path)
split_size=2450000
total_length=len(df_small_seq)//split_size+1
all_dfs=[]
for i in range(0,total_length):
  start=i*split_size
  end=start+split_size
  selected_df=df_small_seq[start:end]
  if i == total_length-1:
    selected_df=df_small_seq[start:]
  all_dfs.append(selected_df)
  print(selected_df)
  selected_df.to_csv(f"../predictions/predictions_dataset/step_2/clustered/clustered_rep_seq95_small_kinase_{i}.csv",index=False)
df_small_seq_1=pd.concat(all_dfs)
print(np.sum(df_small_seq["seq_id"]==df_small_seq_1["seq_id"]))
