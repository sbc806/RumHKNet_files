import pandas as pd
import os as os
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information

dataset_path="../../../predictions/predictions_dataset/step_2/clustered"
predictions_path="../../../predictions/predicted_results/step_2/both/clustered"

step_2_predicted_rbag_df=pd.read_csv("../../../RumHKNet_csv/step_2_clustered_newrun_rbags_predicted_03.csv")

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
for f in os.listdir(total_blastp3050_small_dir_path_0):
  df=pd.read_csv(os.path.join(total_blastp3050_small_dir_path_0,f))
  total_blastp3050_small_dfs.append(df)
for f in os.listdir(total_blastp3050_small_dir_path_1):
  df=pd.read_csv(os.path.join(total_blastp3050_small_dir_path_1,f))
  total_blastp3050_small_dfs.append(df)

total_blastp3050_large_path=os.path.join(predictions_path,"2025_01_20_new_blastp3050_shared_large_predicted_03.csv")
total_blastp3050_large_df=pd.read_csv(total_blastp3050_large_path)

total_ko_small_df=pd.concat(total_ko_small_dfs)
total_ko_large_df.columns=total_ko_small_df.columns
total_ko_df=pd.concat([total_ko_small_df,total_ko_large_df])
predictions_information(total_ko_df)

tottal_blastp3050_small_df=pd.concat(total_blastp3050_small_dfs)
total_blastp3050_large_df.columns=total_blastp3050_small_df.columns
total_blastp3050_df=pd.concat([total_blastp3050_small_df,total_blastp3050_large_df])
predictions_information(total_blastp3050_df)

predictions_information(step_2_predicted_rbag_df)









