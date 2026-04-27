import os
import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from predictions_helpers import check_specific

dataset_path= "/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_1/clustered"
predictions_path="/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predicted_results/step_1/both/clustered"

i_df={}
small=[]
small_total=0
selected=[2,3]
small_i=[]
small_remaining=[]
small_remaining_i=[]
for i in range(0,7):
  df=check_specific(predictions_path,f"2026_04_22_clustered95_rep_seq_small_{i}_predicted")
  print(i,len(df))
  small.append(df)
  small_total=small_total+len(df)
  
  if i in selected:
    df_remaining=check_specific(predictions_path,f"2026_04_22_clustered95_rep_seq_small_{i}_remaining")
    small_total=small_total+len(df_remaining)
    small_remaining.append(df_remaining)
    
    print(f"{i}_remaining",len(df_remaining))
    
    small_dataset=pd.read_csv(os.path.join(dataset_path,f"2026_04_22_clustered95_rep_seq_small_{i}.csv"))
    small_full=pd.concat([df,df_remaining])
    print("Length:",len(small_dataset),len(small_full))
    print("Equal:",np.sum(small_dataset["seq_id"].values==small_full["seq_id"].values),np.sum(small_dataset["seq"].values==small_full["seq"].values))
    
    
print("Number of predictions for sequences with length <=1500:",small_total)
small_all=pd.concat(small)
threshold=0.2
small_kinase=small_all["prob"]>=threshold
print(f"Number of predicted kinases with threshold {threshold}:",np.sum(small_kinase),np.sum(small_all["pred"]==1))
small_all_kinase=small_all[small_kinase][["seq_id","seq"]]
print(small_all_kinase)
# small_all_kinase.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/2026_04_22_clustered95_rep_seq_step_1_kinase_small.csv",index=False)
# small_all_kinase.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/2026_04_22_clustered95_rep_seq_step_1_kinase_small_2_3.csv",index=False)

small_remaining_all_1=pd.concat(small_remaining)
print(len(small_remaining_all_1))
small_kinase_remaining_1=small_remaining_all_1["prob"]>=threshold
print(f"Number of predicted kinases with threshold {threshold}:",np.sum(small_kinase_remaining_1),np.sum(small_remaining_all_1["pred"]==1))
small_remaining_all_kinase_1=small_remaining_all_1[small_kinase_remaining_1][["seq_id","seq"]]
print(small_remaining_all_kinase_1)
# small_remaining_all_kinase_1.to_csv("/home/schen123/projects/rrg-guanuofa/schen123/kinases/predictions/predictions_dataset/step_2/clustered/2026_04_22_clustered95_rep_seq_step_1_kinase_small_remaining_1.csv",index=False)

# large=pd.read_csv(os.path.join(predictions_path,"2026_04_22_clustered95_rep_seq_large_predicted_02_v2.csv"))
# print("Number of predictions for sequences with length >1500:",len(large))
large_2=pd.read_csv(os.path.joni(predictions_path,"2026_04_22_clustered95_rep_seq_large_2_predicted_02_v2.csv"))
print(len(large_2))
print(np.sum(large_2["prob"]>=threshold),np.sum(large_2["pred"]==1))
