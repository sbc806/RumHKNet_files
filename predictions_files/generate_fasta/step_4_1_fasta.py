import json
import os as os
import pandas as pd
import numpy as np
import sys
sys.path.append("..")
from predictions_helpers import predictions_information, reverse_dict, add_label

dataset_path="../../../predictions/predictions_results/step_4/clustered"
predictions_path="../../../predictions/predicted_results/step_4/both/clustered"

with open("../../../sbc806/RumHKNet/kinases_dataset/extra_p_133_class_v3_batch/protein/multi_class/label.json","r") as f:
  ko_label=json.load(f)


def df_to_fasta(df,fasta_path):
  with open(fasta_path,"a") as f:
    for i in range(0,len(df)):
      seq=df["seq"].iloc[i]
      seq_id=df["seq_id"].iloc[i]
      pred=df.iloc[:,2].iloc[i]
      pred_other=df.iloc[:,3].iloc[i]
      f.write(f">{seq_id},{pred},{pred_other}\n")
      f.write(seq)
      if i<len(df)-1:
        f.write("\n")

step_4_03_df=pd.read_csv("../../../RumHKNet_csv/step_1_03_step_2_03/step_4_03/step_4_clustered_newrun_rbags_predicted_03.csv")

step_4_02_small_remaining_df=pd.read_csv(os.path.join(predictions_path,"step_4_clustered_newrun_rbags_02_small_remaining_batch_predicted_03_v2.csv")).iloc[:,0:4]
step_4_02_large_remaining_df=pd.read_csv(os.path.join(predictions_path,"step_4_clustered_newrun_rbags_02_large_remaining_batch_predicted_03.csv")).iloc[:,0:4]
print(step_4_02_small_remaining_df.columns)
print(step_4_02_large_remaining_df.columns)
step_4_02_remaining_df=pd.concat([step_4_02_small_remaining_df,step_4_02_large_remaining_df])
step_4_02_remaining_df.columns=step_4_03_df.columns
print(step_4_02_remaining_df)
print(step_4_03_df)
step_4_02_df=pd.concat([step_4_03_df,step_4_02_remaining_df])
predictions_information(step_4_02_df)

step_4_02_df.to_csv("../../../RumHKNet_csv/step_4_clustered_newrun_rbags_predicted_02.csv",index=False)

step_4_02_df_selected=step_4_02_df.loc[:,["seq_id","seq","pred"]]
step_4_02_df_new=add_label(step_4_02_df_selected,reverse_dict(ko_label))
print(step_4_02_df_new)
print(np.unique(step_4_02_df_new["pred"]))
print(np.unique(step_4_02_df_new["pred_other"]))

df_to_fasta(step_4_02_df_new,"../../../RumHKNet_fasta/step_4_histidine_kinase_ko_clustered_newrun_rbags_674002.fasta")
























