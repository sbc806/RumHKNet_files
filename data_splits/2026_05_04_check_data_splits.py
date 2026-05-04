import os
import numpy as np
import pandas as pd


def get_dfs(dir_path):
  train=pd.read_csv(os.path.join(dir_path,"train/train.csv"))
  dev=pd.read_csv(os.path.join(dir_path,"dev/dev.csv"))
  test=pd.read_csv(os.path.join(dir_path,"test/test.csv"))
  print(len(train),len(dev),len(test))
  return train, dev, test
  
def get_unique_information(df):
  print("Number of unique sequences:",len(df))
  print("Number of unique sequence IDs:",np.unique(df["seq_id"]).shape)
  print("Number of unique sequences:",np.unique(df["seq"]).shape)

def compare(df_1,df_2):
  get_unique_information(df_1)
  get_unique_information(df_2)
  seq_argsort_1=np.argsort(df_1["seq"].values)
  seq_argsort_2=np.argsort(df_2["seq"].values)
  print(df_1.columns)
  print(df_2.columns)
  df_1=df_1.iloc[seq_argsort_1]
  df_2=df_2.iloc[seq_argsort_2]
  for column in df_1.columns:
    if column!="seq_id":
      print(column,"Equal:",np.sum(df_1[column].values==df_2[column].values),"Not equal:",np.sum(df_1[column].values!=df_2[column].values))

dir_path="/home/schen123/scratch/kinases"
step_1="step_1_non_kinases_preprocessed/protein/binary_class"
step_2="extra_p_2_class_v3_kinases_only/protein/binary_class"
step_2_1="step_2/protein/binary_class"
step_3="step_3_11_family/protein/multi_class"
step_4="extra_p_133_class_v3_batch/protein/multi_class"
step_dir=step_3
dir_path_1=os.path.join(dir_path,f"kinases_dataset/{step_dir}")
dir_path_2=os.path.join(dir_path,f"test_code/kinases_dataset/{step_dir}")

dfs_1=get_dfs(dir_path_1)
dfs_2=get_dfs(dir_path_2)
print()
"""
protein_types=["non_kinase_","other_kinase_","histidine_kinase_"]
for i in range(0,3):
  for each_type in protein_types:
    print(each_type,np.sum(dfs_1[i]["seq_id"].str.contains(each_type)),np.sum(dfs_2[i]["seq_id"].str.contains(each_type)))
print()
"""
unique_labels=np.unique(dfs_1[0]["label"])
for label in unique_labels:
  for i in range(0,3):
    print(label,np.sum(dfs_1[i]["label"]==label),np.sum(dfs_2[i]["label"]==label))
print()
df_1=pd.concat(dfs_1)
df_2=pd.concat(dfs_2)
get_unique_information(df_1)
get_unique_information(df_2)
print()
compare(df_1,df_2)
