import os as os
import numpy as np
import pandas as pd
# from step_1_step_2_combined_datasets import split_chunks

def check_specific(dir_path,f_name):
  files=os.listdir(dir_path)
  selected_files=[f for f in files if f_name in f]

  dfs=[]
  for f in selected_files:
    df=pd.read_csv(os.path.join(dir_path,f))
    df.columns=["seq_id","seq","prob","pred"]
    # print(df.columns)
    # print(f,len(df))
    dfs.append(df)
  return pd.concat(dfs)

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1_step_2_combined/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1_step_2_combined/both/clustered"

small_27=pd.read_csv(os.path.join(dataset_path,"unique_clustered_rep_seq_All140086RBAGs_95_90_remaining_small_27.csv"))
print(len(small_27))

selected_i=[27]
i_df={}
total_predicted_kinases=0
for i in selected_i:
  df_i=check_specific(predictions_path,f"unique_clustered_rep_seq_All140086RBAGs_95_90_remaining_small_{i}")
  i_df[i]=df_i
  print(i,len(df_i),"Number of predicted kinases:",np.sum(df_i["prob"]>=0.1),np.sum(df_i["prob"]>=0.2),np.sum(df_i["pred"]))
  total_predicted_kinases=total_predicted_kinases+np.sum(df_i["pred"])
  
large=pd.read_csv(os.path.join(dataset_path,"unique_clustered_rep_seq_All140086RBAGs_95_90_remaining_large.csv"))
large_predicted=pd.read_csv(os.path.join(predictions_path,"unique_clustered_rep_seq_All140086RBAGs_95_90_remaining_large_predicted_02_v2.csv"))
print(len(large),len(large_predicted))
large_predicted.columns=i_df[27].columns
print("Number of predicted large kinases:",np.sum(large_predicted["prob"]>=0.1),np.sum(large_predicted["prob"]>=0.2),np.sum(large_predicted["pred"]))
large_contained=large["seq_id"].isin(large_predicted["seq_id"].values)
print(np.sum(large_contained),np.sum(~large_contained))
