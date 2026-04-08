import os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import check_specific
from predictions_helpers import split_chunks
from prediction_helpers import df_to_fasta

dataset_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path = "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"


i_df={}
small_dfs=[]
for i in range(0,5):
  df_i=check_specific(predictions_path,f"newadd_155098MAGs_small_{i}")
  print(i,len(df_i))
  i_df[i]=df_i
  small_dfs.append(df_i)
  
print("Number of predictions for sequences <= 1500:", len(pd.concat(small_dfs)))
print(np.unique(pd.concat(small_dfs)["seq_id"]).shape,np.unique(pd.concat(small_dfs)["seq"]).shape)

kinase_dfs=[]
for i in i_df:
  df_i=i_df[i]
  print(i,np.sum(df_i["prob"]>=0.2),np.sum(df_i["pred"]))
  kinase_dfs.append(df_i[df_i["pred"]==1])

kinase_small_df=pd.concat(kinase_dfs)[["seq_id","seq"]]
print("Number of predicted kinases for sequences <= 1500:",len(kinase_small_df))
print(kinase_small_df)
chunk_size=200000
# split_chunks(kinase_small_df,chunk_size,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered","newadd_155098MAGs_step_1_kinase")
# kinase_small_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/newadd_155098MAGs_small_step_1_kinase.csv",index=False)

large_df=pd.read_csv(os.path.join("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/newadd_155098MAGs_large_predicted_02_v2.csv"))
print("Number of predictions for sequences > 1500:",len(large_df))
print(np.unique(large_df["seq_id"]).shape,np.unique(large_df["seq"]).shape)
large_df.columns=i_df[0].columns
print(np.sum(large_df["prob"]>=0.2),np.sum(large_df["pred"]))

kinase_large_df=large_df[large_df["pred"]==1][["seq_id","seq"]]
print("Number of predicted kinases for sequences > 1500:",len(kinase_large_df))
print(kinase_large_df)
# kinase_large_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/newadd_155098MAGs_large_step_1_kinase.csv",index=False)

print(kinase_small_df.columns,kinase_large_df.columns)
kinase_df=pd.concat([kinase_small_df,kinase_large_df])
kinase_df.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/cluster_data_predictions/RumHKNet_predictions/step_1_02_step_2_02/newadd_155098MAGs_step_1_kinase_02.csv",index=False)
df_to_fasta(kinase_df,"/home/schen123/projects/rrg-guanuofa/schen123/kinases/cluster_data_predictions/RumHKNet_predictions/step_1_02_step_2_02/newadd_155098MAGs_step_1_kinase_02.fasta")
