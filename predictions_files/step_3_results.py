import os as os
import pandas as pd
import numpy as np
from predictions_helpers import predictions_information

def make_df(dir_path):
  files=os.listdir(dir_path)
  dfs=[]
  for f in files:
    df=pd.read_csv(os.path.join(f))
    dfs.append(df)
  return pd.concat(dfs)


dataset_path="../../predictions/predictions_dataset/step_3/clustered"
predictions_path="../../predictions/predicted_results/step_3/both/clustered"
small_histidine_df=make_df(os.path.join(predictions_path,"small_histidine_kinase"))
predictions_information(small_histidine_df)

large_histidine_df=pd.read_csv(os.path.join(predictions_path,"clustered_rep_seq95_large_histidine_kinase_predicted_03.csv"))
predictions_information(large_histidine_df)
