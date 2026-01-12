import json
import os as os
import pandas as pd
import numpy as np
from predictions_helpers import predictions_information, reverse_dict, add_label

def make_df(dir_path):
  files=os.listdir(dir_path)
  dfs=[]
  for f in files:
    df=pd.read_csv(os.path.join(dir_path,f))
    dfs.append(df)
  return pd.concat(dfs)


dataset_path="../../predictions/predictions_dataset/step_3/clustered"
predictions_path="../../predictions/predicted_results/step_3/both/clustered"
small_histidine_df=make_df(os.path.join(predictions_path,"small_histidine_kinase"))
predictions_information(small_histidine_df)

large_histidine_df=pd.read_csv(os.path.join(predictions_path,"clustered_rep_seq95_large_histidine_kinase_predicted_03.csv"))
predictions_information(large_histidine_df)
"""
with open("../../sbc806/RumHKNet/kinases_dataset/step_3_11_family/protein/multi_class/label.json","r") as f:
  other_label=json.load(f)
small_histidine_df_new=add_label(small_histidine_df,other_label)

large_histidine_df_new=add_label(large_histidine_df,other_label)
"""
print(np.unique(pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/train/train.csv")))
print(np.unique(pd.read_csv("../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/dev/dev.csv")))
print(np.unique(pd.read_csv("../../sbc806/RumHKNet/kinase_dataset/extra_p_133_class_v3_batch/protein/multi_class/test/test.csv")))

small_histidine_df_batch=small_histidine_df.iloc[:,0:2]
small_histidine_df_batch["batch"]=small_histidine_df["pred"]
print(small_histidine_df_batch)

large_histidine_df_batch=large_histidine_df.iloc[:,0:2]
large_histidine_df_batch["batch"]=large_histidine_df["pred"]
print(large_histidine_df_batch)




