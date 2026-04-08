import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific

dataset_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_2/both/clustered"

# i_df={}
small_dfs=[]
specific_total=0
for i in range(0,4):
  df_i=check_specific(predictions_path,f"newadd_155098MAGs_step_1_kinase_small_{i}")
  print(i,len(df_i))
  small_dfs.append(df_i)
  if i == 0:
    specific_total=specific_total+np.sum(df_i["prob"]>=0.2)
  else:
    specific_total=specific_total+np.sum(df_i["prob"]>=0.3)
kinase_small_df=pd.concat(small_dfs)
print(len(kinase_small_df))

chosen=kinase_small_df["prob"]>=0.2
histidine_kinase_small_df=kinase_small_df[kinase_small_df["pred"]==1]
print("small",len(histidine_kinase_small_df),np.sum(kinase_small_df["prob"]>=0.2),specific_total,np.sum(kinase_small_df["pred"]==1))
      
large=pd.read_csv(os.path.join(predictions_path,"newadd_155098MAGs_large_step_1_kinase_predicted_02_v2.csv"))
print(large)
large_histidine=large["label"]==1
print("large",np.sum(large["prob"]>=0.2),np.sum(large_histidine))

# large[large_histidine][["seq_id","seq"]].to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_3/clustered/newadd_155098MAGs_large_step_2_histidine_kinase.csv",index=False)
