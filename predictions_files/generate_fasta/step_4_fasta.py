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
  
