import pandas as pd
import os as os
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, get_interval

dataset_path="../../../predictions/predictions_dataset/step_2/clustered"
predictions_path="../../../predictions/predicted_results/step_2/both/clustered"

# step_1_predicted_rbag_df=pd.read_csv("../../../RumHKNet_csv/step_1_clustered_newrun_rbags_predicted_03.csv")
step_2_predicted_rbag_df=pd.read_csv("../../../RumHKNet_csv/step_2_clustered_newrun_rbags_predicted_03.csv")
step_2_predicted_rbag_histidine_df=step_2_predicted_rbag_df[step_2_predicted_rbag_df.iloc[:,3]==1]

print("total_KO")
total_ko_small_dir_path=os.path.join(predictions_path,"total_ko_small_kinase")
total_ko_small_dfs=[]
for f in os.listdir(total_ko_small_dir_path):
  df=pd.read_csv(os.path.join(total_ko_small_dir_path,f))
  # print(df)
  total_ko_small_dfs.append(df)

total_ko_large_path=os.path.join(predictions_path,"2025_01_20_new_ko_shared_large_predicted_03.csv")
total_ko_large_df=pd.read_csv(total_ko_large_path)

print("total_blastp3050")
total_blastp3050_small_dir_path_0=os.path.join(predictions_path,'total_blastp3050_small_kinase_0')
total_blastp3050_small_dir_path_1=os.path.join(predictions_path,'total_blastp3050_small_kinase_1')
total_blastp3050_small_dfs=[]
for f in sorted(os.listdir(total_blastp3050_small_dir_path_0)[:-1]):
  df=pd.read_csv(os.path.join(total_blastp3050_small_dir_path_0,f))
  # print(f,df)
  total_blastp3050_small_dfs.append(df)
for f in os.listdir(total_blastp3050_small_dir_path_1):
  df=pd.read_csv(os.path.join(total_blastp3050_small_dir_path_1,f))
  # print(f,df)
  total_blastp3050_small_dfs.append(df)

total_blastp3050_large_path=os.path.join(predictions_path,"2025_01_20_new_blastp3050_shared_large_predicted_03.csv")
total_blastp3050_large_df=pd.read_csv(total_blastp3050_large_path)

total_ko_small_df=pd.concat(total_ko_small_dfs)
total_ko_large_df.columns=total_ko_small_df.columns
total_ko_df=pd.concat([total_ko_small_df,total_ko_large_df])
predictions_information(total_ko_df)

total_blastp3050_small_df=pd.concat(total_blastp3050_small_dfs)
total_blastp3050_large_df.columns=total_blastp3050_small_df.columns
total_blastp3050_df=pd.concat([total_blastp3050_small_df,total_blastp3050_large_df])
predictions_information(total_blastp3050_df)

predictions_information(step_2_predicted_rbag_df)

print()
print("Number of histidine kinases predicted in step 2 using RumHKNet and threshold 0.3:",np.sum(step_2_predicted_rbag_df.iloc[:,3]==1))
print("Number of histidine kinases in common with total_KO:",np.sum(step_2_predicted_rbag_histidine_df["seq_id"].isin(total_ko_df["seq_id"].values)))
print("Number of histidine kinases in common with total_blastp3050:",np.sum(step_2_predicted_rbag_histidine_df["seq_id"].isin(total_blastp3050_df["seq_id"].values)))
print()
print("Shared:",np.sum(total_ko["seq_id"].isin(total_blastp3050["seq_id"].values)))
print("total_KO")
intervals=[[0.0,0.1],[0.1,0.2],[0.2,0.3],[0.3,0.4],[0.4,0.5],[0.5,0.6],[0.6,0.7],[0.7,0.8],[0.8,0.9],[0.9,1.0]]
for each_interval in intervals:
  min_prob=each_interval[0]
  max_prob=each_interval[1]
  selected_rows=get_interval(total_ko_df,min_prob,max_prob)
  print(min_prob,max_prob,len(selected_rows))

print()
print("total_blastp3050")

for each_interval in intervals:
  min_prob=each_interval[0]
  max_prob=each_interval[1]
  selected_rows=get_interval(total_blastp3050_df,min_prob,max_prob)  
  print(min_prob,max_prob,len(selected_rows))

print(np.histogram(total_ko_df.iloc[:,2],bins=10))
print(np.histogram(total_blastp3050_df.iloc[:,2],bins=10))

print(np.sum(total_ko_df["seq_id"].isin(step_2_predicted_rbag_df["seq_id"].values)))
print(np.sum(total_blastp3050_df["seq_id"].isin(step_2_predicted_rbag_df["seq_id"].values)))

print()
print("total_ko")
for each_interval in intervals:
  min_prob=each_interval[0]
  max_prob=each_interval[1]
  

















