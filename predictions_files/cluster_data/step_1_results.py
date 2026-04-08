import os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import check_specific
from predictions_helpers import split_chunks

dataset_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"


i_df={}
for i in range(0,5):
  df_i=check_specific(predictions_path,f"newadd_155098MAGs_small_{i}")
  print(i,len(df_i))
  i_df[i]=df_i

print("Number of predictions for sequences <= 1500:", np.concat(i_df.values()))

kinase_dfs=[]
for i in i_df:
  df_i=i_df[i]
  print(i,np.sum(df_i["prob"]>=0.2),np.sum(df_i["pred"]))
  kinase_dfs.append(df_i[df_i["pred"]==1])

kinase_small_df=pd.concat(kinase_dfs)[["seq_id","seq"]]
print(len(kinase_small_df))
print(kinase_small_df)
chunk_size=200000
# split_chunks(kinase_small_df,chunk_size,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered","newadd_155098MAGs_step_1_kinase")
# kinase_small_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/newadd_155098MAGs_small_step_1_kinase.csv",index=False)

large_df=pd.read_csv(os.path.join("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/newadd_155098MAGs_large_predicted_02_v2.csv"))
print(len(large_df))
large_df.columns=i_df[0].columns
print(np.sum(large_df["prob"]>=0.2),np.sum(large_df["pred"]))

kinase_large_df=large_df[large_df["pred"]==1][["seq_id","seq"]]
print(len(kinase_large_df))
print(kinase_large_df)
# kinase_large_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/newadd_155098MAGs_large_step_1_kinase.csv",index=False)
