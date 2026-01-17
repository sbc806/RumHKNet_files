import osd as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information

dataset_path="../../../predictions/predictions_results/step_4/clustered"
predictions_path="../../../prediction/predicted_results/step_4/both/clustered"

print("clustered_rep_seq95")
dir_0_path=os.path.join(predictions_path,"small_histidine_kinase_batch_0")
dir_1_path=os.path.join(predictions_path,"small_histidine_kinase_batch_1")
small_dfs=[]
for f in os.listdir(dir_0_path):
  df=pd.read_csv(os.path.join(dir_0_path,f))
  small_dfs.append(df)
for f in os.listdir(dir_1_path):
  df=pd.read_csv(os.path.join(dir_1_path,f))
  small_dfs.append(df)
  
clustered_complete_small_df=pd.concat(small_dfs)
print(clustered_complete_small_df)
predictions_information(clustered_complete_small_df)
clustered_large_df=pd.read_csv(os.path.join(predictions_path,"clustered_rep95_seq_large_histidine_kinase_batch_predicted_03.csv"))
print(clustered_large_df.columns)
predictions_information(clustered_large_df)

dir_path=os.path.join(predictions_path,"newrun_seqs_small_histidine_kinase_batch")
small_dfs=[]
for f in os.listdir(dir_path):
  df=pd.read_csv(os.path.join(dir_path,f))
  small_dfs.append(df)
newrun_complete_small_df=pd.concat(small_dfs)
print(newrun_complete_small_df.columns)
predictions_information(newrun_complete_small_df)

newrun_large_df=pd.read_csv(os.path.join(predictions_path,"newrun_seqs_large_histidine_kinase_batch_predicted_03.csv"))
print(newrun_large_df.columns)
predictions_information(newrun_large_df)
