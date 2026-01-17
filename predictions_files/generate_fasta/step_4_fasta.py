import json
import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, reverse_dict, add_label

dataset_path="../../../predictions/predictions_results/step_4/clustered"
predictions_path="../../../predictions/predicted_results/step_4/both/clustered"

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
print(clustered_complete_small_df.columns)
predictions_information(clustered_complete_small_df)
clustered_large_df=pd.read_csv(os.path.join(predictions_path,"clustered_rep_seq95_large_histidine_kinase_batch_predicted_03.csv"))
print(clustered_large_df.columns)
predictions_information(clustered_large_df)

clustered_complete_small_df_selected=clustered_complete_small_df.iloc[:,0:2]
clustered_complete_small_df_selected["pred"]=clustered_complete_small_df.iloc[:,3]
clustered_large_df_selected=clustered_large_df.iloc[:,0:2]
clustered_large_df_selected["pred"]=clustered_large_df.iloc[:,3]

with open("../../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)
clustered_complete_small_df_new=add_label(clustered_complete_small_df_selected,reverse_dict(ko_label))
clustered_large_df_new=add_label(clustered_large_df_selected,reverse_dict(ko_label))
clustered_all_df=pd.concat([clustered_complete_small_df_new,clustered_large_df_new])
predictions_information(clustered_all_df)
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
newrun_complete_small_df_selected=newrun_complete_small_df.iloc[:,0:2]
newrun_complete_small_df_selected["pred"]=newrun_complete_small_df.iloc[:,3]
newrun_large_df_selected=newrun_large_df.iloc[:,0:2]
newrun_large_df_selected["pred"]=newrun_large_df.iloc[:,3]

with open("../../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)
newrun_complete_small_df_new=add_label(newrun_complete_small_df_selected,reverse_dict(ko_label))
newrun_large_df_new=add_label(newrun_large_df_selected,reverse_dict(ko_label))
newrun_all_df=pd.concat([newrun_complete_small_df_new,newrun_large_df_new])
predictions_information(newrun_all_df)
def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq=df.iloc[i]
      seq_id["seq_id"].iloc[i]
      pred=df.iloc[:,2].iloc[i]
      pred_other=df.iloc[:,3].iloc[i]
      f.write(">{seq_id},{seq},{pred},{pred_other}\n")
      f.write(seq)
      if i<len(df)-1:
        f.write("\n")

step_4_df=pd.concat([clustered_all_df,newrun_all_df])
step_4_fasta_path="../../../RumHKNet_fasta/step_4_histidine_kinase_batch_clustered_newrun.fasta")
# df_to_fasta(step_4_df,step_4_fasta_path)





